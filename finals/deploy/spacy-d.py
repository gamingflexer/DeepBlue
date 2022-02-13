import spacy
from tika import parser

# model paths
model_spacy_path_all = '700 old code'

model_spacy = spacy.load(model_spacy_path_all)

# predict
doc = model_spacy('first data')
for ent in doc.ents:
    print(f'{ent.label_.upper():{30}} - {ent.text}')
