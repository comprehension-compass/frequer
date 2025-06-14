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
import re

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# LLM Pricing (per 1M tokens)
LLM_PRICING = {
    # OpenAI Models (full model names)
    "gpt-4.1-mini-2025-04-14": {
        "provider": "openai", 
        "input": 0.40,
        "cached_input": 0.10,
        "output": 1.60,
        "cache_writes": 0.00  # Free
    },
    "gpt-4.1-nano-2025-04-14": {
        "provider": "openai",
        "input": 0.10,
        "cached_input": 0.025,
        "output": 0.40,
        "cache_writes": 0.00  # Free
    },
    "gpt-4o-mini-2024-07-18": {
        "provider": "openai",
        "input": 0.15,
        "cached_input": 0.075,
        "output": 0.60,
        "cache_writes": 0.00  # Free
    },
    "o4-mini-2025-04-16": {
        "provider": "openai",
        "input": 1.10,
        "cached_input": 0.275,
        "output": 4.40,
        "cache_writes": 0.00  # Free
    },
    "o3-2025-04-16": {
        "provider": "openai",
        "input": 2.00,
        "cached_input": 0.50,
        "output": 8.00,
        "cache_writes": 0.00  # Free
    },
    
    # Anthropic Models (using 5m cache writes pricing)
    "claude-sonnet-4-20250514": {
        "provider": "anthropic",
        "input": 3.00,
        "cached_input": 0.30,  # Cache hits
        "output": 15.00,
        "cache_writes": 3.75  # 5m cache writes
    },
    "claude-3-5-haiku-20241022": {
        "provider": "anthropic",
        "input": 0.80,
        "cached_input": 0.08,  # Cache hits
        "output": 4.00,
        "cache_writes": 1.00  # 5m cache writes
    },
    "claude-3-haiku-20240307": {
        "provider": "anthropic",
        "input": 0.25,
        "cached_input": 0.03,  # Cache hits
        "output": 1.25,
        "cache_writes": 0.30  # 5m cache writes
    }
}

# Anthropic model max_tokens mapping
ANTHROPIC_MAX_TOKENS = {
    "claude-sonnet-4-20250514": 64000,
    "claude-3-5-haiku-20241022": 8192,
    "claude-3-haiku-20240307": 4096,
}

@dataclass
class TokenUsage:
    """Track token usage for API calls"""
    read_cached_input_tokens: int = 0
    written_cached_input_tokens: int = 0
    uncached_input_tokens: int = 0
    output_tokens: int = 0
    
    def add_anthropic_usage(self, usage_data):
        """Add Anthropic token usage from API response"""
        if hasattr(usage_data, 'cache_read_input_tokens'):
            self.read_cached_input_tokens += usage_data.cache_read_input_tokens or 0
        if hasattr(usage_data, 'cache_creation_input_tokens'):
            self.written_cached_input_tokens += usage_data.cache_creation_input_tokens or 0
        if hasattr(usage_data, 'input_tokens'):
            # For Anthropic, input_tokens already represents uncached input tokens
            self.uncached_input_tokens += usage_data.input_tokens or 0
        if hasattr(usage_data, 'output_tokens'):
            self.output_tokens += usage_data.output_tokens or 0
    
    def add_openai_usage(self, usage_data):
        """Add OpenAI token usage from API response"""
        # OpenAI doesn't charge for cache writes, so always 0
        self.written_cached_input_tokens += 0
        
        # Get cached tokens from prompt_tokens_details
        cached_tokens = 0
        if hasattr(usage_data, 'prompt_tokens_details') and hasattr(usage_data.prompt_tokens_details, 'cached_tokens'):
            cached_tokens = usage_data.prompt_tokens_details.cached_tokens or 0
            self.read_cached_input_tokens += cached_tokens
        
        # Calculate uncached input tokens: total prompt tokens - cached tokens
        total_prompt_tokens = usage_data.prompt_tokens or 0
        self.uncached_input_tokens += max(0, total_prompt_tokens - cached_tokens)
        
        if hasattr(usage_data, 'completion_tokens'):
            self.output_tokens += usage_data.completion_tokens or 0
    
    def calculate_cost(self, model_name: str) -> Dict[str, float]:
        """Calculate cost breakdown based on token usage and model pricing"""
        if model_name not in LLM_PRICING:
            return {
                "uncached_input_cost": 0.0,
                "cached_input_cost": 0.0,
                "cache_write_cost": 0.0,
                "output_cost": 0.0,
                "total_cost": 0.0,
                "error": f"Pricing not found for model: {model_name}"
            }
        
        pricing = LLM_PRICING[model_name]
        
        # Convert tokens to millions for pricing calculation
        uncached_input_cost = (self.uncached_input_tokens / 1_000_000) * pricing["input"]
        cached_input_cost = (self.read_cached_input_tokens / 1_000_000) * pricing["cached_input"]
        cache_write_cost = (self.written_cached_input_tokens / 1_000_000) * pricing["cache_writes"]
        output_cost = (self.output_tokens / 1_000_000) * pricing["output"]
        
        total_cost = uncached_input_cost + cached_input_cost + cache_write_cost + output_cost
        
        return {
            "uncached_input_cost": round(uncached_input_cost, 6),
            "cached_input_cost": round(cached_input_cost, 6),
            "cache_write_cost": round(cache_write_cost, 6),
            "output_cost": round(output_cost, 6),
            "total_cost": round(total_cost, 6)
        }

# STATIC PROMPT CONTENT - DEFINED ONCE
STATIC_PROMPT_CONTENT = """You are a Spanish language expert creating concise, English-speaking language learner-focused definitions for Spanish lemmas.

EXTREMELY IMPORTANT - LEMMA FIELD REQUIREMENTS:
- The "lemma" field in your response MUST be EXACTLY the same as provided in the word list
- Do NOT translate, modify, capitalize, or change the lemma in any way
- Do NOT add accents, remove accents, or alter the spelling in ANY way
- CRITICAL: Preserve ALL accents exactly (ó, é, í, á, ú, ü, ñ, etc.)
- Copy each lemma EXACTLY character-by-character as written in the provided list
- Example: If given "estación", respond with "estación" - NOT "estacion"
- Example: If given "mamá", respond with "mamá" - NOT "mama"
- ANY modification to the lemma will cause processing errors

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
- CRITICAL: Always verify that the conjugation group assigned is correct

GRAMMATICAL METADATA ACCURACY:
- Gender: Only assign to nouns and adjectives that actually have gender, the gender should match the original lemma, not the gender of the word in the example sentence
- Verb group: Only assign to verbs, and ensure the group matches the original lemma
- Transitiveness: Verify if verbs actually take direct objects - be precise about transitive/intransitive
- Part of speech: Be precise - distinguish between adjectives and nouns or adverbs and adjectives carefully
- MULTIPLE MEANINGS: If a word has multiple important meanings or parts of speech, provide separate definitions
- Prepositions: Identify and include all preposition patterns that are relevant for learners

INSTRUCTIONS:
Create definitions that are helpful for Spanish language learners. Prioritize clarity and conciseness over comprehensive dictionary-style explanations.

COMPREHENSIVE COVERAGE REQUIREMENTS:
- ALWAYS check if a word has multiple important meanings or parts of speech
- Provide separate definitions for each significant meaning (e.g., "trabajador" as noun AND adjective)
- Include secondary meanings that are common and educationally valuable
- Don't limit yourself to just the most common meaning if others are important

DEFINITION GUIDELINES:
- If there's a direct English translation that covers the meaning well, use that as the definition
- Only provide longer explanations when there's no direct one-to-one translation
- Avoid overly academic or verbose language
- Include context only when valuable to a time-limited learner

GLOSS GUIDELINES:
- Provide the single most common English word that best translates the Spanish word
- Choose the most frequent/useful translation for learners
- If multiple meanings exist, choose the most common one for the gloss

EXAMPLE SENTENCE GUIDELINES:
- Create a short, natural Spanish sentence that demonstrates the word's meaning clearly
- Use only words that are more common than the target word, or of similar frequency if necessary
- Make the meaning obvious from context where possible
- Format as an Anki cloze deletion: {{c1:target_word_form}} - use EXACTLY this format, no extra braces
- The cloze can contain any inflected form of the lemma (conjugated verbs, plural nouns, etc.)
- CRITICAL: Ensure the word form in the example matches the part of speech being defined
- Keep sentences concise (ideally 5-10 words)
- Avoid complex grammar or rare vocabulary
- The sentence should be immediately understandable to intermediate Spanish learners
- When a word commonly requires a specific preposition, include that preposition in the example sentence to show the pattern
- Provide a natural English translation of the example sentence that maintains the same meaning and context
- Ensure the example sentence is natural Spanish as would be spoken by a native speaker

EXAMPLES:

Example 1 - Direct translation available:
{
  "lemma": "gato",
  "definitions": [
    {
      "definition": "cat",
      "gloss": "cat",
      "part_of_speech": "noun",
      "example_sentence": "Mi {{c1:gato}} duerme en la cama.",
      "example_translation": "My cat sleeps on the bed.",
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

Example 2 - Multiple meanings, comprehensive coverage:
{
  "lemma": "trabajador",
  "definitions": [
    {
      "definition": "worker, employee",
      "gloss": "worker",
      "part_of_speech": "noun",
      "example_sentence": "El {{c1:trabajador}} llegó temprano.",
      "example_translation": "The worker arrived early.",
      "gender": "masculine",
      "verb_group": null,
      "accompanying_preposition": null,
      "case_triggered": null,
      "transitiveness": null
    },
    {
      "definition": "hardworking, diligent",
      "gloss": "hardworking",
      "part_of_speech": "adjective",
      "example_sentence": "Es una persona muy {{c1:trabajadora}}.",
      "example_translation": "She is a very hardworking person.",
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

Example 3 - Verb with correct conjugation and preposition:
{
  "lemma": "responder",
  "definitions": [
    {
      "definition": "to respond, answer",
      "gloss": "respond",
      "part_of_speech": "verb",
      "example_sentence": "Voy a {{c1:responder}} a tu pregunta.",
      "example_translation": "I'm going to respond to your question.",
      "gender": null,
      "verb_group": "2nd conjugation (-er)",
      "accompanying_preposition": "a",
      "case_triggered": null,
      "transitiveness": "intransitive"
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
      "example_sentence": "La {{c1:sobremesa}} duró dos horas.",
      "example_translation": "The after-dinner conversation lasted two hours.",
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
      "example_sentence": "El libro está {{c1:sobre}} la mesa.",
      "example_translation": "The book is on the table.",
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
      "example_sentence": "La empresa usa {{c1:marketing}} digital.",
      "example_translation": "The company uses digital marketing.",
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
      "example_sentence": "Visitamos {{c1:Madeira}} el año pasado.",
      "example_translation": "We visited Madeira last year.",
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

Example 8 - Adjective with proper gender specification:
{
  "lemma": "mínimo",
  "definitions": [
    {
      "definition": "minimum, minimal",
      "gloss": "minimum",
      "part_of_speech": "adjective",
      "example_sentence": "Necesitas el tiempo {{c1:mínimo}} posible.",
      "example_translation": "You need the minimum time possible.",
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
      "example_sentence": "Los niños {{c1:duermen}} temprano.",
      "example_translation": "The children sleep early.",
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

Example 10 - Noun with multiple definitions and different preposition patterns (should_learn: true):
{
  "lemma": "derecho",
  "definitions": [
    {
      "definition": "right (entitlement)",
      "gloss": "right",
      "part_of_speech": "noun",
      "example_sentence": "Todos tienen {{c1:derecho}} a la educación.",
      "example_translation": "Everyone has the right to education.",
      "gender": "masculine",
      "verb_group": null,
      "accompanying_preposition": "a",
      "case_triggered": null,
      "transitiveness": null
    },
    {
      "definition": "law (legal system)",
      "gloss": "law",
      "part_of_speech": "noun",
      "example_sentence": "Estudia {{c1:derecho}} en la universidad.",
      "example_translation": "He studies law at the university.",
      "gender": "masculine",
      "verb_group": null,
      "accompanying_preposition": null,
      "case_triggered": null,
      "transitiveness": null
    },
    {
      "definition": "straight ahead",
      "gloss": "straight",
      "part_of_speech": "adverb",
      "example_sentence": "Sigue {{c1:derecho}} hasta el semáforo.",
      "example_translation": "Go straight until the traffic light.",
      "gender": null,
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

Example 11 - Comprehensive coverage of multiple meanings:
{
  "lemma": "navegador",
  "definitions": [
    {
      "definition": "web browser",
      "gloss": "browser",
      "part_of_speech": "noun",
      "example_sentence": "Abre el {{c1:navegador}} para buscar información.",
      "example_translation": "Open the browser to search for information.",
      "gender": "masculine",
      "verb_group": null,
      "accompanying_preposition": null,
      "case_triggered": null,
      "transitiveness": null
    },
    {
      "definition": "navigator (person who navigates)",
      "gloss": "navigator",
      "part_of_speech": "noun",
      "example_sentence": "El {{c1:navegador}} guió el barco al puerto.",
      "example_translation": "The navigator guided the ship to port.",
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

accompanying_preposition - Should contain:
- The specific preposition that commonly follows the word (e.g., "a", "de", "en", "por", "con", "para", "desde", "hasta", "sobre", "bajo", "contra", "hacia", "ante", "tras", etc.)
- null (for words that don't commonly require a specific preposition)
- Examples for NOUNS: "derecho a", "miedo de/a", "interés en/por", "capacidad de/para", "problema con", "confianza en", "preocupación por", "lucha contra", "camino hacia"
- Examples for VERBS: "pensar en", "soñar con", "depender de", "consistir en", "preocuparse por", "enamorarse de", "tratar de", "dejar de", "empezar a", "invitar a"

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
- CRITICAL: Use proper JSON formatting - no trailing commas, proper quotes, valid structure

JSON OUTPUT REQUIREMENTS:
- Return ONLY valid JSON with no additional text, explanations, or markdown formatting
- Do NOT wrap in code blocks or add any commentary
- Ensure all quotes are properly escaped
- Verify JSON structure is complete and valid before responding

Return the response in this exact JSON format:
{"lemmas": [
    {
        "lemma": "word",
        "definitions": [
            {
                "definition": "concise, learner-friendly definition or direct English translation",
                "gloss": "single English word translation",
                "part_of_speech": "one of the specified values above",
                "example_sentence": "Short Spanish sentence with {{c1:word_form}} cloze deletion",
                "example_translation": "Natural English translation of the example sentence",
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
    example_sentence: str  # Anki cloze sentence with {{c1: word}} format
    example_translation: str  # English translation of the example sentence
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

def normalize_cloze_format(text: str) -> str:
    """
    Normalize cloze deletion format to always be {{c1:word}}.
    Handles cases with 1, 3, 4, 5, or 6 braces and converts them to exactly 2.
    
    Examples:
    - {c1:word} -> {{c1:word}}
    - {{{c1:word}}} -> {{c1:word}}
    - {{{{c1:word}}}} -> {{c1:word}}
    - {{{{{c1:word}}}}} -> {{c1:word}}
    - {{{{{{c1:word}}}}}} -> {{c1:word}}
    """
    if not text:
        return text
    
    # Pattern to match cloze deletions with varying numbers of braces
    # This matches: 1-6 opening braces, c1:, content, 1-6 closing braces
    pattern = r'\{+c1:([^}]+)\}+'
    
    def replace_cloze(match):
        # Extract the content between c1: and the closing braces
        content = match.group(1)
        # Return normalized format with exactly 2 braces
        return f"{{{{c1:{content}}}}}"
    
    # Replace all cloze deletions with normalized format
    normalized = re.sub(pattern, replace_cloze, text)
    
    return normalized

def create_definition_prompt(lemmas: List[str]) -> str:
    """
    Create a learner-focused prompt for definition generation.
    Combines static content with variable lemma list.
    """
    return STATIC_PROMPT_CONTENT + create_variable_prompt_content(lemmas)


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
        self.token_usage = TokenUsage()

    @abstractmethod
    def generate_definitions(self, model: str, lemmas: List[str], batch_size: int) -> List[LemmaInfo]:
        """Generate definitions for a list of lemmas."""
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
            parsed_results = []
            
            for item in data['lemmas']:
                # Process definitions and normalize cloze format
                normalized_definitions = []
                for def_dict in item['definitions']:
                    # Create a copy of the definition dict
                    normalized_def_dict = def_dict.copy()
                    # Normalize the example sentence cloze format
                    if 'example_sentence' in normalized_def_dict:
                        original_sentence = normalized_def_dict['example_sentence']
                        normalized_sentence = normalize_cloze_format(original_sentence)
                        if original_sentence != normalized_sentence:
                            logger.debug(f"Normalized cloze: '{original_sentence}' -> '{normalized_sentence}'")
                        normalized_def_dict['example_sentence'] = normalized_sentence
                    normalized_definitions.append(Definition(**normalized_def_dict))
                
                parsed_results.append(LemmaInfo(
                    lemma=item['lemma'],
                    definitions=normalized_definitions,
                    should_learn=item['should_learn'],
                    has_error=item['has_error'],
                    error_description=item.get('error_description')
                ))
            
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
            # Re-raise the exception to trigger retry logic
            raise ValueError(f"Failed to parse LLM response: {str(e)}")

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

    def _generate_with_retry(self, lemmas: List[str], max_retries: int = 3) -> List[LemmaInfo]:
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

    def _generate_with_retry(self, model:str, lemmas: List[str], max_retries: int = 3) -> List[LemmaInfo]:
        """Generate definitions with retry logic."""
        for attempt in range(max_retries + 1):
            try:
                logger.info(f"Generating definitions for {lemmas} (attempt {attempt + 1})")
                
                # Create prompt with caching support
                system_messages, user_messages = create_definition_prompt_for_anthropic(lemmas)
                
                # Use streaming for Claude Sonnet 4 due to long processing times
                if model == "claude-sonnet-4-20250514":
                    logger.info("Using streaming for Claude Sonnet 4...")
                    
                    stream = self.client.messages.stream(
                        model=model,
                        max_tokens=ANTHROPIC_MAX_TOKENS.get(model, 4096),
                        system=system_messages,
                        messages=user_messages,
                        temperature=0.1
                    )
                    
                    response_text = ""
                    usage_data = None
                    
                    with stream as stream_context:
                        for event in stream_context:
                            if event.type == "content_block_delta":
                                response_text += event.delta.text
                            elif event.type == "message_stop":
                                # Get usage data from the final message
                                usage_data = stream_context.get_final_message().usage
                    
                    # Track token usage for streaming
                    if usage_data:
                        self.token_usage.add_anthropic_usage(usage_data)
                        logger.info(f"Token usage - Input: {usage_data.input_tokens}, Output: {usage_data.output_tokens}, "
                                  f"Cache Read: {getattr(usage_data, 'cache_read_input_tokens', 0)}, "
                                  f"Cache Creation: {getattr(usage_data, 'cache_creation_input_tokens', 0)}")
                    else:
                        logger.warning("No usage data found in Anthropic streaming response")
                
                else:
                    # Use regular (non-streaming) for other Anthropic models
                    response = self.client.messages.create(
                        model=model,
                        max_tokens=ANTHROPIC_MAX_TOKENS.get(model, 4096),
                        system=system_messages,
                        messages=user_messages,
                        temperature=0.1
                    )
                    
                    # Track token usage
                    if hasattr(response, 'usage'):
                        self.token_usage.add_anthropic_usage(response.usage)
                        logger.info(f"Token usage - Input: {response.usage.input_tokens}, Output: {response.usage.output_tokens}, "
                                  f"Cache Read: {getattr(response.usage, 'cache_read_input_tokens', 0)}, "
                                  f"Cache Creation: {getattr(response.usage, 'cache_creation_input_tokens', 0)}")
                    else:
                        logger.warning("No usage data found in Anthropic response: {response}")
                    
                    response_text = response.content[0].text
                
                logger.debug(f"Raw response: {response_text}")
                
                # Parse and validate response using base class method
                parsed_results = self._parse_response(response_text, lemmas)
                logger.info(f"Successfully generated {len(parsed_results)} definitions")
                return parsed_results
                
            except Exception as e:
                error_type = type(e).__name__
                error_msg = str(e)
                
                # Determine retry reason category
                if "json" in error_msg.lower() or "parse" in error_msg.lower():
                    retry_reason = "JSON_PARSING_ERROR"
                elif "validation" in error_msg.lower() or "missing lemmas" in error_msg.lower() or "extra lemmas" in error_msg.lower():
                    retry_reason = "VALIDATION_ERROR"
                elif "api" in error_msg.lower() or "rate" in error_msg.lower() or "quota" in error_msg.lower():
                    retry_reason = "API_ERROR"
                else:
                    retry_reason = "UNKNOWN_ERROR"
                
                logger.warning(f"ANTHROPIC RETRY {attempt + 1}/{max_retries + 1} - {retry_reason} for batch {lemmas}")
                logger.warning(f"Error details: {error_type}: {error_msg}")
                
                if attempt == max_retries:
                    logger.error(f"ANTHROPIC FINAL FAILURE after {max_retries + 1} attempts for batch: {lemmas}")
                    logger.error(f"Final error: {error_type}: {error_msg}")
                    # Return error entries for all lemmas
                    return [
                        LemmaInfo(
                            lemma=lemma,
                            definitions=[],
                            should_learn=True,
                            has_error=True,
                            error_description=f"Failed after {max_retries + 1} attempts. Final error: {retry_reason} - {error_msg}"
                        ) for lemma in lemmas
                    ]
                
                backoff_time = 2 ** attempt
                logger.info(f"Waiting {backoff_time}s before retry {attempt + 2}...")
                time.sleep(backoff_time)  # Exponential backoff

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

    def _generate_with_retry(self, model:str, lemmas: List[str], max_retries: int = 3) -> List[LemmaInfo]:
        """Generate definitions with retry logic and OpenAI automatic caching."""
        for attempt in range(max_retries + 1):
            try:
                logger.info(f"Generating definitions for batch: {lemmas} (attempt {attempt + 1})")
                
                # Use OpenAI-specific prompt optimized for automatic caching
                prompt = create_definition_prompt_for_openai(lemmas)
                
                # Make API call - OpenAI will automatically cache if prompt is 1024+ tokens
                # o4-mini only supports default temperature (1), other models can use 0.1
                api_params = {
                    "model": model,
                    "messages": [{
                        "role": "user", 
                        "content": prompt
                    }]
                }
                
                # Only set temperature for models that support it (not o4-mini or o3)
                if not model.startswith("o4-") and not model.startswith("o3-"):
                    api_params["temperature"] = 0.1
                
                response = self.client.chat.completions.create(**api_params)
                
                # Track token usage
                if hasattr(response, 'usage'):
                    self.token_usage.add_openai_usage(response.usage)
                    logger.info(f"Token usage - Prompt: {response.usage.prompt_tokens}, Completion: {response.usage.completion_tokens}, "
                              f"Cached: {getattr(response.usage.prompt_tokens_details, 'cached_tokens', 0) if hasattr(response.usage, 'prompt_tokens_details') else 0}")
                else:
                    logger.warning("No usage data found in OpenAI response: {response}")
                
                response_text = response.choices[0].message.content
                logger.debug(f"Raw response: {response_text}")
                
                # Parse and validate response using base class method
                parsed_results = self._parse_response(response_text, lemmas)
                logger.info(f"Successfully generated {len(parsed_results)} definitions")
                return parsed_results
                
            except Exception as e:
                error_type = type(e).__name__
                error_msg = str(e)
                
                # Determine retry reason category
                if "json" in error_msg.lower() or "parse" in error_msg.lower():
                    retry_reason = "JSON_PARSING_ERROR"
                elif "validation" in error_msg.lower() or "missing lemmas" in error_msg.lower() or "extra lemmas" in error_msg.lower():
                    retry_reason = "VALIDATION_ERROR"
                elif "api" in error_msg.lower() or "rate" in error_msg.lower() or "quota" in error_msg.lower():
                    retry_reason = "API_ERROR"
                else:
                    retry_reason = "UNKNOWN_ERROR"
                
                logger.warning(f"OPENAI RETRY {attempt + 1}/{max_retries + 1} - {retry_reason} for batch {lemmas}")
                logger.warning(f"Error details: {error_type}: {error_msg}")
                
                if attempt == max_retries:
                    logger.error(f"OPENAI FINAL FAILURE after {max_retries + 1} attempts for batch: {lemmas}")
                    logger.error(f"Final error: {error_type}: {error_msg}")
                    # Return error entries for all lemmas
                    return [
                        LemmaInfo(
                            lemma=lemma,
                            definitions=[],
                            should_learn=True,
                            has_error=True,
                            error_description=f"Failed after {max_retries + 1} attempts. Final error: {retry_reason} - {error_msg}"
                        ) for lemma in lemmas
                    ]
                
                backoff_time = 2 ** attempt
                logger.info(f"Waiting {backoff_time}s before retry {attempt + 2}...")
                time.sleep(backoff_time)  # Exponential backoff

def generate_definitions_for_lemmas(
    lemmas: List[str],
    provider: LLMProvider,
    model: str,
    batch_size: int = 5
) -> Dict[str, Any]:
    """
    Generate definitions for a list of lemmas using the specified LLM provider.
    Returns a dictionary with results and metadata.
    
    Args:
        lemmas: List of lemmas to process
        provider: LLM provider instance to use for generating definitions
        model: Model name to use for generating definitions
        batch_size: Number of lemmas to process in each batch
        
    Returns:
        Dictionary containing:
        - results: List of LemmaInfo objects
        - token_usage: TokenUsage object
        - cost_breakdown: Cost breakdown dictionary
        - metadata: Processing metadata
    """
    logger.info(f"Generating definitions for {len(lemmas)} lemmas using {model}")
    
    results = provider.generate_definitions(model, lemmas, batch_size)
    
    # Calculate costs
    cost_breakdown = provider.token_usage.calculate_cost(model)
    
    # Log token usage summary
    logger.info("=== TOKEN USAGE SUMMARY ===")
    logger.info(f"Read Cached: {provider.token_usage.read_cached_input_tokens}, "
               f"Written Cached: {provider.token_usage.written_cached_input_tokens}, "
               f"Uncached Input: {provider.token_usage.uncached_input_tokens}, "
               f"Output: {provider.token_usage.output_tokens}")
    
    # Log cost breakdown
    if "error" not in cost_breakdown:
        logger.info("=== COST BREAKDOWN ===")
        logger.info(f"Uncached Input: ${cost_breakdown['uncached_input_cost']:.6f}")
        logger.info(f"Cached Input: ${cost_breakdown['cached_input_cost']:.6f}")
        logger.info(f"Cache Writes: ${cost_breakdown['cache_write_cost']:.6f}")
        logger.info(f"Output: ${cost_breakdown['output_cost']:.6f}")
        logger.info(f"TOTAL COST: ${cost_breakdown['total_cost']:.6f}")
    else:
        logger.warning(f"Cost calculation error: {cost_breakdown['error']}")
    
    metadata = {
        "model": model,
        "num_lemmas": len(lemmas),
        "batch_size": batch_size,
        "timestamp": datetime.now().strftime("%Y%m%d_%H%M%S"),
        "token_usage": {
            "read_cached_input_tokens": provider.token_usage.read_cached_input_tokens,
            "written_cached_input_tokens": provider.token_usage.written_cached_input_tokens,
            "uncached_input_tokens": provider.token_usage.uncached_input_tokens,
            "output_tokens": provider.token_usage.output_tokens
        },
        "cost_breakdown": cost_breakdown,
        "cost_per_10k_lemmas": cost_breakdown["total_cost"] * 10000 / len(lemmas) if len(lemmas) > 0 else 0
    }
    
    return {
        "results": results,
        "metadata": metadata
    }

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
    
    Expected input format:
    {
      "lemmas": {
        "lemma_name": {
          "forms": {"form1": count1, "form2": count2, ...},
          "frequency": total_frequency,
          "log10_rate_per_billion": rate_value
        }
      }
    }
    
    Args:
        input_file: Path to the input JSON file containing lemmas and frequencies
        output_file: Path to save the output JSON file with definitions
        provider: LLM provider instance to use for generating definitions
        model: Model name to use for generating definitions
        batch_size: Number of lemmas to process in each batch
        limit: Optional maximum number of lemmas to process
        start: Starting index for processing lemmas
    """
    logger.info(f"Processing lemma file: {input_file}")
    
    # Read input file
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Validate input structure
    if "lemmas" not in data:
        raise ValueError("Input file must contain a 'lemmas' key at the root level")
    
    lemmas_data = data["lemmas"]
    if not isinstance(lemmas_data, dict):
        raise ValueError("'lemmas' must be a dictionary")
    
    # Extract lemmas with optional slicing
    lemmas = list(lemmas_data.keys())
    if limit:
        logger.info(f"Retrieving {limit} lemmas starting at index {start}: {start} - {start + limit}")
        lemmas = lemmas[start:start + limit]
    
    # Process in chunks of 1000
    chunk_size = 1000
    total_processed = 0
    all_results = []
    
    for chunk_start in range(0, len(lemmas), chunk_size):
        chunk_end = min(chunk_start + chunk_size, len(lemmas))
        chunk_lemmas = lemmas[chunk_start:chunk_end]
        
        logger.info(f"Processing chunk {chunk_start//chunk_size + 1}: lemmas {chunk_start} to {chunk_end}")
        
        # Generate definitions for this chunk
        generation_result = generate_definitions_for_lemmas(chunk_lemmas, provider, model, batch_size)
        all_results.extend(generation_result["results"])
        total_processed += len(chunk_lemmas)
        
        # Create output data for this chunk
        output_data = {}
        for lemma_info in generation_result["results"]:
            # Start with all original data for this lemma
            lemma_output = lemmas_data[lemma_info.lemma].copy()
            
            # Add the generated definition information
            lemma_output.update({
                "definitions": [vars(def_) for def_ in lemma_info.definitions],
                "should_learn": lemma_info.should_learn,
                "has_error": lemma_info.has_error,
                "error_description": lemma_info.error_description
            })
            
            output_data[lemma_info.lemma] = lemma_output

        # Add file-specific metadata
        header = generation_result["metadata"].copy()
        header.update({
            "limit": limit,
            "start": start,
            "chunk_start": chunk_start,
            "chunk_end": chunk_end,
            "total_processed": total_processed
        })

        # Create chunk output filename
        chunk_output_file = output_file.replace('.json', f'_chunk_{chunk_start//chunk_size + 1}.json')
        
        full_output_data = {
            "header": header,
            "lemmas": output_data
        }
        
        # Write chunk output file
        output_dir = os.path.dirname(chunk_output_file)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
        
        with open(chunk_output_file, 'w', encoding='utf-8') as f:
            json.dump(full_output_data, f, ensure_ascii=False, indent=2)
        
        logger.info(f"Chunk results saved to: {chunk_output_file}")
    
    # Create final combined output
    final_output_data = {}
    for lemma_info in all_results:
        # Start with all original data for this lemma
        lemma_output = lemmas_data[lemma_info.lemma].copy()
        
        # Add the generated definition information
        lemma_output.update({
            "definitions": [vars(def_) for def_ in lemma_info.definitions],
            "should_learn": lemma_info.should_learn,
            "has_error": lemma_info.has_error,
            "error_description": lemma_info.error_description
        })
        
        final_output_data[lemma_info.lemma] = lemma_output

    # Add final metadata
    final_header = {
        "model": model,
        "num_lemmas": len(all_results),
        "batch_size": batch_size,
        "timestamp": datetime.now().strftime("%Y%m%d_%H%M%S"),
        "token_usage": {
            "read_cached_input_tokens": provider.token_usage.read_cached_input_tokens,
            "written_cached_input_tokens": provider.token_usage.written_cached_input_tokens,
            "uncached_input_tokens": provider.token_usage.uncached_input_tokens,
            "output_tokens": provider.token_usage.output_tokens
        },
        "limit": limit,
        "start": start,
        "total_processed": total_processed
    }

    full_final_output = {
        "header": final_header,
        "lemmas": final_output_data
    }
    
    # Write final output file
    output_dir = os.path.dirname(output_file)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(full_final_output, f, ensure_ascii=False, indent=2)
    
    logger.info(f"Final combined results saved to: {output_file}")

def main():
    import argparse
    
    # Model configurations
    MODEL_OPTIONS = {
        "gpt-4.1-mini": {"provider": "openai", "model_id": "gpt-4.1-mini-2025-04-14"},
        "gpt-4.1-nano": {"provider": "openai", "model_id": "gpt-4.1-nano-2025-04-14"},
        "gpt-4o-mini": {"provider": "openai", "model_id": "gpt-4o-mini-2024-07-18"},
        "o4-mini": {"provider": "openai", "model_id": "o4-mini-2025-04-16"},
        "o3": {"provider": "openai", "model_id": "o3-2025-04-16"},
        "claude-4-sonnet": {"provider": "anthropic", "model_id": "claude-sonnet-4-20250514"},
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
        model_id = model_config["model_id"]
    else:
        raise ValueError("Model not specified")
    
    provider_class = AnthropicProvider if provider_type == "anthropic" else OpenAIProvider
    provider = provider_class()
    
    process_lemma_file(
        args.input_file,
        args.output_file,
        provider,
        model_id,
        args.batch_size,
        args.limit,
        args.start
    )

if __name__ == "__main__":
    main() 