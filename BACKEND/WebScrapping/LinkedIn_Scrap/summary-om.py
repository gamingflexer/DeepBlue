import os
import sys
import time
from socket import socket
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import wget

list1 =['https://www.linkedin.com/in/aju-palleri-248798a4/','https://www.linkedin.com/in/sushopti-gawade-944111147/','https://www.linkedin.com/in/sourabh-r-kulkarni/']
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

driver = webdriver.Chrome(executable_path="/Users/cosmos/Downloads/chromedriver-1", chrome_options=chrome_options)  


# /html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[2]/div[3]/div/div/div/span[1]
# /html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[2]/div[3]/div/div/div/span[1]
# /html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[2]/div[3]/div/div/div/span[1]

# USERNAME AND PASSWORD
USERNAME = 'omsurve570@gmail.com'
PASSWORD = ''

# open linkedin.com
driver.get("https://www.linkedin.com/login")
driver.implicitly_wait(2)

# get Username , Password tag and send details and Hit Enter
driver.find_element(By.ID, "username").send_keys(USERNAME)
driver.find_element(By.ID, "password").send_keys(PASSWORD)
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# GOTO REQUIRED PERSON PROFILE
for i in range(0,2):
    driver.get(list1[i])    
    driver.implicitly_wait(2)
    #text = driver.find_elements_by_xpath("/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[2]/div[3]/div/div/div/span[1]")
    text = driver.find_element_by_xpath("")
    # price_content = text.get_attribute('innerHTML')
    print (text)
    
