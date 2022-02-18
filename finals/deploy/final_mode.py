import spacy
from tika import parser


# spacy 700
spacy_700 = {}
spacy_skills = {}
spacy_edu = {}
spacy_exp = {}
tagvalues_spacy = ['COLLEGE NAME', 'COMPANIES WORKED AT', 'DEGREE', 'DESIGNATION',
                   'EMAIL ADDRESS', 'SKILLS', 'YEARS OF EXPERIENCE', 'LOCATION', 'NAME  ', '']  # add more


def spacy_700(text):
    model_spacy_path_all = '700 old code'

    model_spacy = spacy.load(model_spacy_path_all)

    # predict
    doc = model_spacy(text)
    for ent in doc.ents:
        spacy_700.update({f'{ent.label_.upper():{4}}': ent.text})
    return spacy_700


#spacy - skills
def spacy_skills(text):
    model_skills = '700 old code'

    model_spacy = spacy.load(model_skills)

    # predict
    doc = model_spacy(text)
    for ent in doc.ents:
        spacy_skills.update({f'{ent.label_.upper():{4}}': ent.text})
    return spacy_skills


#spacy - Edu
def spacy_edu(text):
    model_edu = '700 old code'

    model_spacy = spacy.load(model_edu)

    # predict
    doc = model_spacy(text)
    for ent in doc.ents:
        spacy_edu.update({f'{ent.label_.upper():{4}}': ent.text})
    return spacy_edu

#spacy - Exp


def spacy_exp(text):
    model_exp = '700 old code'

    model_spacy = spacy.load(model_exp)

    # predict
    doc = model_spacy(text)
    for ent in doc.ents:
        spacy_exp.update({f'{ent.label_.upper():{4}}': ent.text})
    return spacy_exp


# clean spacy
# if same in any dict delete
# keyword - not possible in spacy
# after , remove for name
