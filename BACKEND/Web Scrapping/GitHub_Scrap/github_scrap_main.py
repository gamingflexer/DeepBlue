from selenium import webdriver
from selenium.webdriver.common.keys import Keys
PATH = 'D:\\Py New\\Py Softwares\\Selenium\\chromedriver.exe'
driver = webdriver.Chrome(PATH)

userURL = 'https://github.com/gamingflexer'
reposURL = userURL + '?tab=repositories'

