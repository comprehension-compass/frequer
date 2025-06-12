# Quick Setup Guide

## 1. Install Dependencies

```bash
pip install -r requirements.txt
```

## 2. Set Up API Keys

### Option A: Use .env File (Recommended)

1. Edit the `.env` file in the project root
2. Replace the placeholder values with your actual API keys:

```
OPENAI_API_KEY=sk-your-actual-openai-key-here
ANTHROPIC_API_KEY=sk-ant-your-actual-anthropic-key-here
```

### Option B: Set Environment Variables

**Windows:**
```cmd
set OPENAI_API_KEY=your-openai-api-key-here
set ANTHROPIC_API_KEY=your-anthropic-api-key-here
```

**macOS/Linux:**
```bash
export OPENAI_API_KEY="your-openai-api-key-here"
export ANTHROPIC_API_KEY="your-anthropic-api-key-here"
```

## 3. Test the Setup

Run a quick test with a small sample:

```bash
python evaluate_llms.py final-lists/your_frequency_file.json --sample-size 5 --models gpt-4o-mini
```

## 4. Get API Keys

- **OpenAI**: [platform.openai.com](https://platform.openai.com) → API Keys
- **Anthropic**: [console.anthropic.com](https://console.anthropic.com) → API Keys

## 5. Run Full Evaluation

```bash
# Basic evaluation
python evaluate_llms.py final-lists/your_frequency_file.json

# With batching comparison
python evaluate_llms.py final-lists/your_frequency_file.json --compare-batching

# With Batch API comparison (OpenAI only)
python evaluate_llms.py final-lists/your_frequency_file.json --compare-batch-api
```

## Troubleshooting

- **"Could not resolve authentication method"**: Check that your API keys are set correctly
- **"Module not found"**: Run `pip install -r requirements.txt`
- **"File not found"**: Make sure your frequency file path is correct

For detailed documentation, see `EVALUATION_README.md`. 