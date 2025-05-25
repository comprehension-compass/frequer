#!/usr/bin/env python3
"""
Example script to run LLM evaluation for GitHub issue #2.
This demonstrates how to use the evaluate_llms.py script.
"""

import subprocess
import sys
import os
from pathlib import Path

def main():
    # Check if the frequency file exists
    frequency_file = "final-lists/en-es_paracrawl_lemmatized_freq_filtered_20250524_175918.json"
    
    if not os.path.exists(frequency_file):
        print(f"Error: Frequency file not found: {frequency_file}")
        print("Please ensure you have run the frequer.py script first to generate frequency data.")
        return 1
    
    # Check if API keys are set
    if not os.getenv('ANTHROPIC_API_KEY') and not os.getenv('OPENAI_API_KEY'):
        print("Warning: No API keys found in environment variables.")
        print("Please set ANTHROPIC_API_KEY and/or OPENAI_API_KEY to run the evaluation.")
        print("Example:")
        print("  export ANTHROPIC_API_KEY='your-key-here'")
        print("  export OPENAI_API_KEY='your-key-here'")
        return 1
    
    print("Running LLM evaluation for GitHub issue #2...")
    print("This will:")
    print("1. Sample lemmas from the top 10,000 most frequent words")
    print("2. Evaluate the cheapest LLMs (Claude 3 Haiku and GPT-4o Mini) on cost, speed, and quality")
    print("3. Use Claude Sonnet 4 as a quality judge (optional)")
    print("4. Generate a comprehensive evaluation report")
    print()
    
    # Basic evaluation (cost and speed only)
    print("Running basic evaluation (cost and speed)...")
    cmd_basic = [
        sys.executable, "evaluate_llms.py",
        frequency_file,
        "--sample-size", "100",  # Smaller sample for demo
        "--models", "claude-3-haiku", "gpt-4o-mini",
        "--output", "evaluation_basic.json"
    ]
    
    try:
        result = subprocess.run(cmd_basic, check=True, capture_output=True, text=True)
        print("Basic evaluation completed successfully!")
        print("Results saved to: evaluation_basic.json")
    except subprocess.CalledProcessError as e:
        print(f"Error running basic evaluation: {e}")
        print("STDOUT:", e.stdout)
        print("STDERR:", e.stderr)
        return 1
    
    # Full evaluation with quality assessment (more expensive)
    print("\nRunning full evaluation with quality assessment...")
    print("Note: This will use Claude Sonnet 4 as a judge, which incurs additional costs.")
    
    cmd_full = [
        sys.executable, "evaluate_llms.py", 
        frequency_file,
        "--sample-size", "50",  # Even smaller for quality evaluation
        "--models", "claude-3-haiku", "gpt-4o-mini",
        "--evaluate-quality",
        "--output", "evaluation_full.json"
    ]
    
    try:
        result = subprocess.run(cmd_full, check=True, capture_output=True, text=True)
        print("Full evaluation completed successfully!")
        print("Results saved to: evaluation_full.json")
    except subprocess.CalledProcessError as e:
        print(f"Error running full evaluation: {e}")
        print("STDOUT:", e.stdout)
        print("STDERR:", e.stderr)
        return 1
    
    print("\nEvaluation complete! Check the JSON files for detailed results.")
    print("\nTo run a custom evaluation, use:")
    print(f"python evaluate_llms.py {frequency_file} --help")
    
    return 0

if __name__ == "__main__":
    sys.exit(main()) 