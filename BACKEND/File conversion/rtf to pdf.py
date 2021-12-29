import sys
import os,os.path
import comtypes.client

wdFormatPDF = 17

input_dir = r"C:\Users\COSMOS\Desktop\DEEPBLUE\Doptech\BACKEND\File conversion\resume.rtf"
output_dir = r"C:\Users\COSMOS\Desktop\DEEPBLUE\Doptech\BACKEND\File conversion"

for subdir, dirs, files in os.walk(input_dir):
    for file in files:
        in_file = os.path.join(subdir, file)
        output_file = file.split('.')[0]
        out_file = output_dir+output_file+'.pdf'
        word = comtypes.client.CreateObject('Word.Application')

        doc = word.Documents.Open(in_file)
        doc.SaveAs(out_file, FileFormat=wdFormatPDF)
        doc.Close()
        word.Quit()
