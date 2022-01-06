import time

from _cffi_backend import string
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = 'D:\\Py New\\Py Softwares\\Selenium\\chromedriver.exe'
driver = webdriver.Chrome(PATH)
from githubFunctions import *

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

userURL = 'https://github.com/gamingflexer'
reposURL = userURL + '?tab=repositories'

html_content = requests.get(reposURL).text
soup = BeautifulSoup(html_content, 'html.parser')
star_count = soup.find_all('a', attrs={'class': 'Link--muted mr-3'})
repo_name = soup.find_all('p', attrs={'class': 'col-9 d-inline-block color-fg-muted mb-2 pr-4'})

i = []
j = []

for tag in star_count:
    i.append(tag.text.strip())

for tag in repo_name:
    j.append(tag.text.strip())

'''for k in range(len(j)):
    j[k] = j[k].split('\n')
    j[k] = [j[k] for j[k] in j[k] if j[k].strip()]
'''

for index in range(len(j)):
    print(j[index], i[index])
