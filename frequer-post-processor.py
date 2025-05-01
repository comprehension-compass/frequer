#!/usr/bin/env python3
import json
import argparse
import re
import statistics
from collections import defaultdict
import spacy
from pathlib import Path

def load_frequency_data(input_file):
    """Load frequency data from JSON file."""
    print(f"Loading data from {input_file}...")
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def test_lemmatization(nlp, word):
    """Test how a word is currently lemmatized, returning the format 'word -> lemma'."""
    doc = nlp(word)
    if not doc or len(doc) == 0:
        return f"{word} -> Could not lemmatize"
    return f"{word} -> {doc[0].lemma_}"

def check_lemma_form_ratio(lemmas, ratio_threshold=100):
    """
    Flag lemmas where any form frequency is more than ratio_threshold times the median frequency.
    This helps identify potentially mis-lemmatized forms.
    """
    flagged_lemmas = {}
    
    for lemma, data in lemmas.items():
        forms = data["forms"]
        frequencies = list(forms.values())
        
        # Need at least 2 forms to calculate a meaningful ratio
        if len(frequencies) < 2:
            continue
            
        median_freq = statistics.median(frequencies)
        
        # Identify forms with frequencies significantly higher than the median
        high_ratio_forms = []
        for form, freq in forms.items():
            if median_freq > 0 and freq / median_freq > ratio_threshold:
                high_ratio_forms.append((form, freq, freq / median_freq))
        
        if high_ratio_forms:
            # Also find the lowest frequency forms for comparison
            sorted_forms = sorted(forms.items(), key=lambda x: x[1])
            lowest_forms = sorted_forms[:min(3, len(sorted_forms))]
            
            flagged_lemmas[lemma] = {
                "data": data,
                "reason": "form_ratio",
                "details": [],
                "highest_forms": high_ratio_forms,
                "lowest_forms": lowest_forms
            }
            
            for form, freq, ratio in high_ratio_forms:
                flagged_lemmas[lemma]["details"].append({
                    "form": form,
                    "frequency": freq,
                    "median_frequency": median_freq,
                    "ratio": ratio
                })
    
    return flagged_lemmas

def check_singular_plural_mismatch(lemmas, nlp):
    """
    Flag lemmas where removing plural endings results in a different lemma.
    This helps identify cases where plural forms should map to a different lemma.
    """
    flagged_lemmas = {}
    
    # Simple heuristic for languages with common plural suffixes
    plural_endings = {
        "s": "",      # e.g., "cars" -> "car"
        "es": "",     # e.g., "boxes" -> "box"
        "s": "r",     # e.g., "houses" -> "house"
    }
    
    for lemma, data in lemmas.items():
        # Skip lemmas that are too short
        if len(lemma) < 3:
            continue
            
        # Check if lemma looks like a plural form
        for plural_ending, replacement in plural_endings.items():
            if lemma.endswith(plural_ending):
                potential_singular = lemma[:-len(plural_ending)] + replacement
                potential_singular = potential_singular.strip()
                
                # Skip if potential singular is too short
                if len(potential_singular) < 2:
                    continue
                
                # Lemmatize the potential singular form
                doc = nlp(potential_singular)
                if not doc or len(doc) == 0:
                    continue
                
                singular_lemma = doc[0].lemma_
                
                # If the lemmatized singular form is different from our current lemma
                # and that lemma exists in our data, flag it
                if singular_lemma != lemma and singular_lemma in lemmas:
                    if lemma not in flagged_lemmas:
                        flagged_lemmas[lemma] = {
                            "data": data,
                            "reason": "plural_lemma",
                            "details": []
                        }
                    
                    flagged_lemmas[lemma]["details"].append({
                        "lemma": lemma,
                        "potential_singular": potential_singular,
                        "singular_lemma": singular_lemma,
                        "lemma_frequency": sum(data["forms"].values()),
                        "singular_lemma_frequency": sum(lemmas[singular_lemma]["forms"].values()),
                    })
    
    return flagged_lemmas

def check_lemma_consistency(lemmas, nlp):
    """
    Flag lemmas where the lemma itself has elsewhere been lemmatized to something else.
    """
    flagged_lemmas = {}
    
    # Process each lemma to see how it would be lemmatized by spaCy
    for lemma, data in lemmas.items():
        # Skip very short lemmas
        if len(lemma) < 2:
            continue
            
        # Lemmatize the lemma with spaCy
        doc = nlp(lemma)
        if not doc or len(doc) == 0:
            continue
            
        spacy_lemma = doc[0].lemma_
        
        # If spaCy lemmatizes differently and that lemma exists in our data
        if spacy_lemma != lemma and spacy_lemma in lemmas:
            if lemma not in flagged_lemmas:
                flagged_lemmas[lemma] = {
                    "data": data,
                    "reason": "inconsistent_lemma",
                    "details": [],
                    "spacy_lemma_data": lemmas[spacy_lemma]  # Store the data for the spacy lemma
                }
            
            flagged_lemmas[lemma]["details"].append({
                "lemma": lemma,
                "spacy_lemma": spacy_lemma,
                "lemma_frequency": sum(data["forms"].values()),
                "spacy_lemma_frequency": sum(lemmas[spacy_lemma]["forms"].values()),
            })
    
    return flagged_lemmas

def check_short_lemmas(lemmas, nlp):
    """Flag lemmas that are one or two characters long."""
    flagged_lemmas = {}
    
    for lemma, data in lemmas.items():
        if len(lemma) <= 2:
            # Test lemmatization for all forms
            form_lemmatizations = []
            for form in data["forms"]:
                form_lemmatizations.append((form, test_lemmatization(nlp, form)))
            
            flagged_lemmas[lemma] = {
                "data": data,
                "reason": "short_lemma",
                "details": [{
                    "lemma": lemma,
                    "length": len(lemma),
                    "frequency": sum(data["forms"].values()),
                }],
                "form_lemmatizations": form_lemmatizations
            }
    
    return flagged_lemmas

def check_case_sensitivity(lemmas):
    """Flag all non-lowercase lemmas for review as potential proper nouns."""
    flagged_lemmas = {}
    
    for lemma, data in lemmas.items():
        if lemma != lemma.lower():
            flagged_lemmas[lemma] = {
                "data": data,
                "reason": "non_lowercase",
                "details": [{
                    "lemma": lemma,
                    "lowercase": lemma.lower(),
                    "frequency": sum(data["forms"].values()),
                }]
            }
    
    return flagged_lemmas

def generate_lemmatization_rule(lemma, correct_lemma):
    """Generate a lemmatization rule that can be added to the lookup table."""
    return f'lemma_lookup["{lemma}"] = ["{correct_lemma}"]'

def generate_markdown_report(flagged_lemmas_by_category, nlp, output_file, lemma_ranks):
    """Generate a markdown report with all flagged lemmas for manual review."""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# Frequer Post-Processing Report\n\n")
        f.write("This report contains lemmas flagged for review based on various heuristics.\n\n")
        
        # Write each category of flagged lemmas
        categories = {
            "form_ratio": "Forms with Frequency Significantly Higher than Median",
            "plural_lemma": "Potential Plural Lemmas Instead of Singular",
            "inconsistent_lemma": "Inconsistent Lemmatization",
            "short_lemma": "Very Short Lemmas",
            "non_lowercase": "Non-Lowercase Lemmas (Potential Proper Nouns)",
        }
        
        for reason, label in categories.items():
            flagged_lemmas = flagged_lemmas_by_category.get(reason, {})
            
            if not flagged_lemmas:
                continue
                
            f.write(f"## {label} ({len(flagged_lemmas)} items)\n\n")
            
            for lemma, info in sorted(flagged_lemmas.items(), 
                                      key=lambda x: sum(x[1]["data"]["forms"].values()), 
                                      reverse=True):
                data = info["data"]
                details = info["details"]
                
                # Get frequency rank (position in overall frequency list)
                rank = lemma_ranks.get(lemma, "Unknown")
                
                f.write(f"### Lemma: `{lemma}` (Rank: #{rank})\n\n")
                f.write(f"- **Total frequency**: {sum(data['forms'].values())}\n")
                f.write(f"- **Log10 rate per billion**: {data['log10_rate_per_billion']}\n")
                f.write(f"- **Current lemmatization**: `{test_lemmatization(nlp, lemma)}`\n\n")
                
                # Display forms with their lemmatization
                f.write("**Forms and their lemmatization:**\n\n")
                f.write("| Form | Frequency | Lemmatization |\n")
                f.write("|------|----------:|---------------|\n")
                
                # For form_ratio, sort and display the most frequent forms first
                if reason == "form_ratio":
                    # Display highest frequency forms first
                    for form, freq, ratio in info.get("highest_forms", []):
                        f.write(f"| `{form}` | {freq} | `{test_lemmatization(nlp, form)}` |\n")
                    
                    # Then display a few of the lowest frequency forms for comparison
                    f.write("\n**Lowest frequency forms (for comparison):**\n\n")
                    f.write("| Form | Frequency | Lemmatization |\n")
                    f.write("|------|----------:|---------------|\n")
                    
                    for form, freq in info.get("lowest_forms", []):
                        f.write(f"| `{form}` | {freq} | `{test_lemmatization(nlp, form)}` |\n")
                else:
                    # For other reasons, just display all forms in frequency order
                    for form, freq in sorted(data["forms"].items(), key=lambda x: x[1], reverse=True):
                        f.write(f"| `{form}` | {freq} | `{test_lemmatization(nlp, form)}` |\n")
                
                f.write("\n**Reason for flagging:**\n\n")
                
                if reason == "form_ratio":
                    for detail in details:
                        f.write(f"- Form `{detail['form']}` has frequency {detail['frequency']}, "
                                f"which is {detail['ratio']:.1f}x the median frequency ({detail['median_frequency']}).\n")
                
                elif reason == "plural_lemma":
                    for detail in details:
                        f.write(f"- Lemma `{detail['lemma']}` appears to be a plural form. "
                                f"Potential singular form: `{detail['potential_singular']}` "
                                f"which lemmatizes to `{detail['singular_lemma']}` "
                                f"(Frequency: {detail['singular_lemma_frequency']}).\n")
                
                elif reason == "inconsistent_lemma":
                    for detail in details:
                        f.write(f"- Lemma `{detail['lemma']}` is lemmatized as `{detail['spacy_lemma']}` by spaCy. "
                                f"The alternative lemma has frequency {detail['spacy_lemma_frequency']}.\n")
                        
                    # Display information about the spaCy lemma entry
                    spacy_lemma = details[0]["spacy_lemma"]
                    if "spacy_lemma_data" in info:
                        spacy_data = info["spacy_lemma_data"]
                        f.write(f"\n**Alternative lemma entry (`{spacy_lemma}`) information:**\n\n")
                        f.write(f"- **Rank**: #{lemma_ranks.get(spacy_lemma, 'Unknown')}\n")
                        f.write(f"- **Total frequency**: {sum(spacy_data['forms'].values())}\n")
                        f.write(f"- **Forms**: {', '.join([f'`{form}`' for form in list(spacy_data['forms'].keys())[:10]])}"
                               f"{' and more...' if len(spacy_data['forms']) > 10 else ''}\n")
                
                elif reason == "short_lemma":
                    for detail in details:
                        f.write(f"- Lemma is only {detail['length']} characters long. "
                                f"Verify this is a valid word.\n")
                    
                    # Display lemmatization of all forms
                    if "form_lemmatizations" in info:
                        f.write("\n**Form lemmatizations:**\n\n")
                        for form, lemmatization in info["form_lemmatizations"]:
                            f.write(f"- `{lemmatization}`\n")
                
                elif reason == "non_lowercase":
                    for detail in details:
                        f.write(f"- Lemma `{detail['lemma']}` contains uppercase characters. "
                                f"Lowercase form would be `{detail['lowercase']}`.\n")
                
                f.write("\n**Example lemmatization rules to fix (if needed):**\n\n")
                f.write("```python\n")
                
                if reason == "plural_lemma" and details:
                    singular_lemma = details[0]["singular_lemma"]
                    f.write(f"{generate_lemmatization_rule(lemma, singular_lemma)}\n")
                    
                    # Add rules for all forms to map to the singular form
                    for form in data["forms"]:
                        if form != singular_lemma:
                            f.write(f"{generate_lemmatization_rule(form, singular_lemma)}\n")
                
                elif reason == "inconsistent_lemma" and details:
                    spacy_lemma = details[0]["spacy_lemma"]
                    f.write(f"{generate_lemmatization_rule(lemma, spacy_lemma)}\n")
                    
                    # Add rules for all forms
                    for form in data["forms"]:
                        f.write(f"{generate_lemmatization_rule(form, spacy_lemma)}\n")
                
                else:
                    f.write(f"# To be determined based on review. Some possibilities:\n")
                    f.write(f"{generate_lemmatization_rule(lemma, 'correct_lemma_here')}\n")
                    
                    # For non-lowercase, suggest mapping to lowercase version
                    if reason == "non_lowercase":
                        f.write(f"# If this should be lowercase:\n")
                        lowercase = lemma.lower()
                        f.write(f"{generate_lemmatization_rule(lemma, lowercase)}\n")
                
                f.write("```\n\n")
                f.write("---\n\n")
        
        # Generate prompts for LLM review
        f.write("## LLM Review Prompts\n\n")
        
        # 1. Lemmatization mistakes prompt
        f.write("### Prompt for Lemmatization Review\n\n")
        f.write("```\n")
        f.write("You are a linguistic expert. I'm working on creating a frequency list for language learners.\n\n")
        f.write("Please review the following lemmas and their forms, which have been flagged for potential lemmatization issues:\n\n")
        f.write("1. Identify any clear lemmatization mistakes\n")
        f.write("2. Suggest the correct lemma for each entry\n")
        f.write("3. Note any entries that appear to be from a different language\n")
        f.write("4. Provide your confidence level for each assessment (high, medium, low)\n\n")
        f.write("Your output should be a JSON array with entries following this format:\n")
        f.write('{\n  "lemma": "original_lemma",\n  "correct_lemma": "suggested_correction",\n  "foreign_language": true/false,\n  "confidence": "high/medium/low",\n  "notes": "Brief explanation"\n}\n')
        f.write("```\n\n")
        
        # 2. Proper nouns prompt
        f.write("### Prompt for Proper Nouns Review\n\n")
        f.write("```\n")
        f.write("You are a linguistic expert. I'm working on creating a frequency list for language learners.\n\n")
        f.write("Please review the following non-lowercase lemmas, which are likely proper nouns:\n\n")
        f.write("1. Categorize each proper noun into one of these categories:\n")
        f.write("   - ESSENTIAL: Proper nouns that language learners should know (countries, major cities, continents, etc.)\n")
        f.write("   - USEFUL: Proper nouns that are somewhat useful (common organizations, famous landmarks, etc.)\n")
        f.write("   - NONESSENTIAL: Proper nouns that language learners can safely ignore (personal names, brand names, etc.)\n")
        f.write("   - NOT_PROPER_NOUN: Words that appear to be capitalized for other reasons (beginning of sentences, errors, etc.)\n\n")
        f.write("2. Provide your confidence level for each assessment (high, medium, low)\n\n")
        f.write("Your output should be a JSON array with entries following this format:\n")
        f.write('{\n  "lemma": "ProperNoun",\n  "category": "ESSENTIAL/USEFUL/NONESSENTIAL/NOT_PROPER_NOUN",\n  "confidence": "high/medium/low",\n  "notes": "Brief explanation"\n}\n')
        f.write("```\n\n")
        
    print(f"Markdown report generated: {output_file}")

def prepare_llm_data(lemmas, max_lemmas=10000, output_file=None):
    """
    Prepare data for LLM review by selecting the top lemmas.
    Returns JSON string and optionally writes to a file.
    """
    # Sort lemmas by frequency
    sorted_lemmas = sorted(
        lemmas.items(),
        key=lambda x: sum(x[1]["forms"].values()),
        reverse=True
    )
    
    # Take top N lemmas
    top_lemmas = sorted_lemmas[:max_lemmas]
    
    # Create simpler format for LLM review
    llm_data = []
    for idx, (lemma, data) in enumerate(top_lemmas):
        forms_data = {form: freq for form, freq in data["forms"].items()}
        llm_data.append({
            "rank": idx + 1,
            "lemma": lemma,
            "total_frequency": sum(data["forms"].values()),
            "forms": forms_data
        })
    
    # Convert to JSON string
    json_data = json.dumps(llm_data, ensure_ascii=False, indent=2)
    
    # Write to file if output_file is provided
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(json_data)
        print(f"LLM data file generated: {output_file}")
    
    return json_data

def main():
    parser = argparse.ArgumentParser(description="Post-process the filtered output from frequer script")
    parser.add_argument("input_file", help="Path to the filtered JSON output file from frequer")
    parser.add_argument("lang", help="Language code (e.g., 'es' for Spanish)")
    parser.add_argument("--output-dir", "-o", default=".", help="Directory to save output files")
    parser.add_argument("--form-ratio-threshold", type=float, default=1000.0, 
                        help="Threshold for flagging forms with frequency much higher than median")
    parser.add_argument("--max-llm-lemmas", type=int, default=10000, 
                        help="Maximum number of top lemmas to include in LLM data")
    parser.add_argument("--max-review-lemmas", type=int, default=20000,
                        help="Maximum number of top lemmas to include in manual review (default: 20000)")
    
    args = parser.parse_args()
    
    # Create output directory if it doesn't exist
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Load spaCy model for lemmatization
    print(f"Loading spaCy model for language: {args.lang}")
    nlp = spacy.blank(args.lang)
    nlp.add_pipe("lemmatizer", config={"mode": "lookup"})
    nlp.initialize()
    
    # Load frequency data
    data = load_frequency_data(args.input_file)
    lemmas = data["lemmas"]
    stats = data["statistics"]
    
    # Generate base filename for outputs
    input_base_name = Path(args.input_file).stem
    
    # Create a dictionary mapping lemmas to their frequency rank
    print("Computing lemma frequency ranks...")
    sorted_lemmas = sorted(
        lemmas.items(),
        key=lambda x: sum(x[1]["forms"].values()),
        reverse=True
    )
    lemma_ranks = {lemma: idx + 1 for idx, (lemma, _) in enumerate(sorted_lemmas)}
    
    # Create a set of top lemmas to include in review
    top_lemmas_set = set(lemma for lemma, _ in sorted_lemmas[:args.max_review_lemmas])
    print(f"Limiting review to top {args.max_review_lemmas} lemmas by frequency")
    
    # Run all checks and combine results
    print("Running analysis...")
    flagged_by_category = {
        "form_ratio": check_lemma_form_ratio(lemmas, args.form_ratio_threshold),
        "plural_lemma": check_singular_plural_mismatch(lemmas, nlp),
        "inconsistent_lemma": check_lemma_consistency(lemmas, nlp),
        "short_lemma": check_short_lemmas(lemmas, nlp),
        "non_lowercase": check_case_sensitivity(lemmas),
    }
    
    # Filter flagged lemmas to include only those in top_lemmas_set
    flagged_by_category_filtered = {}
    for category, flagged in flagged_by_category.items():
        flagged_by_category_filtered[category] = {
            lemma: info for lemma, info in flagged.items() 
            if lemma in top_lemmas_set
        }
    
    # Count total flagged lemmas (a lemma might be flagged for multiple reasons)
    all_flagged = set()
    all_flagged_filtered = set()
    
    for category, flagged in flagged_by_category.items():
        all_flagged.update(flagged.keys())
        
    for category, flagged in flagged_by_category_filtered.items():
        all_flagged_filtered.update(flagged.keys())
    
    print(f"Analysis complete.")
    print(f"Found {len(all_flagged)} total lemmas to flag for review.")
    print(f"After filtering to top {args.max_review_lemmas} lemmas: {len(all_flagged_filtered)} lemmas to review.")
    
    # Generate markdown report with filtered lemmas
    markdown_output = output_dir / f"{input_base_name}_review.md"
    generate_markdown_report(flagged_by_category_filtered, nlp, markdown_output, lemma_ranks)
    
    # Prepare LLM data
    llm_output = output_dir / f"{input_base_name}_llm_data.json"
    prepare_llm_data(lemmas, args.max_llm_lemmas, llm_output)
    
    print("Post-processing complete!")
    print(f"Markdown report: {markdown_output}")
    print(f"LLM data file: {llm_output}")
    
    # Print summary statistics
    print("\nSummary of flagged items (after filtering to top lemmas):")
    for category, label in {
        "form_ratio": "Forms with unusual frequency ratios",
        "plural_lemma": "Potential plural lemmas",
        "inconsistent_lemma": "Inconsistently lemmatized words",
        "short_lemma": "Very short lemmas",
        "non_lowercase": "Non-lowercase lemmas",
    }.items():
        print(f"  - {label}: {len(flagged_by_category_filtered[category])}")
    print(f"  - Total unique flagged lemmas: {len(all_flagged_filtered)}")

if __name__ == "__main__":
    main()