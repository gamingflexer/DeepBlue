# !pip install transformers==3.1.0

from transformers import pipeline
# try a smaller model

text1 = " "  # text to classify


def comparemain(text):

    classifier = pipeline("zero-shot-classification")
    # classes to divide into or not
    candidate_labels = ["skills", "education", "experience"]
    output = classifier(text, candidate_labels, multi_class=False)

    # last element of the dict
    final_list = {output['sequence']: output['labels'][2]}
    return final_list

# take the output of final output as a comparsions
