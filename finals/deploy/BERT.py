# Importing required Libraries
import textract
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
import re
from tika import parser


def bert(text):
    tags_vals = ['Empty', 'UNKNOWN', 'Email Address', 'Links', 'Skills', 'Graduation Year', 'College Name', 'Degree', 'Companies worked at', 'Location', 'Name', 'Designation', 'projects',
                 'Years of Experience', 'Can Relocate to', 'Rewards and Achievements', 'Address', 'University', 'Relocate to', 'Certifications', 'state', 'links', 'College', 'training', 'des', 'abc']
    tag2idx = {t: i for i, t in enumerate(tags_vals)}
    idx2tag = {i: t for i, t in enumerate(tags_vals)}

    # config
    MAX_LEN = 512  # 512 #300

    device = torch.device("cpu")
    # device = torch.device("cuda")
    # n_gpu = torch.cuda.device_count()
    # torch.cuda.get_device_name(0)

    # Load
    from transformers import BertForTokenClassification, BertTokenizerFast
    import torch
    from keras.preprocessing.text import Tokenizer

    # use transformers of choice

    MAX_LEN = 512
    EPOCHS = 6
    DEVICE = torch.device("cuda")
    MODEL_PATH = '/content/drive/MyDrive/Colab Notebooks/DeepBlue/bert-large-uncased'
    STATE_DICT = torch.load(
        '/content/drive/MyDrive/Colab Notebooks/DeepBlue/TYPE 2/uncased/new/large-uncased-bert-700-512-basedir.pth', map_location=DEVICE)
    #TOKENIZER = BertTokenizerFast('/content/drive/MyDrive/Colab Notebooks/DeepBlue/bert-large-uncased/vocab.txt', lowercase=True)
    TOKENIZER = Tokenizer(num_words=20000)  # SIMPLE
    MODEL = BertForTokenClassification.from_pretrained(
        MODEL_PATH, state_dict=STATE_DICT['model_state_dict'], num_labels=26)

    # Prediction code

    def process_resume2(text, tokenizer, max_len):
        tok = tokenizer.encode_plus(
            text, max_length=max_len, return_offsets_mapping=True)

        curr_sent = dict()

        padding_length = max_len - len(tok['input_ids'])

        curr_sent['input_ids'] = tok['input_ids'] + ([0] * padding_length)
        curr_sent['token_type_ids'] = tok['token_type_ids'] + \
            ([0] * padding_length)
        curr_sent['attention_mask'] = tok['attention_mask'] + \
            ([0] * padding_length)

        final_data = {
            'input_ids': torch.tensor(curr_sent['input_ids'], dtype=torch.long),
            'token_type_ids': torch.tensor(curr_sent['token_type_ids'], dtype=torch.long),
            'attention_mask': torch.tensor(curr_sent['attention_mask'], dtype=torch.long),
            'offset_mapping': tok['offset_mapping']
        }

        return final_data

    def predict(model, tokenizer, idx2tag, tag2idx, device, text):
        model.eval()
        data = process_resume2(text, tokenizer, MAX_LEN)
        input_ids, input_mask = data['input_ids'].unsqueeze(
            0), data['attention_mask'].unsqueeze(0)
        labels = torch.tensor([1] * input_ids.size(0),
                              dtype=torch.long).unsqueeze(0)
        with torch.no_grad():
            outputs = model(
                input_ids,
                token_type_ids=None,
                attention_mask=input_mask,
                labels=labels,
            )
            tmp_eval_loss, logits = outputs[:2]

        logits = logits.cpu().detach().numpy()
        label_ids = np.argmax(logits, axis=2)

        entities = []
        for label_id, offset in zip(label_ids[0], data['offset_mapping']):
            curr_id = idx2tag[label_id]
            curr_start = offset[0]
            curr_end = offset[1]
            if curr_id != 'O':
                if len(entities) > 0 and entities[-1]['entity'] == curr_id and curr_start - entities[-1]['end'] in [0, 1]:
                    entities[-1]['end'] = curr_end
                else:
                    entities.append(
                        {'entity': curr_id, 'start': curr_start, 'end': curr_end})
        for ent in entities:
            ent['text'] = text[ent['start']:ent['end']]
        return entities
    return

# #prediction - 1
# fname = '' #add a recuuring file function

# raw = parser.from_file(fname)
# text = raw['content']

# #prediction - 2 # take from the database and pass it here
# entities1 = predict(MODEL, TOKENIZER, idx2tag, tag2idx, DEVICE, text)

# for i in entities1:
#     print(i['entity'], '-', i['text']) #display them in the list
