from selenium import webdriver
import githubFunctions as gf
from selenium.webdriver.common.by import By
import time
import os
PATH = 'D:\\Py New\\Py Softwares\\Selenium\\chromedriver.exe'
driver = webdriver.Chrome(PATH)

userURL = 'https://github.com/gamingflexer'
reposURL = userURL + '?tab=repositories'

