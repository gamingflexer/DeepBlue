import spacy
from tika import parser

text = ''
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


# BERT
entities1 = predict(MODEL, TOKENIZER, idx2tag, tag2idx, DEVICE, text)

# convert
# tags_vals = ['Empty', 'UNKNOWN', 'Email Address', 'Links', 'Skills', 'Graduation Year', 'College Name', 'Degree', 'Companies worked at', 'Location', 'Name', 'Designation', 'projects',
#             'Years of Experience', 'Can Relocate to', 'Rewards and Achievements', 'Address', 'University', 'Relocate to', 'Certifications', 'state', 'links', 'College', 'training', 'des', 'abc']

tags_vals = ["UNKNOWN", "Name", "Degree", "Skills", "College Name", "Email Address", "Designation",
             "Companies worked at", "Empty", "Graduation Year", "Years of Experience", "Location"]

main = []
for i in entities1:
    if i['entity'] in tags_vals:
        k = {i['entity']: i['text']}
        main = main + [k]

main = main + [{'Empty': 'Resume'}]
print(main)


#save & clean
k = len(main)
#save and clean

k = len(main)

for i in range(0, k):
    for m in range(0, 26):
        val = tags_vals[m]
        if val in main[i].keys():
            if main[i][val] != '':
                print(main[i])


# functions
spacy_700(text)
spacy_edu(text)
spacy_exp(text)
spacy_skills(text)
