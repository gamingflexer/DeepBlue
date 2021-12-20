from selenium import webdriver
import githubFunctions as gf
from selenium.webdriver.common.by import By
import time
import os

PATH = 'D:\\Py New\\Py Softwares\\Selenium\\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get('https://github.com/gamingflexer')

gf.getContributions(driver)

driver.quit()