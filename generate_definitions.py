"""
Script to generate definitions and learning information for lemmas using LLM APIs.
"""

import json
import os
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Dict, Optional, Any
import time
from pathlib import Path
import logging
import anthropic
from openai import OpenAI
import hashlib
from datetime import datetime

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# STATIC PROMPT CONTENT - DEFINED ONCE
STATIC_PROMPT_CONTENT = """You are a Spanish language expert creating concise, English-speaking language learner-focused definitions for Spanish lemmas.

EXTREMELY IMPORTANT - LEMMA FIELD REQUIREMENTS:
- The "lemma" field in your response MUST be EXACTLY the same as provided in the word list
- Do NOT translate, modify, capitalize, or change the lemma in any way
- Do NOT add accents, remove accents, or alter the spelling
- Copy each lemma EXACTLY as written in the provided list

CRITICAL - AVOID CROSS-LANGUAGE CONFUSION:
- You are analyzing SPANISH lemmas from SPANISH text corpora
- If a word is not used in Spanish, identify it as such and mark should_learn as false
- If a word appears to be a proper noun (place name, person name, brand), identify it as such
- If a word looks like it might be from another language, consider if it's actually a proper noun or loan word in Spanish context
- When in doubt about proper nouns, mark should_learn as false and identify the proper noun type

PROPER NOUN IDENTIFICATION:
- Place names (cities, regions, countries): mark countries as should_learn: True and provide a definition. For all other place names, only mark as should_learn: True if they a significantly different between languages and highly relevant to Spanish learners
- Brand names: Always mark as should_learn: false
- Person names: Always mark as should_learn: false
- If a word could be either a common noun OR a proper noun, prioritize the proper noun interpretation if it appears in frequency data

NON-SPANISH WORD DETECTION (CRITICAL):
- English loanwords that are NOT integrated into Spanish: Mark should_learn as FALSE
- Examples of NON-integrated: "marketing", "email", "software", "business", "online" when used in English contexts
- Examples of INTEGRATED: "fútbol", "champú", "estrés", "wifi", "internet" (when used as Spanish words)
- If it appears in Spanish text but retains English pronunciation/usage, mark should_learn as FALSE

VERB CONJUGATION ACCURACY (CRITICAL):
- -ar verbs: "1st conjugation (-ar)" (caminar, hablar, estudiar)
- -er verbs: "2nd conjugation (-er)" (comer, beber, correr, obtener)
- -ir verbs: "3rd conjugation (-ir)" (vivir, escribir, salir)
- Irregular verbs: "irregular" (ser, estar, ir, haber, tener, hacer, decir, poder, querer)
- Stem changing verbs: provide the category of the verb and add (stem changing) after the verb group
- DOUBLE-CHECK: Verify the infinitive ending before assigning conjugation group

GRAMMATICAL METADATA ACCURACY:
- Gender: Only assign to nouns and adjectives that actually have gender
- Transitiveness: Verify if verbs actually take direct objects
- Part of speech: Be precise - distinguish between adjectives and nouns carefully, if multiple parts of speech are possible, consider whether two separate definitions are needed
- Prepositions: Only include if the word commonly requires a specific preposition

INSTRUCTIONS:
Create definitions that are helpful for Spanish language learners. Prioritize clarity and conciseness over comprehensive dictionary-style explanations.

DEFINITION GUIDELINES:
- If there's a direct English translation that covers the meaning well, use that as the definition
- Only provide longer explanations when there's no direct one-to-one translation
- Avoid overly academic or verbose language
- Include context only when valuable to a time-limited learner

GLOSS GUIDELINES:
- Provide the single most common English word that best translates the Spanish word
- Choose the most frequent/useful translation for learners
- If multiple meanings exist, choose the most common one for the gloss

EXAMPLES:

Example 1 - Direct translation available:
{
  "lemma": "gato",
  "definitions": [
    {
      "definition": "cat",
      "gloss": "cat",
      "part_of_speech": "noun",
      "gender": "masculine",
      "verb_group": null,
      "accompanying_preposition": null,
      "case_triggered": null,
      "transitiveness": null
    }
  ],
  "should_learn": true,
  "has_error": false,
  "error_description": null
}

Example 2 - Multiple meanings, concise definitions:
{
  "lemma": "banco",
  "definitions": [
    {
      "definition": "bank (financial institution)",
      "gloss": "bank",
      "part_of_speech": "noun",
      "gender": "masculine",
      "verb_group": null,
      "accompanying_preposition": null,
      "case_triggered": null,
      "transitiveness": null
    },
    {
      "definition": "bench (seat)",
      "gloss": "bench",
      "part_of_speech": "noun",
      "gender": "masculine",
      "verb_group": null,
      "accompanying_preposition": null,
      "case_triggered": null,
      "transitiveness": null
    }
  ],
  "should_learn": true,
  "has_error": false,
  "error_description": null
}

Example 3 - Verb with correct conjugation:
{
  "lemma": "obtener",
  "definitions": [
    {
      "definition": "to obtain, get",
      "gloss": "obtain",
      "part_of_speech": "verb",
      "gender": null,
      "verb_group": "2nd conjugation (-er)",
      "accompanying_preposition": null,
      "case_triggered": null,
      "transitiveness": "transitive"
    }
  ],
  "should_learn": true,
  "has_error": false,
  "error_description": null
}

Example 4 - Cultural concept requiring explanation:
{
  "lemma": "sobremesa",
  "definitions": [
    {
      "definition": "time spent talking at the table after a meal",
      "gloss": "after-dinner",
      "part_of_speech": "noun",
      "gender": "feminine",
      "verb_group": null,
      "accompanying_preposition": null,
      "case_triggered": null,
      "transitiveness": null
    }
  ],
  "should_learn": true,
  "has_error": false,
  "error_description": null
}

Example 5 - Preposition with common usage:
{
  "lemma": "sobre",
  "definitions": [
    {
      "definition": "on, about",
      "gloss": "on",
      "part_of_speech": "preposition",
      "gender": null,
      "verb_group": null,
      "accompanying_preposition": null,
      "case_triggered": "accusative",
      "transitiveness": null
    }
  ],
  "should_learn": true,
  "has_error": false,
  "error_description": null
}

Example 6 - Non-integrated English word (should_learn: false):
{
  "lemma": "marketing",
  "definitions": [
    {
      "definition": "marketing (English business term)",
      "gloss": "marketing",
      "part_of_speech": "noun",
      "gender": "masculine",
      "verb_group": null,
      "accompanying_preposition": null,
      "case_triggered": null,
      "transitiveness": null
    }
  ],
  "should_learn": false,
  "has_error": false,
  "error_description": null
}

Example 7 - Place name (should_learn: false):
{
  "lemma": "madeira",
  "definitions": [
    {
      "definition": "Madeira (Portuguese island)",
      "gloss": "Madeira",
      "part_of_speech": "noun",
      "gender": "feminine",
      "verb_group": null,
      "accompanying_preposition": null,
      "case_triggered": null,
      "transitiveness": null
    }
  ],
  "should_learn": false,
  "has_error": false,
  "error_description": null
}

Example 8 - Integrated loanword (should_learn: true):
{
  "lemma": "fútbol",
  "definitions": [
    {
      "definition": "soccer, football",
      "gloss": "soccer",
      "part_of_speech": "noun",
      "gender": "masculine",
      "verb_group": null,
      "accompanying_preposition": null,
      "case_triggered": null,
      "transitiveness": null
    }
  ],
  "should_learn": true,
  "has_error": false,
  "error_description": null
}

Example 9 - Stem changing verb (should_learn: true):
{
  "lemma": "dormir",
  "definitions": [
    {
      "definition": "to sleep",
      "gloss": "sleep",
      "part_of_speech": "verb",
      "gender": null,
      "verb_group": "3rd conjugation (-ir) (stem changing)",
      "accompanying_preposition": null,
      "case_triggered": null,
      "transitiveness": "intransitive"
    }
  ],
  "should_learn": true,
  "has_error": false,
  "error_description": null
}


FIELD VALUE SPECIFICATIONS (use EXACTLY these values):

part_of_speech - MUST be one of:
- "noun"
- "verb" 
- "adjective"
- "adverb"
- "preposition"
- "conjunction"
- "pronoun"
- "determiner"
- "interjection"
- "numeral"

gender - MUST be one of:
- "masculine" (for masculine nouns/adjectives)
- "feminine" (for feminine nouns/adjectives)
- "both" (for adjectives that don't change form)
- null (for non-gendered words like verbs, prepositions, etc.)

verb_group - MUST be one of:
- "1st conjugation (-ar)"
- "2nd conjugation (-er)"
- "3rd conjugation (-ir)"
- "1st conjugation (-ar) (stem changing)"
- "2nd conjugation (-er) (stem changing)"
- "3rd conjugation (-ir) (stem changing)"
- "irregular" (for verbs with more irregularities than stem changing)
- null (for non-verbs)

transitiveness - MUST be one of:
- "transitive" (takes direct object)
- "intransitive" (no direct object)
- "both" (can be used both ways)
- "reflexive" (primarily reflexive usage)
- "impersonal" (impersonal verbs like llover)
- null (for non-verbs)

case_triggered - MUST be one of:
- "accusative" (direct object case)
- "dative" (indirect object case)
- "genitive" (possessive case)
- "ablative" (instrumental/locative case)
- null (for words that don't trigger case)

should_learn - MUST be exactly:
- true (boolean, not string)
- false (boolean, not string)

has_error - MUST be exactly:
- true (boolean, not string)
- false (boolean, not string)

CLASSIFICATION RULES FOR "should_learn":
- TRUE for: 
  * Core Spanish vocabulary (common verbs/nouns/adjectives)
  * Useful cognates that help with learning
  * Common abbreviations used in Spanish
  * Words borrowed from other languages that are now used like Spanish words by native speakers (e.g., "fútbol", "champú", "estrés")
  * Country names (España, Francia, Alemania, etc.)
  * City or region names that differ significantly between languages and are relevant to Spanish learning or are very very common
- FALSE for: 
  * Proper nouns identical between languages (Madrid, Barcelona, etc.)
  * Brand names (Nike, Apple, McDonald's, etc.)
  * Uncommon abbreviations
  * Numbers and symbols
  * Foreign words that are mostly used in quotations, code-switching, or non-Spanish contexts
  * English words that appear in Spanish text but are not integrated into Spanish and have no meaning changes from English/the foreign language (like "marketing", "email", "software")
  * City or region names that are identical or very similar between languages and are not relevant to Spanish learning


ERROR DETECTION RULES FOR "has_error":
- TRUE for: Lemmatization errors, non-sensical entries, uncertain or unclear definitions
- FALSE for: Valid Spanish words with clear definitions

FORMATTING REQUIREMENTS:
- Keep definitions concise and learner-friendly
- Use null (not empty string "") for non-applicable fields
- Use exact values from the specifications above
- Ensure JSON is properly formatted with correct boolean types
- Focus on the most common/useful meanings for learners

CRITICAL: Return ONLY the JSON response with no additional text, explanations, or markdown formatting.

Return the response in this exact JSON format:
{"lemmas": [
    {
        "lemma": "word",
        "definitions": [
            {
                "definition": "concise, learner-friendly definition or direct English translation",
                "gloss": "single English word translation",
                "part_of_speech": "one of the specified values above",
                "gender": "masculine/feminine/both/null",
                "verb_group": "one of the specified values above",
                "accompanying_preposition": "preposition string or null",
                "case_triggered": "accusative/dative/genitive/ablative/null",
                "transitiveness": "transitive/intransitive/both/reflexive/impersonal/null"
            }
        ],
        "should_learn": true,
        "has_error": false,
        "error_description": null
    }
]}"""

def create_variable_prompt_content(lemmas: List[str]) -> str:
    """
    Create the variable part of the prompt that contains the specific lemmas to analyze.
    This part is not cached since it changes with each request.
    """
    lemma_count = len(lemmas)
    lemma_list = ', '.join(lemmas)
    
    return f"""

TASK: Analyze these {lemma_count} Spanish lemmas: {lemma_list}

CRITICAL REQUIREMENTS:
1. Provide definitions for EXACTLY these {lemma_count} lemmas and NO OTHERS
2. Do NOT add extra lemmas, examples, or additional words
3. Use the EXACT lemma spelling as provided - do not modify in any way
4. Return exactly {lemma_count} lemma entries, one for each requested lemma"""

@dataclass
class Definition:
    definition: str
    gloss: str  # Single English word that best covers the meaning
    part_of_speech: str
    gender: Optional[str] = None
    verb_group: Optional[str] = None
    accompanying_preposition: Optional[str] = None
    case_triggered: Optional[str] = None
    transitiveness: Optional[str] = None

@dataclass
class LemmaInfo:
    lemma: str
    definitions: List[Definition]
    should_learn: bool
    has_error: bool
    error_description: Optional[str] = None

def create_definition_prompt(lemmas: List[str]) -> str:
    """
    Create a learner-focused prompt for definition generation.
    Combines static content with variable lemma list.
    """
    return STATIC_PROMPT_CONTENT + create_variable_prompt_content(lemmas)

def get_static_instructions_hash() -> str:
    """
    Generate a hash of the static instruction portion of the prompt.
    This is used for cache key generation.
    """
    return hashlib.md5(STATIC_PROMPT_CONTENT.encode()).hexdigest()

def create_definition_prompt_for_anthropic(lemmas: List[str]) -> tuple[list, list]:
    """
    Create a prompt structure optimized for Anthropic's prompt caching.
    Returns (system_messages, user_messages) where system can be cached.
    """
    # Static system instructions that can be cached
    system_messages = [
        {
            "type": "text",
            "text": STATIC_PROMPT_CONTENT,
            "cache_control": {"type": "ephemeral"}  # Enable Anthropic caching
        }
    ]
    
    # Variable user message (not cached)
    variable_content = create_variable_prompt_content(lemmas)
    user_messages = [
        {
            "role": "user",
            "content": variable_content.strip()
        }
    ]
    
    return system_messages, user_messages

def create_definition_prompt_for_openai(lemmas: List[str]) -> str:
    """
    Create a prompt optimized for OpenAI's automatic prompt caching.
    Places static instructions at the beginning (1024+ tokens for caching).
    """
    variable_content = create_variable_prompt_content(lemmas)
    
    # For OpenAI, we need to format the JSON template with proper escaping
    openai_static_content = STATIC_PROMPT_CONTENT.replace("{", "{{").replace("}", "}}")
    
    return openai_static_content + variable_content

class LLMProvider(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def generate_definitions(self, model: str, lemmas: List[str], batch_size: int) -> List[LemmaInfo]:
        pass

    def _parse_response(self, response: str, original_lemmas: List[str]) -> List[LemmaInfo]:
        """Unified response parsing for all providers with validation."""
        try:
            # Handle JSON wrapped in markdown code blocks
            response_text = response.strip()
            
            # First, try to find JSON in markdown code blocks
            if '```json' in response_text:
                # Extract JSON from markdown code block
                start_idx = response_text.find('```json') + 7  # Skip past ```json
                end_idx = response_text.find('```', start_idx)
                if start_idx != -1 and end_idx != -1:
                    response_text = response_text[start_idx:end_idx].strip()
            elif '```' in response_text:
                # Handle generic code blocks
                start_idx = response_text.find('```')
                end_idx = response_text.find('```', start_idx + 3)
                if start_idx != -1 and end_idx != -1:
                    response_text = response_text[start_idx + 3:end_idx].strip()
            
            # If no code blocks, look for JSON structure in the text
            if not response_text.startswith('{'):
                # Find the first opening brace
                start_idx = response_text.find('{')
                if start_idx != -1:
                    # Find the matching closing brace by counting braces
                    brace_count = 0
                    end_idx = start_idx
                    for i in range(start_idx, len(response_text)):
                        if response_text[i] == '{':
                            brace_count += 1
                        elif response_text[i] == '}':
                            brace_count -= 1
                            if brace_count == 0:
                                end_idx = i + 1
                                break
                    
                    if end_idx > start_idx:
                        response_text = response_text[start_idx:end_idx]
            
            data = json.loads(response_text)
            parsed_results = [
                LemmaInfo(
                    lemma=item['lemma'],
                    definitions=[
                        Definition(**def_dict)
                        for def_dict in item['definitions']
                    ],
                    should_learn=item['should_learn'],
                    has_error=item['has_error'],
                    error_description=item.get('error_description')
                )
                for item in data['lemmas']
            ]
            
            # Validate that we got exactly the right lemmas
            validation_error = self._validate_lemma_response(parsed_results, original_lemmas)
            if validation_error:
                logger.warning(f"Validation failed: {validation_error}")
                logger.warning(f"Expected lemmas: {original_lemmas}")
                logger.warning(f"Received lemmas: {[r.lemma for r in parsed_results]}")
                # Return validation error instead of the parsed results
                raise ValueError(validation_error)
            
            return parsed_results
            
        except Exception as e:
            logger.error(f"Error parsing response: {str(e)}")
            logger.error(f"Response content: {response[:500]}...")
            return [
                LemmaInfo(
                    lemma=lemma,
                    definitions=[],
                    should_learn=False,
                    has_error=True,
                    error_description="Failed to parse LLM response"
                ) for lemma in original_lemmas
            ]

    def _validate_lemma_response(self, parsed_results: List[LemmaInfo], expected_lemmas: List[str]) -> Optional[str]:
        """
        Validate that the parsed response contains exactly the expected lemmas.
        Returns error message if validation fails, None if validation passes.
        """
        if len(parsed_results) != len(expected_lemmas):
            return f"Expected {len(expected_lemmas)} lemmas, got {len(parsed_results)}"
        
        received_lemmas = [r.lemma for r in parsed_results]
        expected_set = set(expected_lemmas)
        received_set = set(received_lemmas)
        
        if expected_set != received_set:
            missing = expected_set - received_set
            extra = received_set - expected_set
            error_parts = []
            if missing:
                error_parts.append(f"Missing lemmas: {list(missing)}")
            if extra:
                error_parts.append(f"Extra lemmas: {list(extra)}")
            return "; ".join(error_parts)
        
        return None  # Validation passed

    def _generate_with_retry(self, lemmas: List[str], max_retries: int = 2) -> List[LemmaInfo]:
        """
        Generate definitions with retry logic for validation failures.
        This method should be implemented by subclasses.
        """
        raise NotImplementedError("Subclasses must implement _generate_with_retry")

class AnthropicProvider(LLMProvider):
    def __init__(self, api_key: Optional[str] = None):
        super().__init__()
        self.client = anthropic.Anthropic(api_key=api_key or os.getenv('ANTHROPIC_API_KEY'))
        
    def generate_definitions(self, model:str, lemmas: List[str], batch_size: int = 5) -> List[LemmaInfo]:
        results = []
        
        for i in range(0, len(lemmas), batch_size):
            batch = lemmas[i:i + batch_size]
            logger.info(f"Processing batch: {batch}")
            batch_results = self._generate_with_retry(model, batch)
            results.extend(batch_results)
            
            time.sleep(1)  # Rate limiting
            
        return results

    def _generate_with_retry(self, model:str, lemmas: List[str], max_retries: int = 2) -> List[LemmaInfo]:
        """Generate definitions with retry logic."""
        for attempt in range(max_retries + 1):
            try:
                logger.info(f"Generating definitions for {lemmas} (attempt {attempt + 1})")
                
                # Create prompt with caching support
                system_messages, user_messages = create_definition_prompt_for_anthropic(lemmas)
                
                response = self.client.messages.create(
                    model=model,
                    system=system_messages,
                    messages=user_messages,
                    temperature=0.1
                )
                
                response_text = response.content[0].text
                logger.debug(f"Raw response: {response_text}")
                
                # Parse and validate response using base class method
                parsed_results = self._parse_response(response_text, lemmas)
                logger.info(f"Successfully generated {len(parsed_results)} definitions")
                return parsed_results
                
            except Exception as e:
                logger.warning(f"Attempt {attempt + 1} failed: {str(e)}")
                if attempt == max_retries:
                    logger.error(f"All {max_retries + 1} attempts failed for batch: {lemmas}")
                    # Return error entries for all lemmas
                    return [
                        LemmaInfo(
                            lemma=lemma,
                            definitions=[],
                            should_learn=True,
                            has_error=True,
                            error_description=f"Failed to generate definition after {max_retries + 1} attempts: {str(e)}"
                        ) for lemma in lemmas
                    ]
                time.sleep(2 ** attempt)  # Exponential backoff

class OpenAIProvider(LLMProvider):
    def __init__(self, api_key: Optional[str] = None):
        super().__init__()
        self.client = OpenAI(api_key=api_key or os.getenv('OPENAI_API_KEY'))
        
    def generate_definitions(self, model:str, lemmas: List[str], batch_size: int = 5) -> List[LemmaInfo]:
        results = []
        
        for i in range(0, len(lemmas), batch_size):
            batch = lemmas[i:i + batch_size]
            logger.info(f"Processing batch: {batch}")
            batch_results = self._generate_with_retry(model, batch)
            results.extend(batch_results)
            
            time.sleep(1)  # Rate limiting
            
        return results

    def _generate_with_retry(self, model:str, lemmas: List[str], max_retries: int = 2) -> List[LemmaInfo]:
        """Generate definitions with retry logic and OpenAI automatic caching."""
        for attempt in range(max_retries + 1):
            try:
                logger.info(f"Generating definitions for batch: {lemmas} (attempt {attempt + 1})")
                
                # Use OpenAI-specific prompt optimized for automatic caching
                prompt = create_definition_prompt_for_openai(lemmas)
                
                # Make API call - OpenAI will automatically cache if prompt is 1024+ tokens
                response = self.client.chat.completions.create(
                    model=model,
                    messages=[{
                        "role": "user", 
                        "content": prompt
                    }],
                    temperature=0.1
                )
                
                response_text = response.choices[0].message.content
                logger.debug(f"Raw response: {response_text}")
                
                # Parse and validate response using base class method
                parsed_results = self._parse_response(response_text, lemmas)
                logger.info(f"Successfully generated {len(parsed_results)} definitions")
                return parsed_results
                
            except Exception as e:
                logger.warning(f"Attempt {attempt + 1} failed: {str(e)}")
                if attempt == max_retries:
                    logger.error(f"All {max_retries + 1} attempts failed for batch: {lemmas}")
                    # Return error entries for all lemmas
                    return [
                        LemmaInfo(
                            lemma=lemma,
                            definitions=[],
                            should_learn=True,
                            has_error=True,
                            error_description=f"Failed to generate definition after {max_retries + 1} attempts: {str(e)}"
                        ) for lemma in lemmas
                    ]
                time.sleep(2 ** attempt)  # Exponential backoff

def process_lemma_file(
    input_file: str,
    output_file: str,
    provider: LLMProvider,
    model: str,
    batch_size: int = 5,
    limit: Optional[int] = 100,
    start: Optional[int] = 0
) -> None:
    """
    Process a JSON file containing lemmas and generate definitions using the specified LLM provider.
    
    Args:
        input_file: Path to the input JSON file containing lemmas and frequencies
        output_file: Path to save the output JSON file with definitions
        provider: LLM provider instance to use for generating definitions
        batch_size: Number of lemmas to process in each batch
        limit: Optional maximum number of lemmas to process
    """
    logger.info(f"Processing lemma file: {input_file}")
    
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    lemmas = list(data.keys())
    if limit:
        logger.info(f"Retrieving {limit} lemmas starting at index {start}: {start} - {start + limit}")
        lemmas = lemmas[start:start + limit]
    
    results = provider.generate_definitions(model, lemmas, batch_size)
    
    # Merge results with original frequency data
    output_data = {}
    for lemma_info in results:
        output_data[lemma_info.lemma] = {
            "frequency": data[lemma_info.lemma],
            "definitions": [vars(def_) for def_ in lemma_info.definitions],
            "should_learn": lemma_info.should_learn,
            "has_error": lemma_info.has_error,
            "error_description": lemma_info.error_description
        }

    header = {
        "model": model,
        "batch_size": batch_size,
        "limit": limit,
        "start": start,
        "timestamp": datetime.now().strftime("%Y%m%d_%H%M%S")
    }

    full_output_data = {
        "header": header,
        "lemmas": output_data
    }
    
    output_dir = os.path.dirname(output_file)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(full_output_data, f, ensure_ascii=False, indent=2)
    
    logger.info(f"Results saved to: {output_file}")

def main():
    import argparse
    
    # Model configurations
    MODEL_OPTIONS = {
        "gpt-4.1-mini": {"provider": "openai", "model_id": "gpt-4.1-mini-2025-04-14"},
        "gpt-4.1-nano": {"provider": "openai", "model_id": "gpt-4.1-nano-2025-04-14"},
        "gpt-4o-mini": {"provider": "openai", "model_id": "gpt-4o-mini-2024-07-18"},
        "claude-3.5-haiku": {"provider": "anthropic", "model_id": "claude-3-5-haiku-20241022"},
        "claude-3-haiku": {"provider": "anthropic", "model_id": "claude-3-haiku-20240307"}
    }
    
    parser = argparse.ArgumentParser(description="Generate definitions for lemmas using LLM APIs")
    parser.add_argument("input_file", help="Path to input JSON file containing lemmas")
    parser.add_argument(
        "output_file", 
        default=f"definitions_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
        help="Path to save output JSON file with definitions"
    )
    parser.add_argument(
        "--model",
        choices=list(MODEL_OPTIONS.keys()),
        default="claude-3-haiku",
        help="Model to use for generating definitions"
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=5,
        help="Number of lemmas to process in each batch"
    )
    parser.add_argument(
        "--limit",
        type=int,
        help="Maximum number of lemmas to process"
    )
    parser.add_argument(
        "--start",
        type=int,
        default=0,
        help="Starting index for processing lemmas"
    )
    
    args = parser.parse_args()
    
    # Determine provider from model selection
    if args.model:
        model_config = MODEL_OPTIONS[args.model]
        provider_type = model_config["provider"]
    else:
        raise ValueError("Model not specified")
    
    provider_class = AnthropicProvider if provider_type == "anthropic" else OpenAIProvider
    provider = provider_class()
    
    process_lemma_file(
        args.input_file,
        args.output_file,
        provider,
        args.model,
        args.batch_size,
        args.limit,
        args.start
    )

if __name__ == "__main__":
    main() 