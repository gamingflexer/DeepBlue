import requests
from bs4 import BeautifulSoup
from selenium import webdriver

PATH = 'D:\\Softwares\\chromedriver.exe'
driver = webdriver.Chrome(PATH)

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

for index in range(len(j)):
    print(j[index], i[index])