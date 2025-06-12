"""
Evaluation script to compare different models for Spanish definition generation.

This script:
1. Runs generate_definitions over specified models on randomly selected words
2. Uses Claude Sonnet 4 to blindly evaluate the quality of definitions
3. Compares costs and quality scores across models
"""

import json
import os
import random
import subprocess
import tempfile
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Tuple
import anthropic
import argparse
import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Model configurations
MODEL_CONFIGS = {
    "gpt-4.1-nano": "gpt-4.1-nano",
    "gpt-4.1-mini": "gpt-4.1-mini",
    "gpt-4o-mini": "gpt-4o-mini",
    "o4-mini": "o4-mini",
    "o3": "o3",
    "claude-4-sonnet": "claude-4-sonnet",
    "claude-3.5-haiku": "claude-3.5-haiku",
    "claude-3-haiku": "claude-3-haiku"
}

# Evaluation prompt for Claude Sonnet 4
EVALUATION_PROMPT = """You are an expert Spanish language teacher evaluating AI-generated definitions for Spanish lemmas. You will be shown definitions from multiple models (labeled as Model A, Model B, etc.) for a set of Spanish words.

EVALUATION CRITERIA:
1. **Accuracy**: Are the definitions correct and complete?
2. **Clarity**: Are definitions clear and learner-friendly?
3. **Example Quality**: Are example sentences natural, appropriate difficulty, and helpful?
4. **Grammatical Metadata**: Are part of speech, gender, verb groups, etc. correct?
5. **Preposition Patterns**: Are accompanying prepositions correctly identified when relevant?
6. **Multiple Meanings**: Are important different meanings included when appropriate?
7. **Translation Quality**: Are English translations of examples natural and accurate?
8. MOST IMPORTANT: **Value to language learners**: Would the entry be valuable to a language learner who wants to quickly understand what the word means in a passage they are reading?

IMPORTANT EVALUATION NOTES:
- **Cloze Deletion Format**: Example sentences use {{c1:word_form}} format where word_form can be ANY inflected form of the lemma (conjugated verbs, plural nouns, feminine adjectives, etc.). This is CORRECT and expected.
- **Inflected Forms**: It is perfectly acceptable and often preferable for the cloze to contain inflected forms rather than the base lemma (e.g., {{c1:trabajadora}} for feminine form, {{c1:responden}} for conjugated verb).
- **Grammatical Agreement**: The word form in the cloze should match the grammatical context of the sentence (gender, number, conjugation).
= **Gender**: the gender listed should match the original lemma, not the gender of the word in the example sentence

Evaluate each model's overall performance across ALL the provided words collectively. Consider consistency, accuracy patterns, and overall educational value.

For each model, provide:
- A score from 1-10 (10 being excellent) based on overall performance across all words
- A detailed comment (1-2 sentences) explaining the score, highlighting strengths and weaknesses

Be objective and focus on educational value for Spanish learners.

Return your evaluation in this exact JSON format:
{
  "model_evaluations": {
    "Model A": {
      "score": 8,
      "comment": "Generally accurate definitions with good grammatical metadata. Example sentences are natural and appropriate for learners. However, occasionally misses secondary meanings and some preposition patterns could be better identified. Overall solid performance for educational use."
    },
    "Model B": {
      "score": 9,
      "comment": "Excellent comprehensive coverage with consistently accurate definitions. Example sentences are well-crafted and translations are natural. Strong identification of multiple meanings and preposition patterns. Very high educational value with minor room for improvement in complex cases."
    }
  },
  "comparative_analysis": "Detailed comparison of the models' relative strengths and weaknesses across the evaluation set.",
  "words_evaluated": ["list", "of", "words", "evaluated"]
}"""

def select_random_words(lemma_file: str, top_n: int, num_words: int) -> List[str]:
    """Select random words from the top N most frequent words."""
    logger.info(f"Selecting {num_words} random words from top {top_n} words")
    
    with open(lemma_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    lemmas = list(data["lemmas"].keys())[:top_n]
    selected = random.sample(lemmas, min(num_words, len(lemmas)))
    
    logger.info(f"Selected words: {selected}")
    return selected

def run_model_generation(model_name: str, lemma_file: str, words: List[str], output_dir: str) -> Tuple[str, Dict[str, Any]]:
    """Run generate_definitions for a specific model on given words."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join(output_dir, f"eval_{model_name}_{timestamp}.json")
    
    # Create a temporary file with just the selected words
    with open(lemma_file, 'r', encoding='utf-8') as f:
        full_data = json.load(f)
    
    # Create subset data with only selected words
    subset_data = {
        "lemmas": {word: full_data["lemmas"][word] for word in words if word in full_data["lemmas"]}
    }
    
    temp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False, encoding='utf-8')
    json.dump(subset_data, temp_file, ensure_ascii=False, indent=2)
    temp_file.close()
    
    try:
        # Run generate_definitions
        cmd = [
            "python", "generate_definitions.py",
            temp_file.name,
            output_file,
            "--model", model_name,
            "--batch-size", "5"
        ]
        
        logger.info(f"Running {model_name} on {len(words)} words")
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        
        # Load and return the results
        with open(output_file, 'r', encoding='utf-8') as f:
            output_data = json.load(f)
        
        return output_file, output_data
        
    except subprocess.CalledProcessError as e:
        logger.error(f"Error running {model_name}: {e}")
        logger.error(f"Stdout: {e.stdout}")
        logger.error(f"Stderr: {e.stderr}")
        raise
    finally:
        # Clean up temp file
        os.unlink(temp_file.name)

def prepare_evaluation_data(model_outputs: Dict[str, Dict[str, Any]], words: List[str]) -> Tuple[Dict[str, Dict[str, Any]], Dict[str, str]]:
    """Prepare data for evaluation by organizing by word and obfuscating model names."""
    evaluation_data = {}
    model_mapping = {}
    
    # Create obfuscated model names
    model_names = list(model_outputs.keys())
    random.shuffle(model_names)  # Randomize order
    for i, model_name in enumerate(model_names):
        model_mapping[f"Model {chr(65 + i)}"] = model_name  # Model A, Model B, etc.
    
    # Organize data by word
    for word in words:
        evaluation_data[word] = {}
        for obfuscated_name, real_name in model_mapping.items():
            if word in model_outputs[real_name]["lemmas"]:
                evaluation_data[word][obfuscated_name] = model_outputs[real_name]["lemmas"][word]
    
    return evaluation_data, model_mapping

def evaluate_with_claude(evaluation_data: Dict[str, Dict[str, Any]], words_subset: List[str]) -> Dict[str, Any]:
    """Use Claude Sonnet 4 to evaluate model outputs."""
    client = anthropic.Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))
    
    # Prepare the subset for evaluation
    subset_data = {word: evaluation_data[word] for word in words_subset if word in evaluation_data}
    
    # Create the evaluation prompt
    prompt = f"{EVALUATION_PROMPT}\n\nEVALUATE THESE DEFINITIONS:\n\nWords to evaluate: {words_subset}\n\n{json.dumps(subset_data, ensure_ascii=False, indent=2)}"
    
    logger.info(f"Evaluating {len(words_subset)} words with Claude Sonnet 4")
    
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=4000,
        messages=[{
            "role": "user",
            "content": prompt
        }],
        temperature=0.1
    )
    
    # Parse the response
    response_text = response.content[0].text
    
    # Handle JSON wrapped in markdown code blocks
    if '```json' in response_text:
        start_idx = response_text.find('```json') + 7
        end_idx = response_text.find('```', start_idx)
        if start_idx != -1 and end_idx != -1:
            response_text = response_text[start_idx:end_idx].strip()
    elif '```' in response_text:
        start_idx = response_text.find('```')
        end_idx = response_text.find('```', start_idx + 3)
        if start_idx != -1 and end_idx != -1:
            response_text = response_text[start_idx + 3:end_idx].strip()
    
    try:
        evaluation_result = json.loads(response_text)
        return evaluation_result
    except json.JSONDecodeError as e:
        logger.error(f"Failed to parse Claude evaluation response: {e}")
        logger.error(f"Response: {response_text}")
        raise

def calculate_model_scores(evaluations: List[Dict[str, Any]], model_mapping: Dict[str, str]) -> Dict[str, Dict[str, Any]]:
    """Calculate average scores for each model across all evaluations."""
    model_scores = {real_name: {"scores": [], "total_score": 0, "count": 0, "comments": []} for real_name in model_mapping.values()}
    
    for evaluation in evaluations:
        if "model_evaluations" in evaluation:
            for obfuscated_name, eval_data in evaluation["model_evaluations"].items():
                if obfuscated_name in model_mapping:
                    real_name = model_mapping[obfuscated_name]
                    score = eval_data.get("score", 0)
                    comment = eval_data.get("comment", "")
                    model_scores[real_name]["scores"].append(score)
                    model_scores[real_name]["total_score"] += score
                    model_scores[real_name]["count"] += 1
                    model_scores[real_name]["comments"].append(comment)
    
    # Calculate averages
    for model_name in model_scores:
        if model_scores[model_name]["count"] > 0:
            model_scores[model_name]["average"] = model_scores[model_name]["total_score"] / model_scores[model_name]["count"]
        else:
            model_scores[model_name]["average"] = 0
    
    return model_scores

def run_evaluation(
    models: List[str],
    lemma_file: str,
    top_n: int = 1000,
    num_eval_words: int = 30,
    output_dir: str = "outputs/evaluation"
) -> None:
    """Run the complete evaluation process."""
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    # Select random words for evaluation
    eval_words = select_random_words(lemma_file, top_n, num_eval_words)
    
    # Run generation for each model
    model_outputs = {}
    model_costs = {}
    
    for model_name in models:
        try:
            output_file, output_data = run_model_generation(model_name, lemma_file, eval_words, output_dir)
            model_outputs[model_name] = output_data
            
            # Extract cost information
            if "header" in output_data and "cost_breakdown" in output_data["header"]:
                model_costs[model_name] = output_data["header"]["cost_breakdown"]
            
            logger.info(f"Completed generation for {model_name}")
            
        except Exception as e:
            logger.error(f"Failed to run {model_name}: {e}")
            continue
    
    if not model_outputs:
        logger.error("No models completed successfully")
        return
    
    # Prepare evaluation data with obfuscated model names
    evaluation_data, model_mapping = prepare_evaluation_data(model_outputs, eval_words)
    
    # Split evaluation words into 5 rounds
    words_per_round = len(eval_words) // 5
    evaluation_rounds = [
        eval_words[i:i + words_per_round] 
        for i in range(0, len(eval_words), words_per_round)
    ]
    
    # Run 5 evaluation rounds
    all_evaluations = []
    for i, round_words in enumerate(evaluation_rounds):
        if not round_words:
            continue
            
        logger.info(f"Running evaluation round {i + 1} with {len(round_words)} words")
        try:
            evaluation_result = evaluate_with_claude(evaluation_data, round_words)
            all_evaluations.append(evaluation_result)
        except Exception as e:
            logger.error(f"Evaluation round {i + 1} failed: {e}")
            continue
    
    # Calculate final scores
    model_scores = calculate_model_scores(all_evaluations, model_mapping)
    
    # Create final report
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report = {
        "evaluation_metadata": {
            "timestamp": timestamp,
            "models_evaluated": list(models),
            "num_words": len(eval_words),
            "evaluation_words": eval_words,
            "top_n_selection": top_n
        },
        "model_mapping": model_mapping,
        "cost_analysis": {
            model: {
                **costs,
                "cost_per_10k_definitions": (costs.get("total_cost", 0) * 10000 / len(eval_words)) if len(eval_words) > 0 else 0
            }
            for model, costs in model_costs.items()
        },
        "quality_scores": {
            model: {
                "average_score": scores["average"],
                "total_evaluations": scores["count"],
                "score_distribution": scores["scores"]
            }
            for model, scores in model_scores.items()
        },
        "detailed_evaluations": all_evaluations,
        "summary": {
            "best_quality": max(model_scores.items(), key=lambda x: x[1]["average"])[0] if model_scores else None,
            "lowest_cost": min(model_costs.items(), key=lambda x: x[1].get("total_cost", float('inf')))[0] if model_costs else None
        }
    }
    
    # Save final report
    report_file = os.path.join(output_dir, f"evaluation_report_{timestamp}.json")
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    
    # Print summary
    logger.info("=== EVALUATION SUMMARY ===")
    logger.info(f"Models evaluated: {len(model_outputs)}")
    logger.info(f"Words evaluated: {len(eval_words)}")
    logger.info(f"Evaluation rounds: {len(all_evaluations)}")
    
    if model_scores:
        logger.info("\n=== QUALITY SCORES ===")
        for model, scores in sorted(model_scores.items(), key=lambda x: x[1]["average"], reverse=True):
            logger.info(f"{model}: {scores['average']:.2f}/10 (n={scores['count']})")
    
    if model_costs:
        logger.info("\n=== COST ANALYSIS ===")
        for model, costs in sorted(model_costs.items(), key=lambda x: x[1].get("total_cost", 0)):
            total_cost = costs.get("total_cost", 0)
            cost_per_10k = (total_cost * 10000 / len(eval_words)) if len(eval_words) > 0 else 0
            logger.info(f"{model}: ${total_cost:.6f} (${cost_per_10k:.2f} per 10k definitions)")
    
    logger.info(f"\nDetailed report saved to: {report_file}")

def main():
    parser = argparse.ArgumentParser(description="Evaluate Spanish definition generation models")
    parser.add_argument("lemma_file", help="Path to input JSON file containing lemmas")
    parser.add_argument(
        "--models",
        nargs="+",
        choices=list(MODEL_CONFIGS.keys()),
        default=["gpt-4.1-nano", "claude-3.5-haiku"],
        help="Models to evaluate"
    )
    parser.add_argument(
        "--top-n",
        type=int,
        default=1000,
        help="Select evaluation words from top N most frequent words"
    )
    parser.add_argument(
        "--num-words",
        type=int,
        default=30,
        help="Number of words to evaluate"
    )
    parser.add_argument(
        "--output-dir",
        default="outputs/evaluation",
        help="Directory to save evaluation results"
    )
    
    args = parser.parse_args()
    
    run_evaluation(
        models=args.models,
        lemma_file=args.lemma_file,
        top_n=args.top_n,
        num_eval_words=args.num_words,
        output_dir=args.output_dir
    )

if __name__ == "__main__":
    main() 