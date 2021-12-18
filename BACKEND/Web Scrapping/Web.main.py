import time

from selenium import webdriver

PATH = 'D:\\Py New\\Py Softwares\\Selenium\\chromedriver.exe'
driver = webdriver.Chrome(PATH)

email = 'idontknowimjustabirmd@gmail.com'
password = '12345Idontknow'

driver.get('https://www.linkedin.com/login')
time.sleep(10)