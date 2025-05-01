import spacy
import pandas as pd
from collections import defaultdict, Counter
import json
import os
from datetime import datetime, timedelta
import time
from tqdm import tqdm
import math
from wordfreq import word_frequency, top_n_list
import pickle
import argparse
import concurrent.futures
import multiprocessing

def default_dict_factory():
    """Factory function for creating a default dict of int"""
    return defaultdict(int)

def load_checkpoint(checkpoint_file):
    """Load checkpoint data if it exists"""
    if os.path.exists(checkpoint_file):
        print(f"Loading checkpoint from {checkpoint_file}")
        with open(checkpoint_file, 'rb') as f:
            checkpoint_data = pickle.load(f)
        return checkpoint_data
    return None

def save_checkpoint(checkpoint_file, lemma_counts, total_words, processed_lines, chunk_num, start_time):
    """Save checkpoint data"""
    print(f"Saving checkpoint to {checkpoint_file}")
    checkpoint_data = {
        'lemma_counts': lemma_counts,
        'total_words': total_words,
        'processed_lines': processed_lines,
        'chunk_num': chunk_num,
        'start_time': start_time,
        'last_update_time': time.time()
    }
    with open(checkpoint_file, 'wb') as f:
        pickle.dump(checkpoint_data, f)

def process_sentences_in_chunks(file_path, nlp, chunk_size=10000000, min_frequency=3, checkpoint_file=None, file_format="tatoeba", max_lines=None, num_workers=None):
    """
    Process sentences from a large TSV file in chunks
    
    Args:
        file_path: Path to the TSV file
        nlp: spaCy language model
        chunk_size: Number of sentences to process per chunk
        min_frequency: Minimum frequency threshold for lemmas
        checkpoint_file: Path to save/load checkpoint data
        file_format: Format of input file, either "tatoeba" or "paracrawl"
        max_lines: Maximum number of lines to process (for testing)
        num_workers: Number of worker processes for parallel processing
    """
    # Initialize counters and data structures
    lemma_counts = defaultdict(default_dict_factory)  # Use named factory function instead of lambda
    total_words = 0
    processed_lines = 0
    chunk_num = 0
    start_time = time.time()
    
    # Check if checkpoint exists and load it
    if checkpoint_file and os.path.exists(checkpoint_file):
        checkpoint_data = load_checkpoint(checkpoint_file)
        if checkpoint_data:
            lemma_counts = checkpoint_data['lemma_counts']
            total_words = checkpoint_data['total_words']
            processed_lines = checkpoint_data['processed_lines']
            chunk_num = checkpoint_data['chunk_num']
            # Restore original start time if available, otherwise use current time
            start_time = checkpoint_data.get('start_time', time.time())
            
            elapsed_time = format_time(time.time() - start_time)
            print(f"Resuming from checkpoint: processed {processed_lines} sentences, {total_words} words, chunk {chunk_num}")
            print(f"Time elapsed so far: {elapsed_time}")
    
    # Get total number of lines for progress reporting
    if max_lines:
        print(f"Will process at most {max_lines} lines")
        # Count lines up to max_lines or total file size, whichever is smaller
        total_lines = 0
        with open(file_path, 'r', encoding='utf-8') as f:
            for _ in range(max_lines):
                if next(f, None) is None:
                    break
                total_lines += 1
        print(f"Counted {total_lines} lines (limited by --max-lines={max_lines})")
    else:
        total_lines = sum(1 for _ in open(file_path, 'r', encoding='utf-8'))
        print(f"Total lines in file: {total_lines}")
    
    # Open the file and skip already processed lines
    with open(file_path, 'r', encoding='utf-8') as f:
        if processed_lines > 0:
            print(f"Skipping {processed_lines} already processed lines...")
            for _ in range(processed_lines):
                next(f, None)
        
        # Process in chunks
        current_chunk = []
        line_count = 0
        
        print(f"Processing from line {processed_lines+1} in chunks of {chunk_size} sentences...")
        
        chunk_start_time = time.time()
        
        for line in f:
            # Check if we've reached the maximum number of lines
            if max_lines and processed_lines + line_count >= max_lines:
                break
                
            text = None
            
            if file_format == "tatoeba":
                # Tatoeba format: id, lang, text
                parts = line.strip().split('\t')
                if len(parts) >= 3:
                    text = parts[2]
                else:
                    # Handle malformed lines
                    print(f"Warning: Skipping malformed Tatoeba line: {line}")
            
            elif file_format == "paracrawl":
                # Paracrawl format: English text, target language text
                parts = line.strip().split('\t')
                if len(parts) >= 2:
                    # We only want the target language text (second column)
                    text = parts[1]
                else:
                    # Handle malformed lines
                    print(f"Warning: Skipping malformed Paracrawl line: {line}")
            
            # Add to current chunk if we have valid text
            if text:
                current_chunk.append(text)
                
            line_count += 1
            
            # Process chunk when it reaches the desired size
            if line_count % chunk_size == 0:
                print(f"\nProcessing chunk {chunk_num+1} ({len(current_chunk)} sentences)...")
                chunk_words = process_chunk(current_chunk, nlp, lemma_counts, num_workers)
                
                # Update counters
                processed_lines += len(current_chunk)
                total_words += chunk_words
                chunk_num += 1
                
                # Calculate and display timing information
                current_time = time.time()
                chunk_time = format_time(current_time - chunk_start_time)
                total_time = format_time(current_time - start_time)
                
                # Estimate remaining time
                if processed_lines > 0:
                    time_per_line = (current_time - start_time) / processed_lines
                    remaining_lines = min(total_lines, max_lines if max_lines else total_lines) - processed_lines
                    estimated_remaining = time_per_line * remaining_lines
                    remaining_time = format_time(estimated_remaining)
                else:
                    remaining_time = "unknown"
                
                print(f"Chunk processing time: {chunk_time}")
                print(f"Total processing time: {total_time}")
                print(f"Estimated remaining time: {remaining_time}")
                
                # Save checkpoint
                save_checkpoint(checkpoint_file, lemma_counts, total_words, processed_lines, chunk_num, start_time)
                
                # Clear the chunk and reset chunk start time
                current_chunk = []
                chunk_start_time = time.time()
                
                # Show progress - adjust total based on max_lines if provided
                total_to_process = min(total_lines, max_lines) if max_lines else total_lines
                print(f"Progress: {processed_lines}/{total_to_process} lines processed ({(processed_lines/total_to_process)*100:.2f}%)")
                print(f"Total words so far: {total_words}")
        
        # Process remaining sentences
        if current_chunk:
            print(f"\nProcessing final chunk ({len(current_chunk)} sentences)...")
            chunk_words = process_chunk(current_chunk, nlp, lemma_counts, num_workers)
            processed_lines += len(current_chunk)
            total_words += chunk_words
    
    # Calculate final processing time
    end_time = time.time()
    total_processing_time = format_time(end_time - start_time)
    
    # Calculate frequency and create result dictionary
    result_all = create_result_dictionary(lemma_counts, total_words)
    
    # Apply filters
    result_filtered, stats = apply_filters(result_all, lemma_counts, total_words, processed_lines, min_frequency)
    
    # Add timing information to stats
    stats['processing_time_seconds'] = end_time - start_time
    stats['processing_time_formatted'] = total_processing_time
    
    return result_all, result_filtered, stats

def format_time(seconds):
    """Format seconds as days, hours, minutes, seconds"""
    return str(timedelta(seconds=int(seconds)))

def process_sentence_batch(batch, nlp):
    """Process a batch of sentences and return lemma counts
    
    This is a helper function for parallel processing.
    """
    # Process the batch with spaCy
    local_lemma_counts = Counter()
    local_form_counts = defaultdict(Counter)
    word_count = 0
    
    for doc in nlp.pipe(batch, batch_size=100):
        for token in doc:
            if not token.is_punct and not token.is_space:
                lemma = token.lemma_
                form = token.text
                local_lemma_counts[lemma] += 1
                local_form_counts[lemma][form] += 1
                word_count += 1
    
    return local_lemma_counts, local_form_counts, word_count

def process_chunk(sentences, nlp, lemma_counts, num_workers=None):
    """Process a chunk of sentences and update lemma counts using parallel processing"""
    if num_workers is None:
        # Default to number of CPU cores minus 1 (leave one for system)
        num_workers = max(1, multiprocessing.cpu_count() - 1)
    
    # Calculate batch size (aim for at least 1000 sentences per batch)
    total_sentences = len(sentences)
    batch_size = max(1000, total_sentences // (num_workers * 4))
    
    # Create batches
    batches = [sentences[i:i+batch_size] for i in range(0, total_sentences, batch_size)]
    num_batches = len(batches)
    
    print(f"Processing {total_sentences} sentences in {num_batches} batches using {num_workers} workers")
    
    chunk_words = 0
    processed_batches = 0
    
    # Process batches in parallel
    with concurrent.futures.ProcessPoolExecutor(max_workers=num_workers) as executor:
        # Submit all batch processing tasks
        future_to_batch = {
            executor.submit(process_sentence_batch, batch, nlp): i 
            for i, batch in enumerate(batches)
        }
        
        # Process results as they complete
        for future in tqdm(concurrent.futures.as_completed(future_to_batch), total=len(batches)):
            try:
                local_lemma_counts, local_form_counts, word_count = future.result()
                
                # Update the global counts
                for lemma, count in local_lemma_counts.items():
                    for form, form_count in local_form_counts[lemma].items():
                        lemma_counts[lemma][form] += form_count
                
                chunk_words += word_count
                processed_batches += 1
                
                # Provide periodic updates
                if processed_batches % 10 == 0 or processed_batches == num_batches:
                    completion_percentage = (processed_batches / num_batches) * 100
                    print(f"Completed {processed_batches}/{num_batches} batches ({completion_percentage:.1f}%), {chunk_words} words processed so far")
                
            except Exception as e:
                print(f"Error processing batch: {e}")
    
    print(f"Processed {total_sentences} sentences with {chunk_words} words in this chunk.")
    return chunk_words

def create_result_dictionary(lemma_counts, total_words):
    """Create result dictionary with lemma information"""
    result_all = {}
    for lemma, forms in lemma_counts.items():
        # Calculate total frequency for this lemma (sum of all forms)
        frequency = sum(forms.values())
        # Calculate rate per billion words
        rate_per_billion = (frequency / total_words) * 1000000000
        
        # Add to result dictionary
        result_all[lemma] = {
            "forms": dict(forms),
            "frequency": frequency,
            "log10_rate_per_billion": round(math.log10(rate_per_billion) if rate_per_billion > 0 else 0, 2)
        }
    
    return result_all

def apply_filters(result_all, lemma_counts, total_words, total_sentences, min_frequency):
    """Apply filters to lemmas and generate statistics"""
    # Count the total number of unique lemmas before any filtering
    total_lemmas_before = len(result_all)
    
    # Filter out lemmas with frequency less than min_frequency
    result_filtered_freq = {lemma: data for lemma, data in result_all.items() 
                           if data["frequency"] >= min_frequency}
    
    # Count after frequency filtering
    total_lemmas_after_freq = len(result_filtered_freq)
    
    # Filter out lemmas that don't contain at least one letter
    # This includes digits (e.g., "123"), punctuation ("°", "%"), and number formats ("150.000", "5,000")
    import re
    # Unicode regex pattern for any letter (includes accented characters, special letters across languages)
    has_letter_pattern = re.compile(r'[^\W\d_]', re.UNICODE)  # Matches any Unicode letter character
    
    result_filtered_nonwords = {}
    nonword_lemmas = set()
    
    for lemma, data in result_filtered_freq.items():
        if has_letter_pattern.search(lemma):
            # Lemma contains at least one letter
            result_filtered_nonwords[lemma] = data
        else:
            # Lemma doesn't contain any letters (only digits, symbols, etc.)
            nonword_lemmas.add(lemma)
    
    total_lemmas_after_nonwords = len(result_filtered_nonwords)
    
    # Display some of the filtered out non-word lemmas
    if nonword_lemmas:
        print(f"Filtered out {len(nonword_lemmas)} non-word lemmas (no letters): {', '.join(list(nonword_lemmas)[:15])}{'...' if len(nonword_lemmas) > 15 else ''}")
    
    # Optimized approach for uppercase lemma merging
    print("Identifying uppercase lemmas to merge with their lowercase counterparts...")
    lemmas_to_remove = set()
    lemma_merges = {}  # Dict to track which lemmas are merged with which
    
    # Build an inverse dictionary mapping forms to lemmas: {form: {lemma: frequency}}
    print("Building inverse dictionary (form -> lemmas)...")
    form_to_lemmas = defaultdict(dict)
    for lemma, data in result_filtered_nonwords.items():
        for form, freq in data['forms'].items():
            form_to_lemmas[form][lemma] = freq
    
    # Find non-lowercase lemmas that need to be merged
    print("Identifying non-lowercase lemmas to merge...")
    non_lowercase_lemmas = [lemma for lemma in result_filtered_nonwords if lemma.lower() != lemma]
    print(f"Found {len(non_lowercase_lemmas)} non-lowercase lemmas to check")
    
    # For each non-lowercase lemma, check if its lowercase version exists as a form
    for lemma in tqdm(non_lowercase_lemmas):
        lowercase_form = lemma.lower()
        
        # Check if this lowercase form exists as a form under any lemma
        if lowercase_form in form_to_lemmas:
            # Get lemmas that have this form
            containing_lemmas = form_to_lemmas[lowercase_form]
            
            # Filter lemmas where the frequency meets the threshold
            qualifying_lemmas = {target_lemma: freq for target_lemma, freq in containing_lemmas.items() 
                               if freq >= min_frequency}
            
            if qualifying_lemmas:
                # Find the lemma where this lowercase form has the highest frequency
                target_lemma = max(qualifying_lemmas.items(), key=lambda x: x[1])[0]
                
                # Mark for merge
                lemmas_to_remove.add(lemma)
                lemma_merges[lemma] = target_lemma
    
    # Third pass: Merge the frequency data of non-lowercase lemmas into their target lemmas
    print(f"Merging {len(lemmas_to_remove)} non-lowercase lemmas with their target lemmas...")
    skipped_merges = 0
    
    for lemma in lemmas_to_remove:
        target_lemma = lemma_merges[lemma]
        
        # Safety check: ensure the target lemma exists
        if target_lemma not in result_filtered_nonwords:
            print(f"  Warning: Cannot merge '{lemma}' because target '{target_lemma}' no longer exists (likely filtered out)")
            skipped_merges += 1
            continue
        
        non_lowercase_data = result_filtered_nonwords[lemma]
        
        # Add frequency to target lemma
        original_freq = result_filtered_nonwords[target_lemma]['frequency']
        additional_freq = non_lowercase_data['frequency']
        result_filtered_nonwords[target_lemma]['frequency'] += additional_freq
        
        # Recalculate log10_rate_per_billion
        new_rate = (result_filtered_nonwords[target_lemma]['frequency'] / total_words) * 1000000000
        result_filtered_nonwords[target_lemma]['log10_rate_per_billion'] = round(
            math.log10(new_rate) if new_rate > 0 else 0, 2
        )
        
        # Also add the non-lowercase lemma itself as a form under target_lemma if not already there
        if lemma not in result_filtered_nonwords[target_lemma]['forms']:
            # We add it with the same frequency as the non-lowercase lemma
            result_filtered_nonwords[target_lemma]['forms'][lemma] = non_lowercase_data['frequency']
        else:
            # If it's already there, add the frequencies
            result_filtered_nonwords[target_lemma]['forms'][lemma] += non_lowercase_data['frequency']
        
        # Merge forms dictionaries
        for form, freq in non_lowercase_data['forms'].items():
            if form in result_filtered_nonwords[target_lemma]['forms']:
                result_filtered_nonwords[target_lemma]['forms'][form] += freq
            else:
                result_filtered_nonwords[target_lemma]['forms'][form] = freq
    
    # Fourth pass: Remove the merged lemmas
    result_filtered_final = {lemma: data for lemma, data in result_filtered_nonwords.items() 
                        if lemma not in lemmas_to_remove}
    
    # Count after case filtering
    total_lemmas_after_case = len(result_filtered_final)
    
    # Add statistics
    stats = {
        "total_words": total_words,
        "total_sentences": total_sentences,
        "unique_lemmas_before_filtering": total_lemmas_before,
        "unique_lemmas_after_frequency_filtering": total_lemmas_after_freq,
        "unique_lemmas_after_nonword_filtering": total_lemmas_after_nonwords,
        "lemmas_removed_by_frequency": total_lemmas_before - total_lemmas_after_freq,
        "lemmas_removed_by_nonword_filtering": total_lemmas_after_freq - total_lemmas_after_nonwords,
        "lemmas_removed_by_case_check": total_lemmas_after_nonwords - total_lemmas_after_case,
        "unique_lemmas_after_all_filtering": total_lemmas_after_case,
        "total_lemmas_removed": total_lemmas_before - total_lemmas_after_case,
        "minimum_frequency_threshold": min_frequency,
        "merged_uppercase_lemmas_count": len(lemmas_to_remove) - skipped_merges,
        "skipped_merges_count": skipped_merges
    }
    
    if skipped_merges > 0:
        print(f"Note: Skipped {skipped_merges} merges due to missing target lemmas")
    
    return result_filtered_final, stats

def compare_with_wordfreq(your_lemmas, language_code, nlp, top_n=1000):
    """
    Compare your top lemmas with wordfreq's top lemmas (after lemmatization).
    
    Args:
        your_lemmas: Dictionary of your lemma data
        language_code: Language code for wordfreq (e.g., 'es' for Spanish)
        nlp: Loaded spaCy model for lemmatization
        top_n: Number of top lemmas to compare
    
    Returns:
        Dictionary with comparison statistics
    """
    
    # Get your top lemmas by frequency
    sorted_your_lemmas = sorted(
        your_lemmas.items(), 
        key=lambda x: x[1]['frequency'], 
        reverse=True
    )
    your_top_lemmas = [lemma for lemma, _ in sorted_your_lemmas[:top_n]]
    
    # Get wordfreq's top forms (get 5x more to account for lemmatization convergence)
    try:
        wordfreq_top_forms = top_n_list(language_code, top_n * 5)
    except ValueError as e:
        print(f"Error with wordfreq: {e}")
        return {"error": str(e)}
    
    # Create a dictionary to store combined frequencies by lemma
    wordfreq_lemma_counts = defaultdict(float)
    
    # Process each form from wordfreq
    for form in wordfreq_top_forms:
        # Get the actual frequency from wordfreq
        freq = word_frequency(form, language_code)
        
        # Lemmatize the form
        doc = nlp(form)
        if len(doc) > 0:  # Ensure we have at least one token
            lemma = doc[0].lemma_
            # Add the frequency to this lemma
            wordfreq_lemma_counts[lemma] += freq
    
    # Sort lemmas by their aggregated frequency
    sorted_wordfreq_lemmas = sorted(
        wordfreq_lemma_counts.items(),
        key=lambda x: x[1],
        reverse=True
    )
    
    # Take top_n lemmas from the sorted list
    wordfreq_top_lemmas = [lemma for lemma, _ in sorted_wordfreq_lemmas[:top_n]]
    
    # Find the intersection
    common_lemmas = set(your_top_lemmas) & set(wordfreq_top_lemmas)
    
    # Calculate statistics
    comparison_stats = {
        "your_top_lemmas_count": len(your_top_lemmas),
        "wordfreq_top_lemmas_count": len(wordfreq_top_lemmas),
        "common_lemmas_count": len(common_lemmas),
        "percentage_overlap": round((len(common_lemmas) / top_n) * 100, 2),
        "common_lemmas": sorted(list(common_lemmas))
    }
    
    return comparison_stats

def generate_interim_report(checkpoint_file, output_base, lang, nlp, min_frequency=3):
    """Generate an interim report from checkpoint data"""
    checkpoint_data = load_checkpoint(checkpoint_file)
    if not checkpoint_data:
        print("No checkpoint found, cannot generate interim report")
        return
    
    # Extract data from checkpoint
    lemma_counts = checkpoint_data['lemma_counts']
    total_words = checkpoint_data['total_words']
    processed_lines = checkpoint_data['processed_lines']
    chunk_num = checkpoint_data['chunk_num']
    
    # Get timing information if available
    start_time = checkpoint_data.get('start_time', None)
    last_update_time = checkpoint_data.get('last_update_time', None)
    
    # Calculate elapsed time if possible
    elapsed_time = None
    if start_time and last_update_time:
        elapsed_seconds = last_update_time - start_time
        elapsed_time = format_time(elapsed_seconds)
    
    # Create intermediate result
    result_all = create_result_dictionary(lemma_counts, total_words)
    result_filtered, stats = apply_filters(result_all, lemma_counts, total_words, processed_lines, min_frequency)
    
    # Sort lemmas by frequency for both unfiltered and filtered results
    sorted_all_lemmas = {}
    for lemma, data in sorted(result_all.items(), key=lambda x: x[1]['frequency'], reverse=True):
        sorted_all_lemmas[lemma] = data
        
    sorted_filtered_lemmas = {}
    for lemma, data in sorted(result_filtered.items(), key=lambda x: x[1]['frequency'], reverse=True):
        sorted_filtered_lemmas[lemma] = data
    
    # Create interim outputs
    interim_output_all = {
        "lemmas": sorted_all_lemmas,
        "statistics": {
            "total_words": total_words,
            "total_sentences": processed_lines,
            "unique_lemmas": len(sorted_all_lemmas)
        },
        "progress": {
            "processed_sentences": processed_lines,
            "processed_chunks": chunk_num,
            "total_words": total_words
        }
    }
    
    interim_output_filtered = {
        "lemmas": sorted_filtered_lemmas,
        "statistics": stats,
        "progress": {
            "processed_sentences": processed_lines,
            "processed_chunks": chunk_num,
            "total_words": total_words
        }
    }
    
    # Add timing information if available
    if elapsed_time:
        elapsed_seconds = last_update_time - start_time
        interim_output_all["progress"]["processing_time"] = elapsed_time
        interim_output_all["progress"]["processing_seconds"] = elapsed_seconds
        interim_output_filtered["progress"]["processing_time"] = elapsed_time
        interim_output_filtered["progress"]["processing_seconds"] = elapsed_seconds
        
        # Also add to stats
        stats['processing_time_seconds'] = elapsed_seconds
        stats['processing_time_formatted'] = elapsed_time
    
    # Generate filenames for interim reports
    current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
    interim_filename_all = f"{output_base}_interim_unfiltered_{current_datetime}.json"
    interim_filename_filtered = f"{output_base}_interim_filtered_{current_datetime}.json"
    
    # Save interim reports
    with open(interim_filename_all, 'w', encoding='utf-8') as f:
        json.dump(interim_output_all, f, indent=2, ensure_ascii=False)
    
    with open(interim_filename_filtered, 'w', encoding='utf-8') as f:
        json.dump(interim_output_filtered, f, indent=2, ensure_ascii=False)
    
    print(f"Unfiltered interim report saved to {interim_filename_all}")
    print(f"Filtered interim report saved to {interim_filename_filtered}")
    if elapsed_time:
        print(f"Total processing time so far: {elapsed_time}")
    
    # Generate wordfreq comparison if requested
    if lang:
        try:
            wordfreq_comparison1000 = compare_with_wordfreq(result_filtered, lang, nlp, top_n=1000)
            wordfreq_comparison2000 = compare_with_wordfreq(result_filtered, lang, nlp, top_n=2000)
            wordfreq_comparison5000 = compare_with_wordfreq(result_filtered, lang, nlp, top_n=5000)
            
            # Print wordfreq comparison
            print(f"\nWordfreq Comparison:")
            print(f"  Common lemmas found: {wordfreq_comparison1000['common_lemmas_count']}/{wordfreq_comparison1000['your_top_lemmas_count']}, {wordfreq_comparison2000['common_lemmas_count']}/{wordfreq_comparison2000['your_top_lemmas_count']}, {wordfreq_comparison5000['common_lemmas_count']}/{wordfreq_comparison5000['your_top_lemmas_count']}")
        except Exception as e:
            print(f"Error generating wordfreq comparison: {e}")
    
    return interim_filename_filtered, interim_filename_all

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process a large corpus file in chunks and create frequency lists")
    parser.add_argument("lang", help="Language code (e.g., 'es' for Spanish)")
    parser.add_argument("input_file", help="Path to the input TSV file")
    parser.add_argument("--format", choices=["tatoeba", "paracrawl"], default="tatoeba", 
                        help="Format of the input file: 'tatoeba' (id,lang,text) or 'paracrawl' (eng,target_lang)")
    parser.add_argument("--chunk-size", type=int, default=10000000, help="Number of sentences to process per chunk")
    parser.add_argument("--min-frequency", type=int, default=3, help="Minimum frequency threshold for lemmas")
    parser.add_argument("--resume", action="store_true", help="Resume from checkpoint if available")
    parser.add_argument("--generate-interim", action="store_true", help="Generate interim report from checkpoint without further processing")
    parser.add_argument("--max-lines", type=int, default=None, help="Maximum number of lines to process (for testing)")
    parser.add_argument("--workers", type=int, default=None, help="Number of worker processes for parallel processing")
    
    args = parser.parse_args()
    
    lang = args.lang
    input_file_path = args.input_file
    file_format = args.format
    chunk_size = args.chunk_size
    min_frequency = args.min_frequency
    max_lines = args.max_lines
    num_workers = args.workers

    # Adjust the output filename if we're only processing a subset
    input_base_name = os.path.splitext(os.path.basename(input_file_path))[0]
    file_suffix = f"_{file_format}"
    if max_lines:
        file_suffix += f"_first{max_lines}"
    
    checkpoint_file = f"{input_base_name}{file_suffix}_checkpoint.pkl"
    
    # Create a blank spaCy model for lemmatization
    print(f"Loading spaCy model for language: {lang}")
    nlp = spacy.blank(lang)
    nlp.add_pipe("lemmatizer", config={"mode": "lookup"})
    nlp.initialize()
    # edit lookup table to correct
    lemmatizer = nlp.get_pipe('lemmatizer')
    lemma_lookup = lemmatizer.lookups.get_table('lemma_lookup')
    lemma_lookup["para"] = ["para"]
    lemma_lookup["línea"] = ["línea"]
    lemma_lookup["líneas"] = ["línea"]
    lemma_lookup["segundo"] = ["segundo"]
    lemma_lookup["segunda"] = ["segundo"]
    lemma_lookup["segundos"] = ["segundo"]
    lemma_lookup["segundas"] = ["segundo"]
    lemma_lookup["estrella"] = ["estrella"]
    lemma_lookup["estrellas"] = ["estrella"]
    lemma_lookup["hemos"] = ["haber"]
    lemma_lookup["colores"] = ["color"]
    lemma_lookup["sitio"] = ["sitio"]
    lemma_lookup["así"] = ["así"]
    lemma_lookup["cerca"] = ["cerca"]
    lemma_lookup["mano"] = ["mano"]
    lemma_lookup["largo"] = ["largo"]
    lemma_lookup["cinco"] = ["cinco"]
    lemma_lookup["madera"] = ["madera"]
    lemma_lookup["tales"] = ["tal"]
    lemma_lookup["viaje"] = ["viaje"]
    lemma_lookup["vuelo"] = ["vuelo"]
    lemma_lookup["nos"] = ["nos"]
    lemma_lookup["lo"] = ["lo"]
    lemma_lookup["los"] = ["el"]
    lemma_lookup["las"] = ["el"]
    lemma_lookup["la"] = ["el"]
    lemma_lookup["casa"] = ["casa"]
    lemma_lookup["os"] = ["os"]
    lemma_lookup["sis"] = ["sis"]
    lemma_lookup["uno"] = ["uno"]
    lemma_lookup["aes"] = ["aes"]
    lemmatizer.cache = {}
    
    # Generate interim report if requested
    if args.generate_interim:
        interim_filtered_file, interim_all_file = generate_interim_report(
            checkpoint_file, f"{input_base_name}{file_suffix}", lang, nlp, min_frequency
        )
        print(f"Interim reports generated: {interim_filtered_file} (filtered) and {interim_all_file} (unfiltered)")
        exit(0)
    
    # Record start time
    start_time = time.time()
    
    # Process the file in chunks
    print(f"Starting to process {input_file_path} in {file_format} format, chunks of {chunk_size} sentences")
    if max_lines:
        print(f"Limited to first {max_lines} lines (test mode)")
    print(f"Start time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Delete checkpoint file if not resuming
    if os.path.exists(checkpoint_file) and not args.resume:
        print(f"Removing previous checkpoint file: {checkpoint_file}")
        os.remove(checkpoint_file)
    
    result_all, result_filtered, stats = process_sentences_in_chunks(
        input_file_path, 
        nlp, 
        chunk_size=chunk_size, 
        min_frequency=min_frequency,
        checkpoint_file=checkpoint_file,
        file_format=file_format,
        max_lines=max_lines,
        num_workers=num_workers
    )
    
    # Record end time and calculate total processing time
    end_time = time.time()
    processing_time = end_time - start_time
    formatted_time = format_time(processing_time)
    
    # Sort lemmas by frequency for both unfiltered and filtered results
    sorted_all_lemmas = {}
    for lemma, data in sorted(result_all.items(), key=lambda x: x[1]['frequency'], reverse=True):
        sorted_all_lemmas[lemma] = data
    
    sorted_filtered_lemmas = {}
    for lemma, data in sorted(result_filtered.items(), key=lambda x: x[1]['frequency'], reverse=True):
        sorted_filtered_lemmas[lemma] = data
    
    # Create output dictionaries with both unfiltered and filtered results
    output_all = {
        "lemmas": sorted_all_lemmas,
        "statistics": {
            "total_words": stats['total_words'],
            "total_sentences": stats['total_sentences'],
            "unique_lemmas": len(sorted_all_lemmas)
        },
        "processing_info": {
            "format": file_format,
            "start_time": datetime.fromtimestamp(start_time).strftime('%Y-%m-%d %H:%M:%S'),
            "end_time": datetime.fromtimestamp(end_time).strftime('%Y-%m-%d %H:%M:%S'),
            "total_processing_time": formatted_time,
            "total_processing_seconds": processing_time
        }
    }
    
    output_filtered = {
        "lemmas": sorted_filtered_lemmas,
        "statistics": stats,
        "processing_info": {
            "format": file_format,
            "start_time": datetime.fromtimestamp(start_time).strftime('%Y-%m-%d %H:%M:%S'),
            "end_time": datetime.fromtimestamp(end_time).strftime('%Y-%m-%d %H:%M:%S'),
            "total_processing_time": formatted_time,
            "total_processing_seconds": processing_time
        }
    }
    
    # Generate output filenames
    current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename_all = f"{input_base_name}{file_suffix}_lemmatized_freq_unfiltered_{current_datetime}.json"
    output_filename_filtered = f"{input_base_name}{file_suffix}_lemmatized_freq_filtered_{current_datetime}.json"
    
    # Save to files with the generated filenames
    with open(output_filename_all, 'w', encoding='utf-8') as f:
        json.dump(output_all, f, indent=2, ensure_ascii=False)
    
    with open(output_filename_filtered, 'w', encoding='utf-8') as f:
        json.dump(output_filtered, f, indent=2, ensure_ascii=False)
    
    # Compare with wordfreq, passing the spaCy model
    wordfreq_comparison1000 = compare_with_wordfreq(result_filtered, lang, nlp, top_n=1000)
    wordfreq_comparison2000 = compare_with_wordfreq(result_filtered, lang, nlp, top_n=2000)
    wordfreq_comparison5000 = compare_with_wordfreq(result_filtered, lang, nlp, top_n=5000)
    
    # Print statistics to console
    print(f"Processing complete.")
    print(f"Unfiltered results saved to {output_filename_all}")
    print(f"Filtered results saved to {output_filename_filtered}")
    print(f"Total processing time: {formatted_time}")
    
    if max_lines:
        print(f"TEST MODE: Processed only first {max_lines} lines of the file")
        
    print(f"Statistics:")
    print(f"  Total words: {stats['total_words']}")
    print(f"  Total sentences: {stats['total_sentences']}")
    print(f"  Unique lemmas before filtering: {stats['unique_lemmas_before_filtering']}")
    print(f"  Lemmas removed by frequency (min freq={stats['minimum_frequency_threshold']}): {stats['lemmas_removed_by_frequency']}")
    print(f"  Lemmas removed by digit filtering: {stats['lemmas_removed_by_nonword_filtering']}")
    print(f"  Lemmas removed by case check: {stats['lemmas_removed_by_case_check']}")
    print(f"  Total lemmas removed: {stats['total_lemmas_removed']}")
    print(f"  Final unique lemmas: {stats['unique_lemmas_after_all_filtering']}")
    
    # Calculate processing speed
    words_per_second = stats['total_words'] / processing_time if processing_time > 0 else 0
    sentences_per_second = stats['total_sentences'] / processing_time if processing_time > 0 else 0
    print(f"Processing speed: {words_per_second:.2f} words/sec, {sentences_per_second:.2f} sentences/sec")

    # Print wordfreq comparison
    print(f"\nWordfreq Comparison:")
    print(f"  Common lemmas found: {wordfreq_comparison1000['common_lemmas_count']}/{wordfreq_comparison1000['your_top_lemmas_count']}, {wordfreq_comparison2000['common_lemmas_count']}/{wordfreq_comparison2000['your_top_lemmas_count']}, {wordfreq_comparison5000['common_lemmas_count']}/{wordfreq_comparison5000['your_top_lemmas_count']}")