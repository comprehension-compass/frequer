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
import diskcache

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class Definition:
    definition: str
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

class LLMProvider(ABC):
    def __init__(self):
        cache_dir = Path('.cache') / 'llm_responses'
        cache_dir.mkdir(parents=True, exist_ok=True)
        self.cache = diskcache.Cache(str(cache_dir))
    
    @abstractmethod
    def generate_definitions(self, lemmas: List[str], batch_size: int) -> List[LemmaInfo]:
        pass

    def _get_cached_response(self, cache_key: str) -> Optional[Any]:
        return self.cache.get(cache_key)

    def _set_cached_response(self, cache_key: str, response: Any):
        self.cache.set(cache_key, response)

class AnthropicProvider(LLMProvider):
    def __init__(self, api_key: Optional[str] = None):
        super().__init__()
        self.client = anthropic.Anthropic(api_key=api_key or os.getenv('ANTHROPIC_API_KEY'))
        
    def generate_definitions(self, lemmas: List[str], batch_size: int = 5) -> List[LemmaInfo]:
        results = []
        
        for i in range(0, len(lemmas), batch_size):
            batch = lemmas[i:i + batch_size]
            cache_key = f"anthropic_{'_'.join(batch)}"
            
            cached_response = self._get_cached_response(cache_key)
            if cached_response:
                results.extend(cached_response)
                continue
                
            prompt = self._create_prompt(batch)
            
            try:
                response = self.client.messages.create(
                    model="claude-3-haiku-20240307",
                    max_tokens=1000,
                    messages=[{
                        "role": "user",
                        "content": prompt
                    }]
                )
                
                batch_results = self._parse_response(response.content[0].text, batch)
                self._set_cached_response(cache_key, batch_results)
                results.extend(batch_results)
                
            except Exception as e:
                logger.error(f"Error processing batch {batch}: {str(e)}")
                # Add error entries for failed batch
                results.extend([
                    LemmaInfo(
                        lemma=lemma,
                        definitions=[],
                        should_learn=False,
                        has_error=True,
                        error_description=f"Failed to process: {str(e)}"
                    ) for lemma in batch
                ])
            
            time.sleep(1)  # Rate limiting
            
        return results
    
    def _create_prompt(self, lemmas: List[str]) -> str:
        return f"""For each of the following Spanish lemmas, provide detailed linguistic information in JSON format:

Lemmas: {', '.join(lemmas)}

For each lemma, provide:
1. A list of definitions (each with fields: definition, part_of_speech, gender, verb_group, accompanying_preposition, case_triggered, transitiveness)
2. A boolean 'should_learn' field based on these rules:
   - False for proper nouns identical between languages
   - False for brand names and uncommon abbreviations
   - True for common abbreviations
   - True for core vocabulary
   - True for common cognates
   - False for borrowed words already familiar to learners
   - False for familiar numbers and symbols
3. A boolean 'has_error' field and optional 'error_description' for:
   - Lemmatisation errors
   - Non-sensical entries
   - Uncertain definitions

Return the response in this exact JSON format:
{{"lemmas": [
    {{
        "lemma": "example",
        "definitions": [
            {{
                "definition": "string",
                "part_of_speech": "string",
                "gender": "string or null",
                "verb_group": "string or null",
                "accompanying_preposition": "string or null",
                "case_triggered": "string or null",
                "transitiveness": "string or null"
            }}
        ],
        "should_learn": true/false,
        "has_error": true/false,
        "error_description": "string or null"
    }}
]}}"""

    def _parse_response(self, response: str, original_lemmas: List[str]) -> List[LemmaInfo]:
        try:
            data = json.loads(response)
            return [
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
        except Exception as e:
            logger.error(f"Error parsing response: {str(e)}")
            return [
                LemmaInfo(
                    lemma=lemma,
                    definitions=[],
                    should_learn=False,
                    has_error=True,
                    error_description="Failed to parse LLM response"
                ) for lemma in original_lemmas
            ]

class OpenAIProvider(LLMProvider):
    def __init__(self, api_key: Optional[str] = None):
        super().__init__()
        self.client = OpenAI(api_key=api_key or os.getenv('OPENAI_API_KEY'))
        
    def generate_definitions(self, lemmas: List[str], batch_size: int = 5) -> List[LemmaInfo]:
        results = []
        
        for i in range(0, len(lemmas), batch_size):
            batch = lemmas[i:i + batch_size]
            cache_key = f"openai_{'_'.join(batch)}"
            
            cached_response = self._get_cached_response(cache_key)
            if cached_response:
                results.extend(cached_response)
                continue
                
            prompt = self._create_prompt(batch)
            
            try:
                response = self.client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{
                        "role": "user",
                        "content": prompt
                    }],
                    max_tokens=1000,
                    temperature=0.1
                )
                
                batch_results = self._parse_response(response.choices[0].message.content, batch)
                self._set_cached_response(cache_key, batch_results)
                results.extend(batch_results)
                
            except Exception as e:
                logger.error(f"Error processing batch {batch}: {str(e)}")
                # Add error entries for failed batch
                results.extend([
                    LemmaInfo(
                        lemma=lemma,
                        definitions=[],
                        should_learn=False,
                        has_error=True,
                        error_description=f"Failed to process: {str(e)}"
                    ) for lemma in batch
                ])
            
            time.sleep(1)  # Rate limiting
            
        return results
    
    def _create_prompt(self, lemmas: List[str]) -> str:
        """Create prompt for OpenAI (same format as Anthropic)."""
        return f"""For each of the following Spanish lemmas, provide detailed linguistic information in JSON format:

Lemmas: {', '.join(lemmas)}

For each lemma, provide:
1. A list of definitions (each with fields: definition, part_of_speech, gender, verb_group, accompanying_preposition, case_triggered, transitiveness)
2. A boolean 'should_learn' field based on these rules:
   - False for proper nouns identical between languages
   - False for brand names and uncommon abbreviations
   - True for common abbreviations
   - True for core vocabulary
   - True for common cognates
   - False for borrowed words already familiar to learners
   - False for familiar numbers and symbols
3. A boolean 'has_error' field and optional 'error_description' for:
   - Lemmatisation errors
   - Non-sensical entries
   - Uncertain definitions

Return the response in this exact JSON format:
{{"lemmas": [
    {{
        "lemma": "example",
        "definitions": [
            {{
                "definition": "string",
                "part_of_speech": "string",
                "gender": "string or null",
                "verb_group": "string or null",
                "accompanying_preposition": "string or null",
                "case_triggered": "string or null",
                "transitiveness": "string or null"
            }}
        ],
        "should_learn": true/false,
        "has_error": true/false,
        "error_description": "string or null"
    }}
]}}"""

    def _parse_response(self, response: str, original_lemmas: List[str]) -> List[LemmaInfo]:
        """Parse OpenAI response (same format as Anthropic)."""
        try:
            data = json.loads(response)
            return [
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
        except Exception as e:
            logger.error(f"Error parsing response: {str(e)}")
            return [
                LemmaInfo(
                    lemma=lemma,
                    definitions=[],
                    should_learn=False,
                    has_error=True,
                    error_description="Failed to parse LLM response"
                ) for lemma in original_lemmas
            ]

def process_lemma_file(
    input_file: str,
    output_file: str,
    provider: LLMProvider,
    batch_size: int = 5,
    limit: Optional[int] = None
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
        logger.info(f"Limiting processing to first {limit} lemmas")
        lemmas = lemmas[:limit]
    
    results = provider.generate_definitions(lemmas, batch_size)
    
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
    
    output_dir = os.path.dirname(output_file)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)
    
    logger.info(f"Results saved to: {output_file}")

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Generate definitions for lemmas using LLM APIs")
    parser.add_argument("input_file", help="Path to input JSON file containing lemmas")
    parser.add_argument("output_file", help="Path to save output JSON file with definitions")
    parser.add_argument(
        "--provider",
        choices=["anthropic", "openai"],
        default="anthropic",
        help="LLM provider to use"
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
    
    args = parser.parse_args()
    
    provider_class = AnthropicProvider if args.provider == "anthropic" else OpenAIProvider
    provider = provider_class()
    
    process_lemma_file(
        args.input_file,
        args.output_file,
        provider,
        args.batch_size,
        args.limit
    )

if __name__ == "__main__":
    main() 