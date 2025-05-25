# Frequer

A tool for analyzing word frequencies in text and generating language learning resources.

## Features

1. Word frequency analysis from text input
2. Lemmatization support
3. Definition generation using LLMs (Anthropic Claude and OpenAI GPT)
4. **LLM evaluation and comparison** - Compare different models on cost, speed, and quality

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Generate Definitions

After running the frequency analysis with `frequer.py`, use `generate_definitions.py` to create definitions and learning information:

```bash
python generate_definitions.py final-lists/your_frequency_file.json output/definitions.json --provider anthropic --batch-size 5 --limit 100
```

Options:
- `--provider`: Choose between "anthropic" (default) or "openai"
- `--batch-size`: Number of lemmas to process in each API request (default: 5)
- `--limit`: Maximum number of lemmas to process (optional, processes all lemmas if not specified)

### Evaluate LLMs

Use `evaluate_llms.py` to compare different LLMs for definition generation:

```bash
python evaluate_llms.py final-lists/your_frequency_file.json --models claude-3-haiku gpt-4o-mini --evaluate-quality
```

This will evaluate models based on:
- **Cost**: Actual token usage and API pricing
- **Speed**: Processing time
- **Quality**: Using Claude Sonnet 4 as a judge (optional)

See `EVALUATION_README.md` for detailed documentation.

### Environment Variables

Set the following environment variables for API access:
- `ANTHROPIC_API_KEY`: Your Anthropic API key
- `OPENAI_API_KEY`: Your OpenAI API key

## Output Format

The definition generator produces a JSON file with the following structure for each lemma:

```json
{
  "lemma": {
    "frequency": <original_frequency>,
    "definitions": [
      {
        "definition": "string",
        "part_of_speech": "string",
        "gender": "string or null",
        "verb_group": "string or null",
        "accompanying_preposition": "string or null",
        "case_triggered": "string or null",
        "transitiveness": "string or null"
      }
    ],
    "should_learn": true/false,
    "has_error": false,
    "error_description": null
  }
}
```

## Features

- Multiple LLM provider support (Anthropic Claude and OpenAI)
- Response caching to reduce API costs
- Batch processing for efficiency
- Comprehensive linguistic information
- Learning recommendations
- Error detection and reporting