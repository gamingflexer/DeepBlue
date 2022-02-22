import spacy
from tika import parser

text = ''
# spacy 700
spacy_700 = []
spacy_skills = []
spacy_edu = []
spacy_exp = []
tagvalues_spacy = ['COLLEGE NAME', 'COMPANIES WORKED AT', 'DEGREE', 'DESIGNATION',
                   'EMAIL ADDRESS', 'SKILLS', 'YEARS OF EXPERIENCE', 'LOCATION', 'NAME  ', '']  # add more


def spacy_700(text):
    model_spacy_path_all = '700 old code'

    model_spacy = spacy.load(model_spacy_path_all)

    # predict
    doc = model_spacy(text)
    for ent in doc.ents:
        if ent.label_.upper() in tagvalues_spacy:
            temp = {f'{ent.label_.upper():{4}}': [ent.text]}
            spacy_700 = spacy_700 + [temp]
    return spacy_700


#spacy - skills
def spacy_skills(text):
    model_skills = '700 old code'

    model_spacy = spacy.load(model_skills)

    # predict
    doc = model_spacy(text)
    for ent in doc.ents:
        if ent.label_.upper() in tagvalues_spacy:
            temp = {f'{ent.label_.upper():{4}}': [ent.text]}
            spacy_skills = spacy_skills + [temp]
    return spacy_skills


#spacy - Edu
def spacy_edu(text):
    model_edu = '700 old code'

    model_spacy = spacy.load(model_edu)

    # predict
    doc = model_spacy(text)
    for ent in doc.ents:
        if ent.label_.upper() in tagvalues_spacy:
            temp = {f'{ent.label_.upper():{4}}': [ent.text]}
            spacy_edu = spacy_edu + [temp]
    return spacy_edu


#spacy - Exp
def spacy_exp(text):
    model_exp = '700 old code'

    model_spacy = spacy.load(model_exp)

    # predict
    doc = model_spacy(text)
    for ent in doc.ents:
        if ent.label_.upper() in tagvalues_spacy:
            temp = {f'{ent.label_.upper():{4}}': [ent.text]}
            spacy_exp = spacy_exp + [temp]
    return spacy_exp


# clean spacy
# if same in any dict delete
# keyword - not possible in spacy
# after , remove for name


# BERT
# convert
# tags_vals = ['Empty', 'UNKNOWN', 'Email Address', 'Links', 'Skills', 'Graduation Year', 'College Name', 'Degree', 'Companies worked at', 'Location', 'Name', 'Designation', 'projects',
#             'Years of Experience', 'Can Relocate to', 'Rewards and Achievements', 'Address', 'University', 'Relocate to', 'Certifications', 'state', 'links', 'College', 'training', 'des', 'abc']

tags_vals = ["UNKNOWN", "Name", "Degree", "Skills", "College Name", "Email Address", "Designation",
             "Companies worked at", "Empty", "Graduation Year", "Years of Experience", "Location"]

entities1 = predict(MODEL, TOKENIZER, idx2tag, tag2idx, DEVICE, text)

main = []
for i in entities1:
    if i['entity'] in tags_vals:
        k = {i['entity']: i['text']}
        main = main + [k]


#save & clean
k = len(main)

# clean unnescaary values
r = []
for k in range(len(main)):
    for key, value in main[k].items():
        # print(value)
        if value == '':
            r = r + [k]
            # main.remove(main[k])
        elif value == ':':
            r = r + [k]
        elif value == ',':
            r = r + [k]
        elif value == 'Resume':
            r = r + [k]
        elif value == '.':
            r = r + [k]
        elif value == ' ':
            r = r + [k]
        elif value == '.':
            r = r + [k]
        elif value == '.':
            r = r + [k]

for rr in range(len(r)):
    main.remove(main[rr])
r.clear()

# clean unnesacry keys
for val in main:
    for key, value in val.items():
        if key == "Email Address":
            main.remove(val)
        elif key == "UNKNOWN":
            main.remove(val)
        elif key == "Empty":
            main.remove(val)


# functions
spacy_700(text)
spacy_edu(text)
spacy_exp(text)
spacy_skills(text)
