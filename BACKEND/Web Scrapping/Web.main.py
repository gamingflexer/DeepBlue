import time
import

from selenium import webdriver
from selenium.webdriver.common.by import By

PATH = 'D:\\Py New\\Py Softwares\\Selenium\\chromedriver.exe'
driver = webdriver.Chrome(PATH)

email = 'idontknowimjustabirmd@gmail.com'
password = '12345Idontknow'

driver.get('https://www.linkedin.com/login')
driver.maximize_window()
usernameField = driver.find_element(By.ID, 'username')
passwordField = driver.find_element(By.ID, 'password')
time.sleep(10)