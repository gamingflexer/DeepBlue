import spacy
from tika import parser

#prediction - 1
fname = '' #add a recuuring file function
raw = parser.from_file(fname)
text = raw['content']

#model paths
model_spacy_path_edu = ''
model_spacy_path_exp = ''
model_spacy_path_skill = ''


model_spacy_edu = spacy.load(model_spacy_path_edu)
model_spacy_exp = spacy.load(model_spacy_path_exp)
model_spacy_skill = spacy.load(model_spacy_path_skill)

#predict - education
doc = model_spacy_edu(raw['content'])
for ent in doc.ents:
    print(f'{ent.label_.upper():{30}} - {ent.text}')
    

#predict - experience
doc = model_spacy_exp(raw['content'])
for ent in doc.ents:
    print(f'{ent.label_.upper():{30}} - {ent.text}')
    
#predict - skills
doc = model_spacy_skill(raw['content'])
for ent in doc.ents:
    print(f'{ent.label_.upper():{30}} - {ent.text}')
    
