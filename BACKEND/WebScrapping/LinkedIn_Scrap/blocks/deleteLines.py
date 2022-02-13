bad_words = ['Highlights', 'Message']

for i in range(9):
    with open(str(i+1) + 'b.txt') as oldfile, open(str(i+1) + 'bclean.txt', 'w') as newfile:
        for line in oldfile:
            if not any(bad_word in line for bad_word in bad_words):
                newfile.write(line)
