# LLM Evaluation for Definition Generation

This document describes the LLM evaluation system implemented for GitHub issue #2.

## Overview

The evaluation system compares different Large Language Models (LLMs) for generating Spanish word definitions and linguistic information. It evaluates models based on:

1. **Cost** - Based on actual token usage and current API pricing
2. **Speed** - Time taken to process the sample
3. **Quality** - Using Claude 3 Sonnet as a judge to evaluate definition accuracy and completeness

## Files

- `evaluate_llms.py` - Main evaluation script
- `run_evaluation_example.py` - Example script showing how to run evaluations
- `generate_definitions.py` - Updated with complete OpenAI provider implementation

## Supported Models

The evaluation supports the following models with current pricing (as of 2025):

### Anthropic Models
- **Claude 3 Haiku** - $0.25/$1.25 per 1M input/output tokens
- **Claude 3.5 Haiku** - $0.80/$4.00 per 1M input/output tokens
- **Claude 3.5 Sonnet** - $3.00/$15.00 per 1M input/output tokens
- **Claude Sonnet 4** - $3.00/$15.00 per 1M input/output tokens (used as quality judge)

### OpenAI Models  
- **GPT-4.1 Nano** - $0.10/$0.40 per 1M input/output tokens (cheapest overall)
- **GPT-4.1 Mini** - $0.12/$0.50 per 1M input/output tokens (second cheapest overall)
- **GPT-4o Mini** - $0.15/$0.60 per 1M input/output tokens (third cheapest overall)

## Usage

### Basic Usage

```bash
python evaluate_llms.py final-lists/your_frequency_file.json
```

This will:
- Sample 500 lemmas from the top 10,000 most frequent words
- Evaluate GPT-4.1 Nano, GPT-4.1 Mini, and GPT-4o Mini (default cheapest models)
- Generate cost and speed metrics
- Track caching efficiency and cost savings
- Save results to `evaluation_results.json`

### Advanced Usage

```bash
python evaluate_llms.py final-lists/your_frequency_file.json \
    --sample-size 1000 \
    --max-rank 5000 \
    --models claude-3-haiku claude-3-5-haiku claude-3-5-sonnet gpt-4o-mini \
    --batch-size 10 \
    --evaluate-quality \
    --compare-batching \
    --compare-batch-api \
    --output detailed_evaluation.json
```

### Batching Efficiency Comparison

```bash
# Compare batching efficiency for cost optimization
python evaluate_llms.py final-lists/your_frequency_file.json \
    --compare-batching \
    --batching-test-sizes 1 5 25 100 \
    --models gpt-4-1-nano claude-3-haiku
```

This will test different batch sizes (including no batching with batch_size=1) to help you find the optimal balance between cost and speed for each model.

### Batch API Comparison

```bash
# Compare OpenAI Batch API vs real-time API
python evaluate_llms.py final-lists/your_frequency_file.json \
    --compare-batch-api \
    --batch-api-sample-size 100 \
    --models gpt-4-1-nano gpt-4o-mini
```

This compares the OpenAI Batch API (50% cost discount, longer processing time) against the real-time API to help you decide when to use each approach.

### Parameters

- `--sample-size`: Number of lemmas to sample (default: 500)
- `--max-rank`: Sample from top N most frequent lemmas (default: 10,000)
- `--batch-size`: Number of lemmas per API request (default: 5)
- `--models`: Which models to evaluate (default: claude-3-haiku, gpt-4o-mini)
- `--evaluate-quality`: Run quality evaluation using Claude Sonnet 4 as judge
- `--compare-batching`: Compare batching efficiency for cost optimization
- `--batching-test-sizes`: List of batch sizes to test for batching comparison
- `--compare-batch-api`: Compare OpenAI Batch API vs real-time API
- `--batch-api-sample-size`: Number of lemmas to sample for batch API comparison
- `--output`: Output file for results (default: evaluation_results.json)

## Environment Setup

Set the required API keys:

```bash
export ANTHROPIC_API_KEY="your-anthropic-key"
export OPENAI_API_KEY="your-openai-key"
```

## Output Format

The evaluation generates a JSON file with:

```json
{
  "evaluation_config": {
    "sample_size": 500,
    "max_rank": 10000,
    "batch_size": 5,
    "models_evaluated": ["claude-3-haiku", "gpt-4o-mini"],
    "quality_evaluation": true
  },
  "results": [
    {
      "model_name": "Claude 3 Haiku",
      "total_cost": 0.0234,
      "total_time": 45.2,
      "tokens_used": 15420,
      "definitions_generated": 487,
      "quality_score": 8.3,
      "cache_hits": 12,
      "cache_misses": 88,
      "cache_hit_percentage": 12.0,
      "cost_without_cache": 0.0267,
      "cost_savings_from_cache": 0.0033
    }
  ],
  "summary": {
    "total_models": 2,
    "cheapest_model": "GPT-4o Mini",
    "fastest_model": "Claude 3 Haiku",
    "highest_quality": "Claude 3 Haiku"
  }
}
```

## Quality Evaluation

When `--evaluate-quality` is enabled, the system:

1. Samples lemmas that all models successfully processed
2. Uses Claude Sonnet 4 as a judge to evaluate definition quality
3. Rates definitions on accuracy, completeness, and usefulness
4. Returns scores on a 1-10 scale

**Note**: Quality evaluation incurs additional costs as it uses Claude Sonnet 4.

## Cost Optimization Features

- **Caching**: Responses are cached to avoid re-processing the same lemmas
- **Batching**: Multiple lemmas are processed in single API requests
- **Sampling**: Evaluates on a representative sample rather than all data
- **Rate Limiting**: Includes delays to respect API rate limits
- **Cache Metrics**: Tracks cache hit rates and cost savings from caching

### Caching Benefits

The evaluation system automatically caches API responses, providing significant cost savings on repeated evaluations:

- **Cache Hit Tracking**: Shows percentage of requests served from cache
- **Cost Savings Calculation**: Displays actual cost savings from cache usage
- **Efficiency Metrics**: Helps optimize batch sizes and evaluation strategies

When running multiple evaluations or testing different configurations, caching can reduce costs by 50-90% for subsequent runs with overlapping lemma sets.

## Example Results

Based on a sample of 500 lemmas from the top 10,000 most frequent words:

## Cost and Speed Comparison

The evaluation system now defaults to the most cost-effective models while maintaining quality:

### Default Models (Cheapest Options)
- **GPT-4.1 Nano**: $0.0001 input / $0.0004 output per 1K tokens
- **Claude 3 Haiku**: $0.00025 input / $0.00125 output per 1K tokens

### Cost Comparison (per 1K tokens)
| Model | Input Cost | Output Cost | Total (1K in + 1K out) |
|-------|------------|-------------|-------------------------|
| GPT-4.1 Nano | $0.0001 | $0.0004 | $0.0005 |
| GPT-4o Mini | $0.00015 | $0.0006 | $0.00075 |
| Claude 3 Haiku | $0.00025 | $0.00125 | $0.00150 |
| GPT-4.1 Mini | $0.0004 | $0.0016 | $0.0020 |
| GPT-4.1 | $0.002 | $0.008 | $0.010 |
| Claude 3.5 Haiku | $0.0008 | $0.004 | $0.0048 |

### Speed vs Cost Trade-offs
- **Fastest + Cheapest**: GPT-4.1 Nano (best overall value)
- **Balanced**: GPT-4o Mini (slightly more expensive but very fast)
- **Quality Focus**: Claude 3.5 Haiku (higher cost but excellent quality)

## Running the Example

Use the provided example script:

```bash
python run_evaluation_example.py
```

This runs both a basic evaluation (cost/speed) and a full evaluation (with quality assessment) on smaller samples to demonstrate the functionality.

## Integration with Frequer

The evaluation system integrates with the existing Frequer workflow:

1. Run `frequer.py` to generate frequency data
2. Run `evaluate_llms.py` to compare models
3. Choose the best model for your use case
4. Run `generate_definitions.py` with your chosen model

## Troubleshooting

### Common Issues

1. **Missing API Keys**: Ensure environment variables are set
2. **File Not Found**: Check that the frequency file path is correct
3. **Rate Limiting**: The script includes delays, but you may need to adjust for your API limits
4. **Memory Issues**: Use smaller sample sizes if you encounter memory problems

### Performance Tips

- Start with small sample sizes (50-100) for testing
- Use caching to avoid re-processing during development
- Consider the cost implications of quality evaluation
- Monitor your API usage and costs

## Contributing

To add support for new models:

1. Add model configuration to `MODEL_CONFIGS` in `evaluate_llms.py`
2. Update pricing information
3. Test with a small sample
4. Update this documentation 