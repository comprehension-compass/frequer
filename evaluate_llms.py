"""
Script to evaluate different LLMs for definition generation task.
Implements GitHub issue #2: Run evaluation of different LLM performance.
"""

import json
import os
import random
import time
from dataclasses import dataclass, asdict
from typing import List, Dict, Optional, Any, Tuple
from pathlib import Path
import logging
import argparse
from generate_definitions import AnthropicProvider, OpenAIProvider, LemmaInfo, Definition
import anthropic
from openai import OpenAI

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class ModelConfig:
    """Configuration for a model to evaluate."""
    name: str
    provider: str
    model_id: str
    cost_per_input_token: float  # USD per 1000 tokens
    cost_per_output_token: float  # USD per 1000 tokens

@dataclass
class BatchingComparisonResult:
    """Results from comparing different batch sizes for a single model."""
    model_name: str
    batch_size: int
    total_cost: float
    total_time: float
    tokens_used: int
    definitions_generated: int
    requests_made: int
    cost_per_request: float
    time_per_request: float
    efficiency_score: float  # cost * time normalized metric

@dataclass
class BatchAPIComparisonResult:
    """Results from comparing Batch API vs real-time API."""
    model_name: str
    api_type: str  # "realtime" or "batch"
    total_cost: float
    total_time: float  # includes waiting time for batch API
    tokens_used: int
    definitions_generated: int
    cost_per_definition: float
    time_per_definition: float
    cost_savings_vs_realtime: float  # percentage savings
    batch_id: Optional[str] = None  # for batch API tracking

@dataclass
class EvaluationResult:
    """Results from evaluating a single model."""
    model_name: str
    total_cost: float
    total_time: float
    tokens_used: int
    definitions_generated: int
    batch_size: int = 5  # Track which batch size was used
    quality_score: Optional[float] = None
    quality_details: Optional[Dict] = None
    # Caching metrics
    cache_hits: int = 0
    cache_misses: int = 0
    cache_hit_percentage: float = 0.0
    cost_without_cache: float = 0.0
    cost_savings_from_cache: float = 0.0
    # Batching comparison results
    batching_comparison: Optional[List[BatchingComparisonResult]] = None
    # Batch API comparison results
    batch_api_comparison: Optional[List[BatchAPIComparisonResult]] = None

# Model configurations with current pricing (as of 2025)
MODEL_CONFIGS = {
    "claude-3-haiku": ModelConfig(
        name="Claude 3 Haiku",
        provider="anthropic",
        model_id="claude-3-haiku-20240307",
        cost_per_input_token=0.00025,  # $0.25 per 1M tokens
        cost_per_output_token=0.00125   # $1.25 per 1M tokens
    ),
    "claude-3-5-haiku": ModelConfig(
        name="Claude 3.5 Haiku",
        provider="anthropic", 
        model_id="claude-3-5-haiku-20241022",
        cost_per_input_token=0.0008,    # $0.80 per 1M tokens
        cost_per_output_token=0.004     # $4.00 per 1M tokens
    ),
    "claude-3-5-sonnet": ModelConfig(
        name="Claude 3.5 Sonnet",
        provider="anthropic",
        model_id="claude-3-5-sonnet-20241022", 
        cost_per_input_token=0.003,     # $3 per 1M tokens
        cost_per_output_token=0.015     # $15 per 1M tokens
    ),
    "claude-sonnet-4": ModelConfig(
        name="Claude Sonnet 4",
        provider="anthropic",
        model_id="claude-sonnet-4-20250514",
        cost_per_input_token=0.003,     # $3 per 1M tokens
        cost_per_output_token=0.015     # $15 per 1M tokens
    ),
    "gpt-4-1-nano": ModelConfig(
        name="GPT-4.1 Nano",
        provider="openai",
        model_id="gpt-4.1-nano",
        cost_per_input_token=0.0001,    # $0.10 per 1M tokens
        cost_per_output_token=0.0004    # $0.40 per 1M tokens
    ),
    "gpt-4-1-mini": ModelConfig(
        name="GPT-4.1 Mini",
        provider="openai",
        model_id="gpt-4.1-mini",
        cost_per_input_token=0.0004,    # $0.40 per 1M tokens
        cost_per_output_token=0.0016    # $1.60 per 1M tokens
    ),
    "gpt-4o-mini": ModelConfig(
        name="GPT-4o Mini",
        provider="openai",
        model_id="gpt-4o-mini",
        cost_per_input_token=0.00015,   # $0.15 per 1M tokens
        cost_per_output_token=0.0006    # $0.60 per 1M tokens
    )
}

def sample_lemmas_from_file(frequency_file: str, sample_size: int = 500, max_rank: int = 10000) -> List[str]:
    """Sample lemmas from frequency file, handling nested JSON structure."""
    with open(frequency_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Handle nested structure where lemmas are under 'lemmas' key
    if isinstance(data, dict) and 'lemmas' in data:
        lemmas_data = data['lemmas']
    else:
        lemmas_data = data
    
    total_entries = len(lemmas_data)
    logger.info(f"Total entries in frequency file: {total_entries}")
    
    # Sort by frequency (descending) and take top max_rank
    sorted_lemmas = sorted(lemmas_data.items(), key=lambda x: x[1]['frequency'], reverse=True)[:max_rank]
    
    # Sample from the top entries
    sample_lemmas = random.sample(sorted_lemmas, min(sample_size, len(sorted_lemmas)))
    
    logger.info(f"Sampled {len(sample_lemmas)} lemmas from top {max_rank} entries")
    return [lemma for lemma, _ in sample_lemmas]

class EnhancedAnthropicProvider(AnthropicProvider):
    """Enhanced Anthropic provider that tracks tokens and timing."""
    
    def __init__(self, model_id: str, api_key: Optional[str] = None):
        super().__init__(api_key)
        self.model_id = model_id
        self.total_input_tokens = 0
        self.total_output_tokens = 0
        self.total_time = 0
        # Caching metrics
        self.cache_hits = 0
        self.cache_misses = 0
        self.total_requests = 0
        
    def generate_definitions(self, lemmas: List[str], batch_size: int = 5) -> List[LemmaInfo]:
        results = []
        start_time = time.time()
        
        for i in range(0, len(lemmas), batch_size):
            batch = lemmas[i:i + batch_size]
            cache_key = f"{self.model_id}_{'_'.join(batch)}"
            self.total_requests += 1
            
            cached_response = self._get_cached_response(cache_key)
            if cached_response:
                self.cache_hits += 1
                logger.info(f"Cache hit for batch: {batch}")
                results.extend(cached_response)
                continue
                
            self.cache_misses += 1
            logger.info(f"Cache miss for batch: {batch}")
            prompt = self._create_prompt(batch)
            
            try:
                response = self.client.messages.create(
                    model=self.model_id,
                    max_tokens=1000,
                    messages=[{
                        "role": "user",
                        "content": prompt
                    }]
                )
                
                # Track token usage
                self.total_input_tokens += response.usage.input_tokens
                self.total_output_tokens += response.usage.output_tokens
                
                batch_results = self._parse_response(response.content[0].text, batch)
                self._set_cached_response(cache_key, batch_results)
                results.extend(batch_results)
                
            except Exception as e:
                logger.error(f"Error processing batch {batch}: {str(e)}")
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
            
        self.total_time = time.time() - start_time
        return results

class EnhancedOpenAIProvider(OpenAIProvider):
    """Enhanced OpenAI provider with full implementation and token tracking."""
    
    def __init__(self, model_id: str, api_key: Optional[str] = None):
        super().__init__(api_key)
        self.model_id = model_id
        self.total_input_tokens = 0
        self.total_output_tokens = 0
        self.total_time = 0
        # Caching metrics
        self.cache_hits = 0
        self.cache_misses = 0
        self.total_requests = 0
        
    def generate_definitions(self, lemmas: List[str], batch_size: int = 5) -> List[LemmaInfo]:
        results = []
        start_time = time.time()
        
        for i in range(0, len(lemmas), batch_size):
            batch = lemmas[i:i + batch_size]
            cache_key = f"{self.model_id}_{'_'.join(batch)}"
            self.total_requests += 1
            
            cached_response = self._get_cached_response(cache_key)
            if cached_response:
                self.cache_hits += 1
                logger.info(f"Cache hit for batch: {batch}")
                results.extend(cached_response)
                continue
                
            self.cache_misses += 1
            logger.info(f"Cache miss for batch: {batch}")
            prompt = self._create_prompt(batch)
            
            try:
                response = self.client.chat.completions.create(
                    model=self.model_id,
                    messages=[{
                        "role": "user",
                        "content": prompt
                    }],
                    max_tokens=1000,
                    temperature=0.1
                )
                
                # Track token usage
                self.total_input_tokens += response.usage.prompt_tokens
                self.total_output_tokens += response.usage.completion_tokens
                
                batch_results = self._parse_response(response.choices[0].message.content, batch)
                self._set_cached_response(cache_key, batch_results)
                results.extend(batch_results)
                
            except Exception as e:
                logger.error(f"Error processing batch {batch}: {str(e)}")
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
            
        self.total_time = time.time() - start_time
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

def create_provider(model_config: ModelConfig):
    """Create the appropriate provider for a model configuration."""
    if model_config.provider == "anthropic":
        return EnhancedAnthropicProvider(model_config.model_id)
    elif model_config.provider == "openai":
        return EnhancedOpenAIProvider(model_config.model_id)
    else:
        raise ValueError(f"Unknown provider: {model_config.provider}")

def evaluate_model(model_config: ModelConfig, lemmas: List[str], batch_size: int = 5) -> EvaluationResult:
    """Evaluate a single model on the given lemmas."""
    logger.info(f"Evaluating {model_config.name} on {len(lemmas)} lemmas")
    
    provider = create_provider(model_config)
    results = provider.generate_definitions(lemmas, batch_size)
    
    # Calculate costs
    total_input_cost = (provider.total_input_tokens / 1000) * model_config.cost_per_input_token
    total_output_cost = (provider.total_output_tokens / 1000) * model_config.cost_per_output_token
    total_cost = total_input_cost + total_output_cost
    
    # Calculate caching metrics
    cache_hit_percentage = (provider.cache_hits / max(provider.total_requests, 1)) * 100
    
    # Calculate cost without cache (what it would have cost if no caching)
    # Estimate tokens per request based on actual usage
    avg_input_tokens_per_request = provider.total_input_tokens / max(provider.cache_misses, 1)
    avg_output_tokens_per_request = provider.total_output_tokens / max(provider.cache_misses, 1)
    
    # Cost if all requests were cache misses
    cost_without_cache = (
        (provider.total_requests * avg_input_tokens_per_request / 1000) * model_config.cost_per_input_token +
        (provider.total_requests * avg_output_tokens_per_request / 1000) * model_config.cost_per_output_token
    )
    
    cost_savings_from_cache = cost_without_cache - total_cost
    
    # Count successful definitions
    successful_definitions = sum(1 for r in results if r.definitions and not r.has_error)
    
    return EvaluationResult(
        model_name=model_config.name,
        total_cost=total_cost,
        total_time=provider.total_time,
        tokens_used=provider.total_input_tokens + provider.total_output_tokens,
        definitions_generated=successful_definitions,
        batch_size=batch_size,
        cache_hits=provider.cache_hits,
        cache_misses=provider.cache_misses,
        cache_hit_percentage=cache_hit_percentage,
        cost_without_cache=cost_without_cache,
        cost_savings_from_cache=cost_savings_from_cache
    )

def compare_batching_efficiency(model_config: ModelConfig, lemmas: List[str], 
                              batch_sizes: List[int] = [1, 5, 25, 100]) -> List[BatchingComparisonResult]:
    """
    Compare the efficiency of different batch sizes for a given model.
    Tests non-batching (batch_size=1) vs various batching strategies.
    """
    logger.info(f"Comparing batching efficiency for {model_config.name} with batch sizes: {batch_sizes}")
    
    # Use a smaller sample for batching comparison to control costs
    sample_size = min(50, len(lemmas))
    test_lemmas = random.sample(lemmas, sample_size)
    
    results = []
    
    for batch_size in batch_sizes:
        logger.info(f"Testing batch size {batch_size}")
        
        # Create fresh provider for each test to avoid cache interference
        provider = create_provider(model_config)
        
        # Clear any existing cache for fair comparison
        if hasattr(provider, '_cache'):
            provider._cache.clear()
        
        start_time = time.time()
        definitions = provider.generate_definitions(test_lemmas, batch_size)
        end_time = time.time()
        
        # Calculate metrics
        total_time = end_time - start_time
        total_input_cost = (provider.total_input_tokens / 1000) * model_config.cost_per_input_token
        total_output_cost = (provider.total_output_tokens / 1000) * model_config.cost_per_output_token
        total_cost = total_input_cost + total_output_cost
        
        successful_definitions = sum(1 for d in definitions if d.definitions and not d.has_error)
        requests_made = provider.total_requests
        
        # Calculate efficiency metrics
        cost_per_request = total_cost / max(requests_made, 1)
        time_per_request = total_time / max(requests_made, 1)
        
        # Efficiency score: lower is better (combines cost and time)
        # Normalize by dividing by batch_size=1 baseline (will be calculated later)
        efficiency_score = total_cost * total_time
        
        results.append(BatchingComparisonResult(
            model_name=model_config.name,
            batch_size=batch_size,
            total_cost=total_cost,
            total_time=total_time,
            tokens_used=provider.total_input_tokens + provider.total_output_tokens,
            definitions_generated=successful_definitions,
            requests_made=requests_made,
            cost_per_request=cost_per_request,
            time_per_request=time_per_request,
            efficiency_score=efficiency_score
        ))
        
        # Small delay between tests
        time.sleep(2)
    
    # Normalize efficiency scores against batch_size=1 baseline
    baseline_score = next((r.efficiency_score for r in results if r.batch_size == 1), 1.0)
    for result in results:
        result.efficiency_score = result.efficiency_score / baseline_score
    
    logger.info(f"Batching comparison completed for {model_config.name}")
    return results

def compare_batch_api_efficiency(model_config: ModelConfig, lemmas: List[str], 
                                sample_size: int = 100) -> List[BatchAPIComparisonResult]:
    """
    Compare the efficiency of Batch API vs real-time API for a given model.
    Only supports OpenAI models that have Batch API support.
    """
    logger.info(f"Comparing Batch API efficiency for {model_config.name}")
    
    if model_config.provider != "openai":
        logger.warning(f"Batch API comparison only supported for OpenAI models, skipping {model_config.name}")
        return []
    
    # Use a smaller sample for batch API comparison to control costs and time
    test_lemmas = random.sample(lemmas, min(sample_size, len(lemmas)))
    
    results = []
    
    # Test real-time API first
    logger.info("Testing real-time API performance...")
    realtime_provider = create_provider(model_config)
    
    # Clear cache for fair comparison
    if hasattr(realtime_provider, '_cache'):
        realtime_provider._cache.clear()
    
    start_time = time.time()
    realtime_definitions = realtime_provider.generate_definitions(test_lemmas, batch_size=5)
    realtime_time = time.time() - start_time
    
    # Calculate real-time costs
    realtime_input_cost = (realtime_provider.total_input_tokens / 1000) * model_config.cost_per_input_token
    realtime_output_cost = (realtime_provider.total_output_tokens / 1000) * model_config.cost_per_output_token
    realtime_total_cost = realtime_input_cost + realtime_output_cost
    
    realtime_successful = sum(1 for d in realtime_definitions if d.definitions and not d.has_error)
    
    realtime_result = BatchAPIComparisonResult(
        model_name=model_config.name,
        api_type="realtime",
        total_cost=realtime_total_cost,
        total_time=realtime_time,
        tokens_used=realtime_provider.total_input_tokens + realtime_provider.total_output_tokens,
        definitions_generated=realtime_successful,
        cost_per_definition=realtime_total_cost / max(realtime_successful, 1),
        time_per_definition=realtime_time / max(realtime_successful, 1),
        cost_savings_vs_realtime=0.0  # baseline
    )
    results.append(realtime_result)
    
    # Test Batch API
    logger.info("Testing Batch API performance...")
    try:
        batch_result = _test_batch_api(model_config, test_lemmas, realtime_total_cost)
        if batch_result:
            results.append(batch_result)
    except Exception as e:
        logger.error(f"Error testing Batch API for {model_config.name}: {str(e)}")
        # Create a placeholder result indicating failure
        batch_result = BatchAPIComparisonResult(
            model_name=model_config.name,
            api_type="batch",
            total_cost=0.0,
            total_time=0.0,
            tokens_used=0,
            definitions_generated=0,
            cost_per_definition=0.0,
            time_per_definition=0.0,
            cost_savings_vs_realtime=0.0,
            batch_id="FAILED"
        )
        results.append(batch_result)
    
    logger.info(f"Batch API comparison completed for {model_config.name}")
    return results

def _test_batch_api(model_config: ModelConfig, lemmas: List[str], realtime_cost: float) -> Optional[BatchAPIComparisonResult]:
    """
    Test the OpenAI Batch API for the given lemmas.
    Returns None if batch API is not supported or fails.
    """
    import json
    import tempfile
    from openai import OpenAI
    
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    
    # Create batch requests
    batch_requests = []
    for i, lemma in enumerate(lemmas):
        # Create individual requests for batch processing
        request = {
            "custom_id": f"req_{i}_{lemma}",
            "method": "POST",
            "url": "/v1/chat/completions",
            "body": {
                "model": model_config.model_id,
                "messages": [
                    {
                        "role": "user",
                        "content": f"""For the following Spanish lemma, provide detailed linguistic information in JSON format:

Lemma: {lemma}

Provide:
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
{{"lemma": "{lemma}", "definitions": [...], "should_learn": true/false, "has_error": true/false, "error_description": "string or null"}}"""
                    }
                ],
                "max_tokens": 500,
                "temperature": 0.1
            }
        }
        batch_requests.append(request)
    
    # Create temporary file for batch input
    with tempfile.NamedTemporaryFile(mode='w', suffix='.jsonl', delete=False) as f:
        for request in batch_requests:
            f.write(json.dumps(request) + '\n')
        batch_file_path = f.name
    
    try:
        # Upload the batch file
        logger.info("Uploading batch file...")
        with open(batch_file_path, 'rb') as f:
            batch_file = client.files.create(file=f, purpose='batch')
        
        # Create the batch
        logger.info("Creating batch job...")
        start_time = time.time()
        batch = client.batches.create(
            input_file_id=batch_file.id,
            endpoint="/v1/chat/completions",
            completion_window="24h"
        )
        
        # Wait for batch completion (with timeout)
        logger.info(f"Waiting for batch {batch.id} to complete...")
        max_wait_time = 3600  # 1 hour timeout
        check_interval = 30   # Check every 30 seconds
        elapsed_time = 0
        
        while elapsed_time < max_wait_time:
            batch_status = client.batches.retrieve(batch.id)
            
            if batch_status.status == "completed":
                total_time = time.time() - start_time
                logger.info(f"Batch completed in {total_time:.2f} seconds")
                
                # Download and process results
                if batch_status.output_file_id:
                    output_file = client.files.content(batch_status.output_file_id)
                    results_data = output_file.content.decode('utf-8')
                    
                    # Parse results and calculate metrics
                    successful_definitions = 0
                    total_input_tokens = 0
                    total_output_tokens = 0
                    
                    for line in results_data.strip().split('\n'):
                        if line:
                            result = json.loads(line)
                            if result.get('response') and result['response'].get('body'):
                                usage = result['response']['body'].get('usage', {})
                                total_input_tokens += usage.get('prompt_tokens', 0)
                                total_output_tokens += usage.get('completion_tokens', 0)
                                
                                # Check if definition was successfully generated
                                content = result['response']['body']['choices'][0]['message']['content']
                                try:
                                    parsed_content = json.loads(content)
                                    if parsed_content.get('definitions') and not parsed_content.get('has_error'):
                                        successful_definitions += 1
                                except:
                                    pass  # Failed to parse, don't count as successful
                    
                    # Calculate costs (Batch API typically offers 50% discount)
                    batch_discount = 0.5  # 50% discount for batch API
                    batch_input_cost = (total_input_tokens / 1000) * model_config.cost_per_input_token * batch_discount
                    batch_output_cost = (total_output_tokens / 1000) * model_config.cost_per_output_token * batch_discount
                    batch_total_cost = batch_input_cost + batch_output_cost
                    
                    cost_savings = ((realtime_cost - batch_total_cost) / realtime_cost) * 100 if realtime_cost > 0 else 0
                    
                    return BatchAPIComparisonResult(
                        model_name=model_config.name,
                        api_type="batch",
                        total_cost=batch_total_cost,
                        total_time=total_time,
                        tokens_used=total_input_tokens + total_output_tokens,
                        definitions_generated=successful_definitions,
                        cost_per_definition=batch_total_cost / max(successful_definitions, 1),
                        time_per_definition=total_time / max(successful_definitions, 1),
                        cost_savings_vs_realtime=cost_savings,
                        batch_id=batch.id
                    )
                
            elif batch_status.status in ["failed", "expired", "cancelled"]:
                logger.error(f"Batch {batch.id} failed with status: {batch_status.status}")
                return None
            
            # Wait before checking again
            time.sleep(check_interval)
            elapsed_time += check_interval
            logger.info(f"Batch status: {batch_status.status}, elapsed: {elapsed_time}s")
        
        logger.warning(f"Batch {batch.id} timed out after {max_wait_time} seconds")
        return None
        
    finally:
        # Clean up temporary file
        try:
            os.unlink(batch_file_path)
        except:
            pass
    
    return None

def evaluate_quality_with_judge(results_by_model: Dict[str, List[LemmaInfo]], sample_size: int = 50) -> Dict[str, float]:
    """
    Use Claude Sonnet 4 as a judge to evaluate definition quality.
    Samples a subset of results for cost efficiency.
    """
    logger.info(f"Evaluating quality using Claude Sonnet 4 as judge on {sample_size} samples")
    
    # Sample lemmas that all models successfully processed
    common_lemmas = set.intersection(*[
        {r.lemma for r in results if r.definitions and not r.has_error}
        for results in results_by_model.values()
    ])
    
    if len(common_lemmas) < sample_size:
        sample_size = len(common_lemmas)
        logger.warning(f"Only {sample_size} lemmas processed by all models, using all of them")
    
    sampled_lemmas = random.sample(list(common_lemmas), sample_size)
    
    # Create judge client
    judge_client = anthropic.Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))
    
    quality_scores = {}
    
    for model_name, results in results_by_model.items():
        logger.info(f"Evaluating quality for {model_name}")
        
        # Get results for sampled lemmas
        model_results = {r.lemma: r for r in results}
        sampled_results = [model_results[lemma] for lemma in sampled_lemmas if lemma in model_results]
        
        if not sampled_results:
            quality_scores[model_name] = 0.0
            continue
        
        # Create evaluation prompt
        evaluation_data = []
        for result in sampled_results[:10]:  # Evaluate in batches of 10 for cost efficiency
            evaluation_data.append({
                "lemma": result.lemma,
                "definitions": [asdict(d) for d in result.definitions],
                "should_learn": result.should_learn
            })
        
        prompt = f"""Evaluate the quality of these Spanish word definitions on a scale of 1-10:

{json.dumps(evaluation_data, indent=2, ensure_ascii=False)}

Rate each definition based on:
1. Accuracy and correctness
2. Completeness of linguistic information
3. Appropriateness of the "should_learn" recommendation
4. Overall usefulness for language learners

Return a JSON object with:
- "overall_score": average score (1-10)
- "individual_scores": list of scores for each lemma
- "comments": brief explanation of the scoring

Format: {{"overall_score": 8.5, "individual_scores": [8, 9, 7, ...], "comments": "..."}}"""

        try:
            response = judge_client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=500,
                messages=[{"role": "user", "content": prompt}]
            )
            
            evaluation = json.loads(response.content[0].text)
            quality_scores[model_name] = evaluation.get("overall_score", 0.0)
            
        except Exception as e:
            logger.error(f"Error evaluating quality for {model_name}: {str(e)}")
            quality_scores[model_name] = 0.0
        
        time.sleep(2)  # Rate limiting for judge
    
    return quality_scores

def main():
    parser = argparse.ArgumentParser(description="Evaluate different LLMs for definition generation")
    parser.add_argument(
        "frequency_file",
        help="Path to the frequency JSON file"
    )
    parser.add_argument(
        "--sample-size",
        type=int,
        default=500,
        help="Number of lemmas to sample for evaluation"
    )
    parser.add_argument(
        "--max-rank",
        type=int,
        default=10000,
        help="Sample from top N most frequent lemmas"
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=5,
        help="Batch size for API requests"
    )
    parser.add_argument(
        "--models",
        nargs="+",
        choices=list(MODEL_CONFIGS.keys()),
        default=["gpt-4-1-nano", "gpt-4-1-mini", "gpt-4o-mini"],
        help="Models to evaluate"
    )
    parser.add_argument(
        "--output",
        default="evaluation_results.json",
        help="Output file for results"
    )
    parser.add_argument(
        "--evaluate-quality",
        action="store_true",
        help="Run quality evaluation using Claude Sonnet 4 as judge"
    )
    parser.add_argument(
        "--compare-batching",
        action="store_true",
        help="Compare efficiency of different batch sizes (tests batch sizes 1, 5, 25, 100)"
    )
    parser.add_argument(
        "--batching-test-sizes",
        nargs="+",
        type=int,
        default=[1, 5, 25, 100],
        help="Batch sizes to test when --compare-batching is enabled"
    )
    parser.add_argument(
        "--compare-batch-api",
        action="store_true",
        help="Compare Batch API vs real-time API efficiency (OpenAI models only)"
    )
    parser.add_argument(
        "--batch-api-sample-size",
        type=int,
        default=50,
        help="Number of lemmas to use for Batch API comparison (default: 50)"
    )
    
    args = parser.parse_args()
    
    # Sample lemmas
    lemmas = sample_lemmas_from_file(args.frequency_file, args.sample_size, args.max_rank)
    
    logger.info(f"Starting evaluation of {len(args.models)} models on {len(lemmas)} lemmas")
    
    # Evaluate each model
    evaluation_results = []
    results_by_model = {}
    
    for model_key in args.models:
        model_config = MODEL_CONFIGS[model_key]
        
        # Standard evaluation
        result = evaluate_model(model_config, lemmas, args.batch_size)
        
        # Batching comparison if requested
        if args.compare_batching:
            logger.info(f"Running batching comparison for {model_config.name}")
            batching_results = compare_batching_efficiency(
                model_config, 
                lemmas, 
                args.batching_test_sizes
            )
            result.batching_comparison = batching_results
        
        # Batch API comparison if requested
        if args.compare_batch_api:
            logger.info(f"Running Batch API comparison for {model_config.name}")
            batch_api_results = compare_batch_api_efficiency(
                model_config,
                lemmas,
                args.batch_api_sample_size
            )
            result.batch_api_comparison = batch_api_results
        
        evaluation_results.append(result)
        
        # Store results for quality evaluation
        if args.evaluate_quality:
            provider = create_provider(model_config)
            model_results = provider.generate_definitions(lemmas, args.batch_size)
            results_by_model[model_config.name] = model_results
    
    # Quality evaluation
    if args.evaluate_quality and results_by_model:
        logger.info("Running quality evaluation...")
        quality_scores = evaluate_quality_with_judge(results_by_model)
        for result in evaluation_results:
            result.quality_score = quality_scores.get(result.model_name, 0.0)
    
    # Save results
    output_data = {
        "evaluation_config": {
            "sample_size": len(lemmas),
            "max_rank": args.max_rank,
            "batch_size": args.batch_size,
            "models_evaluated": args.models,
            "quality_evaluation": args.evaluate_quality,
            "batching_comparison": args.compare_batching,
            "batching_test_sizes": args.batching_test_sizes if args.compare_batching else None,
            "batch_api_comparison": args.compare_batch_api,
            "batch_api_sample_size": args.batch_api_sample_size if args.compare_batch_api else None
        },
        "results": [asdict(result) for result in evaluation_results],
        "summary": {
            "total_models": len(evaluation_results),
            "cheapest_model": min(evaluation_results, key=lambda x: x.total_cost).model_name,
            "fastest_model": min(evaluation_results, key=lambda x: x.total_time).model_name,
        }
    }
    
    if args.evaluate_quality:
        output_data["summary"]["highest_quality"] = max(
            evaluation_results, 
            key=lambda x: x.quality_score or 0
        ).model_name
    
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)
    
    # Print summary
    print("\n" + "="*60)
    print("LLM EVALUATION RESULTS")
    print("="*60)
    
    for result in evaluation_results:
        print(f"\n{result.model_name}:")
        print(f"  Cost: ${result.total_cost:.4f}")
        print(f"  Time: {result.total_time:.2f}s")
        print(f"  Definitions: {result.definitions_generated}/{len(lemmas)}")
        print(f"  Cost per definition: ${result.total_cost/max(result.definitions_generated, 1):.4f}")
        print(f"  Batch size used: {result.batch_size}")
        
        # Caching information
        print(f"  Cache hits: {result.cache_hits}/{result.cache_hits + result.cache_misses} ({result.cache_hit_percentage:.1f}%)")
        if result.cost_savings_from_cache > 0:
            print(f"  Cost without cache: ${result.cost_without_cache:.4f}")
            print(f"  Cache savings: ${result.cost_savings_from_cache:.4f} ({(result.cost_savings_from_cache/result.cost_without_cache)*100:.1f}%)")
        
        if result.quality_score:
            print(f"  Quality score: {result.quality_score:.1f}/10")
        
        # Batching comparison results
        if result.batching_comparison:
            print(f"\n  Batching Efficiency Comparison:")
            print(f"    {'Batch Size':<10} {'Cost':<8} {'Time':<8} {'Requests':<9} {'Efficiency':<10}")
            print(f"    {'-'*10:<10} {'-'*8:<8} {'-'*8:<8} {'-'*9:<9} {'-'*10:<10}")
            
            for batch_result in result.batching_comparison:
                efficiency_indicator = "★" if batch_result.efficiency_score < 1.0 else " "
                print(f"    {batch_result.batch_size:<10} "
                      f"${batch_result.total_cost:<7.4f} "
                      f"{batch_result.total_time:<7.2f}s "
                      f"{batch_result.requests_made:<9} "
                      f"{batch_result.efficiency_score:<9.2f}{efficiency_indicator}")
            
            # Find best batch size
            best_batch = min(result.batching_comparison, key=lambda x: x.efficiency_score)
            print(f"    Best batch size: {best_batch.batch_size} (efficiency score: {best_batch.efficiency_score:.2f})")
            
            # Calculate savings from optimal batching vs no batching
            no_batch = next((r for r in result.batching_comparison if r.batch_size == 1), None)
            if no_batch and best_batch.batch_size != 1:
                cost_savings = no_batch.total_cost - best_batch.total_cost
                time_savings = no_batch.total_time - best_batch.total_time
                print(f"    Savings vs no batching: ${cost_savings:.4f} cost, {time_savings:.2f}s time")
        
        # Batch API comparison results
        if result.batch_api_comparison:
            print(f"\n  Batch API vs Real-time API Comparison:")
            print(f"    {'API Type':<12} {'Cost':<8} {'Time':<10} {'Cost/Def':<10} {'Savings':<8}")
            print(f"    {'-'*12:<12} {'-'*8:<8} {'-'*10:<10} {'-'*10:<10} {'-'*8:<8}")
            
            for api_result in result.batch_api_comparison:
                if api_result.batch_id == "FAILED":
                    print(f"    {api_result.api_type:<12} FAILED   -         -          -")
                else:
                    savings_str = f"{api_result.cost_savings_vs_realtime:.1f}%" if api_result.api_type == "batch" else "baseline"
                    time_str = f"{api_result.total_time:.1f}s" if api_result.total_time < 3600 else f"{api_result.total_time/3600:.1f}h"
                    print(f"    {api_result.api_type:<12} "
                          f"${api_result.total_cost:<7.4f} "
                          f"{time_str:<10} "
                          f"${api_result.cost_per_definition:<9.4f} "
                          f"{savings_str:<8}")
            
            # Summary of batch API benefits
            batch_api_result = next((r for r in result.batch_api_comparison if r.api_type == "batch"), None)
            if batch_api_result and batch_api_result.batch_id != "FAILED":
                print(f"    Batch API savings: {batch_api_result.cost_savings_vs_realtime:.1f}% cost reduction")
                if batch_api_result.total_time > 300:  # More than 5 minutes
                    print(f"    Note: Batch API takes longer ({batch_api_result.total_time/60:.1f} min) but offers significant cost savings")
    
    print(f"\nResults saved to: {args.output}")

if __name__ == "__main__":
    main() 