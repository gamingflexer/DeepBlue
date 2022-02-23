import spacy
from tika import parser

# model paths
#model_spacy_path_all = 'C:\\Users\\Yash\\OneDrive\\Desktop\\DeepBlue\\finals\\S\\700-old code'

#model_spacy = spacy.load(model_spacy_path_all)

# predict
def model(firstdata):
    model_spacy_path_all = 'C:\\Users\\Yash\\OneDrive\\Desktop\\DeepBlue\\finals\\S\\700-new-code- #loss-7159'

    model_spacy = spacy.load(model_spacy_path_all)
    doc = model_spacy(firstdata)
    for ent in doc.ents:
     print(f'{ent.label_.upper():{30}} - {ent.text}')
