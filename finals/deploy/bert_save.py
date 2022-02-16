entities1 = predict(MODEL, TOKENIZER, idx2tag, tag2idx, DEVICE, text)

# convert
tags_vals = ['Empty', 'UNKNOWN', 'Email Address', 'Links', 'Skills', 'Graduation Year', 'College Name', 'Degree', 'Companies worked at', 'Location', 'Name', 'Designation', 'projects',
             'Years of Experience', 'Can Relocate to', 'Rewards and Achievements', 'Address', 'University', 'Relocate to', 'Certifications', 'state', 'links', 'College', 'training', 'des', 'abc']
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
