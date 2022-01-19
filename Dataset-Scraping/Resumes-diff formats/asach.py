import sys
import os,os.path
import glob
import pdfkit
import zipfile
import re
import xml.dom.minidom
import subprocess

pattern = "\d+"
path ="/Users/cosmos/Desktop/DeepBlue/BACKEND/File_conversion-OCR/Resumes/resume/x/"
files = os.listdir(path)

for file in files:
    pattern = re.compile(pattern)
    x=re.findall(pattern,file)
    if x :
        xml=file
        html=x[0]+".html"
        subprocess.call(['xsltproc',xml,'-o',html])

print= ("done!")



# dom = xml.dom.minidom.parseString(('resume/content.xml')) # or xml.dom.minidom.parseString(xml_string)
# #pretty_xml_as_string = dom.toprettyxml()
# #text_re = re.sub('>\n\s+([^<>\s].*?)\n\s+</',' ', str(pretty_xml_as_string ))    
# #prettyXml = re.sub('>\g<1></',' ', pretty_xml_as_string)

# text_re = re.compile('>\n\s+([^<>\s].*?)\n\s+</', re.DOTALL)    
# prettyXml = text_re.sub('>\g<1></', )
# print (prettyXml)
# print("done!")