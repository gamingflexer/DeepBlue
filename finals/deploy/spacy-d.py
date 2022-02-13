import spacy
from tika import parser

#prediction - 1
# fname = '' #add a recuuring file function
# raw = parser.from_file(fname)
# text = raw['content']

# model paths
model_spacy_path_all = '700 old code'

model_spacy = spacy.load(model_spacy_path_all)

# predict
doc = model_spacy(raw['content'])
for ent in doc.ents:
    print(f'{ent.label_.upper():{30}} - {ent.text}')
