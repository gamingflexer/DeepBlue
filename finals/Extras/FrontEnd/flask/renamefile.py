import os
file1 = "C:\\Users\\Yash\\PycharmProjects\\flask\\static\\files\\SEAT_NUMBER_SEMIII_C_SCHEME_DEC_2021_COMP.pdf"
x = file1.rindex("\\")
y = file1.index(".")
val = 1
num = str(val)
val += val
path = file1[:x+1]+"resume"+num+file1[y:]
os.rename(file1, path)

