from nltk.metrics import edit_distance
import evaluate

def rouge(ground_truth,generated_output):
    rouge-scorer = evaluate.load('rouge')
    results = rouge-scorer.compute(predictions=generated_output,references=ground_truth,use_aggregator=True)
    return results

def exact_match(ground_truth,generated_output):
    if input_string == output_string: 
        return 1
    else: 
        return 0

def levenshtein(ground_truth,generated_output):
    results = edit_distance(ground_truth,generated_output)
    return results