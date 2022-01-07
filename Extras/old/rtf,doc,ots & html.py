import os,os.path
import pdfkit


from socket import socket
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

driver = webdriver.Chrome(executable_path="/Users/cosmos/chromedriver", chrome_options=chrome_options)  


path = '/Users/cosmos/Desktop/DeepBlue/BACKEND/File conversion - OCR/Resumes/resume.odt'
url_ots = 'https://onlineconvertfree.com/convert/ots/'
url_rtf = 'https://online2pdf.com/convert-rtf-to-pdf'


class conversion():
    def __init__(self,path,url_ots,url_rtf):
        self.path = path
        self.url_ots = url_ots
        self.url_rtf = url_rtf
    
    def rtf2pdf(self):
        open = driver.get(url_rtf)
        file_path= "resume.ots"
        input_path = "/Users/cosmos/Desktop/DeepBlue/BACKEND/File_conversion-OCR/Resumes/"
        full_path = os.path.join(input_path,file_path)
        
        upload = driver.find_element_by_xpath('//*[@id="converter"]/div/div/button')
        upload.send_keys(full_path)
        
        convert = driver.find_element_by_name('Convert')
        convert.click()
        #time.sleep(6)
        
        
        print("done!")
    
    def doc2any(self):
        doc_url = 'https://www.ilovepdf.com/word_to_pdf'
        open = driver.get(doc_url)
        file_path= "resume.ots"
        input_path = "/Users/cosmos/Desktop/DeepBlue/BACKEND/File_conversion-OCR/Resumes/"
        full_path = os.path.join(input_path,file_path)
        
        upload = driver.find_element_by_xpath('//*[@id="converter"]/div/div/button')
        upload.send_keys(full_path)
        
        convert = driver.find_element_by_name('Convert')
        convert.click()
        #time.sleep(6)
        
        print("done!")
        
    def ots2pdf(self):
        open = driver.get(url_ots)
        file_path= "resume.ots"
        input_path = "/Users/cosmos/Desktop/DeepBlue/BACKEND/File_conversion-OCR/Resumes/"
        full_path = os.path.join(input_path,file_path)
        
        upload = driver.find_element_by_xpath('//*[@id="converter"]/div/div/button')
        upload.send_keys(full_path)
        
        convert = driver.find_element_by_name('Convert')
        convert.click()
        #time.sleep(6)
        
        print("done!")
        
    def html2pdf(self):
        with open(path) as f:
            pdfkit.from_file(f, 'resume4html.pdf')

        print("done!")
    

# Intialization
Start = conversion(path,url_ots,url_rtf)

#Start.rtf2pdf()
#Start.doc2any()
Start.ots2pdf()
#Start.html2pdf()
        
        