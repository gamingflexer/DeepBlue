for i in range(9):
    print(i + 1)
    f = open(str(i + 1) + "b.txt", "w")
    f.write('')
    f.close()

for i in range(9):
    print(i + 1)
    f = open(str(i + 1) + "bclean.txt", "w")
    f.write('')
    f.close()

