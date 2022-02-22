# !pip install transformers==3.1.0

from transformers import pipeline
classifier = pipeline("zero-shot-classification")  # try a smaller model

text1 = " "  # text to classify


def compare1(text):
    # classes to divide into or not
    candidate_labels = ["skills", "education", "experience"]
    output = classifier(text, candidate_labels, multi_class=False)
    return output


compare1(text1)
final_list = {output['sequence']: output['labels'][2]}

# take the output of final output as a comparsions
