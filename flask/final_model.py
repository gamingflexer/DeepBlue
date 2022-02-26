import spacy
from tika import parser
import numpy as np
import torch
from keras.preprocessing.sequence import pad_sequences
from transformers import BertForTokenClassification, BertTokenizerFast
import torch
from keras.preprocessing.sequence import pad_sequences
from pytorch_pretrained_bert import BertForTokenClassification, BertAdam, BertTokenizer, BertConfig
from keras.preprocessing.text import Tokenizer
import torch.nn.functional as F
import torch.nn as nn
import textract
from tika import parser


#text1 = ''

def both_model(text):
    # #BERT
    # MAX_LEN = 512
    # tags_vals = ['Empty', 'UNKNOWN', 'Email Address', 'Links', 'Skills', 'Graduation Year', 'College Name', 'Degree', 'Companies worked at', 'Location', 'Name', 'Designation', 'projects',
    #          'Years of Experience', 'Can Relocate to', 'Rewards and Achievements', 'Address', 'University', 'Relocate to', 'Certifications', 'state', 'links', 'College', 'training', 'des', 'abc']
    # tag2idx = {t: i for i, t in enumerate(tags_vals)}
    # idx2tag = {i: t for i, t in enumerate(tags_vals)}

    # spacy 700
    spacy_700 = []
    spacy_skills = []
    spacy_edu = []
    spacy_exp = []
    tagvalues_spacy = ['COLLEGE NAME', 'COMPANIES WORKED AT', 'DEGREE', 'DESIGNATION',
                       'EMAIL ADDRESS', 'SKILLS', 'YEARS OF EXPERIENCE', 'LOCATION', 'NAME  ', '']  # add more

    def spacy_700(text):
        model_spacy_path_all = 'C:\\WindowServer\\Flask-app\\v.1.0\\DeepBlue\\flask\\models\\700-old code'

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
        model_skills = 'C:\\WindowServer\\Flask-app\\v.1.0\\DeepBlue\\flask\\models\\Models-Seprate-700\\SKILL'

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
        model_edu = 'C:\\WindowServer\\Flask-app\\v.1.0\\DeepBlue\\flask\\models\\Models-Seprate-700\\EDU'

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
        model_exp = 'C:\\WindowServer\\Flask-app\\v.1.0\\DeepBlue\\flask\\models\\Models-Seprate-700\\EXP'

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

    # def process_resume2(text, tokenizer, max_len):
    #     tok = tokenizer.encode_plus(
    #         text, max_length=max_len, return_offsets_mapping=True)

    #     curr_sent = dict()

    #     padding_length = max_len - len(tok['input_ids'])

    #     curr_sent['input_ids'] = tok['input_ids'] + ([0] * padding_length)
    #     curr_sent['token_type_ids'] = tok['token_type_ids'] + \
    #         ([0] * padding_length)
    #     curr_sent['attention_mask'] = tok['attention_mask'] + \
    #         ([0] * padding_length)

    #     final_data = {
    #         'input_ids': torch.tensor(curr_sent['input_ids'], dtype=torch.long),
    #         'token_type_ids': torch.tensor(curr_sent['token_type_ids'], dtype=torch.long),
    #         'attention_mask': torch.tensor(curr_sent['attention_mask'], dtype=torch.long),
    #         'offset_mapping': tok['offset_mapping']
    #     }

    # def predict(model, tokenizer, idx2tag, tag2idx, device, text):
    #     model.eval()
    #     data = process_resume2(text, tokenizer, MAX_LEN)
    #     input_ids, input_mask = data['input_ids'].unsqueeze(
    #         0), data['attention_mask'].unsqueeze(0)
    #     labels = torch.tensor([1] * input_ids.size(0),
    #                           dtype=torch.long).unsqueeze(0)
    #     with torch.no_grad():
    #         outputs = model(
    #             input_ids,
    #             token_type_ids=None,
    #             attention_mask=input_mask,
    #             labels=labels,
    #         )
    #         tmp_eval_loss, logits = outputs[:2]

    #     logits = logits.cpu().detach().numpy()
    #     label_ids = np.argmax(logits, axis=2)

    #     entities = []
    #     for label_id, offset in zip(label_ids[0], data['offset_mapping']):
    #         curr_id = idx2tag[label_id]
    #         curr_start = offset[0]
    #         curr_end = offset[1]
    #         if curr_id != 'O':
    #             if len(entities) > 0 and entities[-1]['entity'] == curr_id and curr_start - entities[-1]['end'] in [0, 1]:
    #                 entities[-1]['end'] = curr_end
    #             else:
    #                 entities.append(
    #                     {'entity': curr_id, 'start': curr_start, 'end': curr_end})
    #     for ent in entities:
    #         ent['text'] = text[ent['start']:ent['end']]
    #     return entities

    # # convert
    # # tags_vals = ['Empty', 'UNKNOWN', 'Email Address', 'Links', 'Skills', 'Graduation Year', 'College Name', 'Degree', 'Companies worked at', 'Location', 'Name', 'Designation', 'projects',
    # #             'Years of Experience', 'Can Relocate to', 'Rewards and Achievements', 'Address', 'University', 'Relocate to', 'Certifications', 'state', 'links', 'College', 'training', 'des', 'abc']

    # entities1 = predict(MODEL, TOKENIZER, idx2tag, tag2idx, DEVICE, text)

    # main = []
    # for i in entities1:
    #     if i['entity'] in tags_vals:
    #         k = {i['entity']: i['text']}
    #         main = main + [k]

    # #save & clean
    # k = len(main)

    # # clean unnescaary values
    # r = []
    # for k in range(len(main)):
    #     for key, value in main[k].items():
    #         # print(value)
    #         if value == '':
    #             r = r + [k]
    #             # main.remove(main[k])
    #         elif value == ':':
    #             r = r + [k]
    #         elif value == ',':
    #             r = r + [k]
    #         elif value == 'Resume':
    #             r = r + [k]
    #         elif value == '.':
    #             r = r + [k]
    #         elif value == ' ':
    #             r = r + [k]
    #         elif value == '.':
    #             r = r + [k]
    #         elif value == '.':
    #             r = r + [k]

    # for rr in range(len(r)):
    #     main.remove(main[rr])
    # r.clear()

    # # clean unnesacry keys
    # for val in main:
    #     for key, value in val.items():
    #         if key == "Email Address":
    #             main.remove(val)
    #         elif key == "UNKNOWN":
    #             main.remove(val)
    #         elif key == "Empty":
    #             main.remove(val)

    # print(main)

    # functions
    spacy_700(text)
    spacy_edu(text)
    spacy_exp(text)
    spacy_skills(text)
    print(spacy_700)

    return spacy_700, spacy_skills, spacy_edu, spacy_exp
