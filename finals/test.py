# from asyncio.format_helpers import extract_stack
# import re
# # text = 'Hello this is yash wakekar yashwakekar231@gmail.com with  https://stackoverflow.com/questions/3392354/append-values-to-a-set-in-python    www.google.com jaywant patil bluiding plot no 127 near hanuman mandir shiravane gaon nerul navi mumbai 400706'
# https://drive.google.com/file/d/1Z3By3mW0Lp1WkxCnd_y5x9-w_m039tWD/view?usp=sharing

# # def url_grabber(text):
# #     url = ["", ""]
# #     for i in range(0, 2):
# #         url[i] = re.search("(?P<url>https?://[^\s]+)", text"{i}").group("url")
# #         name = "text" + "{i}"
# #         name = text.replace(url[0], "")
# #     return url


# # x = url_grabber(text)

# # print(x)

# links = ['https://www.linkedin.com/in/aju-palleri-248798a4/',
#          'https://github.com/gamingflexer/DeepBlue', 'https://github.com/', 'new.com']

# git_link = []
# lid_link = []
# extras = []


# # def link_seprator(links):
# # for i in range(len(links)):
# #     k = re.search(r'\bwww.linkedin.com\b', links[i]).group(0)
# #     print(k)

# for i in range(len(links)):
#     if 'linkedin' in links[i]:
#         lid_link = lid_link + [links[i]]
#     elif 'github' in links[i]:
#         git_link = git_link + [links[i]]
#     else:
#         extras = extras + [links[i]]

# print(lid_link)
# print(git_link)
# print(extras)

# # regex = re.compile("linkedin+\w*")
# # match_object = regex.findall(links[0])
# # prin


state_list = ["andhra Pradesh", "arunachal pradesh ", "assam", "Bihar", "chhattisgarh", "goa", "gujarat", "haryana", "himachal pradesh", "jammu and kashmir", "jharkhand", "karnataka", "kerala", "madhya pradesh", "maharashtra", "manipur", "meghalaya", "mizoram", "nagaland", "odisha",
              "punjab", "rajasthan", "sikkim", "tamil nadu", "telangana", "tripura", "uttar pradesh", "uttarakhand", "west bengal", "andaman and nicobar islands", "chandigarh", "dadra and nagar haveli", "daman and diu", "lakshadweep", "delhi", "puducherry"]

state = []
text = 'hi i am om i am from Punjab and tamil nadu'
text = text.lower()
text2 = text.split()
for t in text2:
    if t == 'tamil':
        state = state + ['tamil nadu']
    elif t == 'andhra':
        state = state + ['andhra Pradesh']
    elif t == 'arunachal':
        state = state + ['arunachal pradesh']
    elif t == 'uttar':
        state = state + ['uttar pradesh']
    elif t == 'west':
        state = state + ['west bengal']
    elif t == 'himachal':
        state = state + ['himachal pradesh']
    elif t == 'jammu':
        state = state + ['jammu and kashmir']
    elif t == 'dadra':
        state = state + ['dadra and nagar haveli']
    elif t == 'daman':
        state = state + ['daman and diu']
    elif t == 'madhya':
        state = state + ['madhya pradesh']
    for s in state_list:
        if t == s:
            state = state + [s]

print(state)


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


tags_vals = ["UNKNOWN", "O", "Name", "Degree", "Skills", "College Name", "Email Address",
             "Designation", "Companies worked at", "Graduation Year", "Years of Experience", "Location"]
tag2idx = {t: i for i, t in enumerate(tags_vals)}
idx2tag = {i: t for i, t in enumerate(tags_vals)}


def predict(model, tokenizer, idx2tag, tag2idx, device, test_resume):
    model.eval()
    data = process_resume2(test_resume, tokenizer, MAX_LEN)
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
        ent['text'] = test_resume[ent['start']:ent['end']]
    return entities
