import sys, fitz
fname = '/Users/cosmos/Desktop/DeepBlue/BACKEND/File_conversion-OCR/Resumes/resume_linkdien.pdf'
doc = fitz.open(fname)
text = ""
for page in doc:
    text = text + str(page.getText())
tx = " ".join(text.split('\n'))
print(tx)