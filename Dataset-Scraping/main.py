import os
import sys
import time
import csv
from pandas.io.pytables import Table
import wget
import pandas as pd
import lxml

from bs4 import BeautifulSoup


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

url = "https://demos.pragnakalp.com/resume-parser/"
#url = "https://www.linkedin.com/"

class praglap():
    def __init__(self,url):
        self.url = url
        
    def upload_files(self):
        open = driver.get(url)
        my_path = os.getcwd()
        file_path= "ajjubhai.pdf"
        input_path = "/Users/cosmos/Desktop/DeepBlue/Dataset-Scraping/"
        full_path = os.path.join(input_path,file_path)
        
        upload = driver.find_element_by_xpath('/html/body/div/div/div/form/div[1]/input')
        upload.send_keys(full_path)
        
        parse = driver.find_element_by_xpath('/html/body/div/div/div/form/div[3]/button')
        parse.click()
        time.sleep(6)
        
    def extract_data(self):
        #driver.maximize_window()
        r = 1
        templist = []
        
        while(1):
            try:
                scrape= driver.find_element_by_xpath('/html/body/div/div/div/div[3]/table/tbody/tr[2]/td[2]/span').text
                Table_dict = {'Scrape':scrape}
                templist.append(Table_dict)
                df = pd.DataFrame(templist)
                r+=1
                break
                
                
            except NoSuchElementException:
                pass
        
        df.to_csv('data.csv')
        
    def bs4(self):
        soup = BeautifulSoup(driver.page_source, 'lxml')
        tables = soup.find_all('table')
        data_tb= pd.read_html(str(tables))
        print(f'Total Tables : {len(data_tb)}')
        print(data_tb)
        templist_bs4 = []
        templist_bs4.append(data_tb)
        df2 = pd.DataFrame(templist_bs4)
        df2.to_json('data2.json')
        driver.delete_all_cookies()
        

      
           
    def newTab(self):
       driver.get(url)
       driver.execute_script("window.open('https://www.youtube.com/', '_blank');");
       time.sleep(5)
       


Start = praglap(url)
Start.upload_files()
#Start.extract_data()
Start.bs4()

#Start.newTab()