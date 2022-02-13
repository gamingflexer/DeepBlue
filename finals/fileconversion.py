from docx2pdf import convert
import cv2
from fpdf import FPDF
from PIL import Image
import pytesseract
import pdfkit
import os,os.path
import textract


#function to accept file path from user
print = ( '################# ENTER FILE TO CONVERT INTO PDF ####################')
filename = str(input())

#filename = "CG experiments.docx"
x = filename.rfind(".")
extension=filename[x+1:]

#docx - pdf #docx2pdf
if(extension == "docx"):
    convert(filename, r"filepdf100.pdf")
    
#image - pdf
elif(extension=="png" or extension=="jpg" or extension=="jpeg"):
    file = open(filename, "w")
    pdf = FPDF()
    pdf.add_page()
    fpdf = FPDF('L', 'cm', (500, 550))
    pdf.set_font("Arial", size=12)
    #change file path accordingly
    pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
    img = cv2.imread(filename)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    print(pytesseract.image_to_string(img))

    file.write(pytesseract.image_to_string(img))

    cv2.imshow('Result', img)

    file.close()
    f = open(filename, 'r')
    for x in f:
        pdf.cell(200, 10, txt=x, ln=1, align='L')

    pdf.output("{filename}"".pdf")
 #  cv2.waitKey(0)
 #text - pdf
elif(extension=="txt"):
     pdf = FPDF()
     pdf.add_page()
     fpdf = FPDF('L', 'cm', (500, 550))
     pdf.set_font("Arial", size=11)
     f = open(filename, 'r')
     for x in f:
         pdf.cell(200, 10, txt=x, ln=1, align='L')

     pdf.output("{filename}"".pdf")
     
elif (extension=="html"):
    with open(filename) as f:
        pdfkit.from_file(f, 'resume4html.pdf')
    
    #save function to make 
    
elif (extension == "rtf"):
    text = textract.process(filename)
    print(text)
    
elif (extension == "odt"):
    text = textract.process(filename)
    print(text)
    
elif (extension == "doc"):
    text = textract.process(filename)
    print(text)



#add save function in each of it 