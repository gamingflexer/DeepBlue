from selenium import webdriver
from linkedin_scraper import Person,actions
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


PATH = 'D:\\Py New\\Py Softwares\\Selenium\\chromedriver.exe'
driver = webdriver.Chrome(PATH)

email = 'idontknowimjustabirmd@gmail.com'
password = '12345Idontknow'

driver.get('https://www.linkedin.com/login')
time.sleep(10)