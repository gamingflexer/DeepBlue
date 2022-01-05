from docx2pdf import convert
#import cv2
from fpdf import FPDF
from PIL import Image
import pytesseract

#function to accept file path from user
print = ( '################# ENTER FILE TO CONVERT INTO PDF ####################')
filename = str(input())

#filename = "CG experiments.docx"
x = filename.rfind(".")
extension=filename[x+1:]

#docx - pdf
if(extension == "docx"):
    convert(filename, r"filepdf100.pdf")
#image - pdf
elif(extension=="png" or extension=="jpg"):
    file = open("imgtotext99.txt", "w")
    pdf = FPDF()
    pdf.add_page()
    fpdf = FPDF('L', 'cm', (500, 550))
    pdf.set_font("Arial", size=12)
    pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
    img = cv2.imread(filename)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    print(pytesseract.image_to_string(img))

    file.write(pytesseract.image_to_string(img))

    cv2.imshow('Result', img)

    file.close()
    f = open("imgtotext99.txt", 'r')
    for x in f:
        pdf.cell(200, 10, txt=x, ln=1, align='L')

    pdf.output("imgtopdf100.pdf")
 #  cv2.waitKey(0)
 #text - pdf
elif(extension=="txt"):
     pdf = FPDF()
     pdf.add_page()
     fpdf = FPDF('L', 'cm', (500, 550))
     pdf.set_font("Arial", size=11)
     f = open("example.txt", 'r')
     for x in f:
         pdf.cell(200, 10, txt=x, ln=1, align='L')

     pdf.output("txttoppdf99.pdf")