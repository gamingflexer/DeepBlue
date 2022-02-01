from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import re
import xml.etree.ElementTree as ET

# PATH to chrome driver
PATH = 'D:\\Softwares\\chromedriver.exe'
ser = Service(PATH)
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

# USERNAME AND PASSWORD
USERNAME = 'adwaitg02@gmail.com'
PASSWORD = ''

# open linkedin.com
driver.get("https://www.linkedin.com/login")
driver.implicitly_wait(2)

# get Username , Password tag and send details and Hit Enter
driver.find_element(By.ID, "username").send_keys(USERNAME)
driver.find_element(By.ID, "password").send_keys(PASSWORD)
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# GOTO REQUIRED PERSON PROFILE
driver.get('https://www.linkedin.com/in/aju-palleri-248798a4/')

pagesource = driver.page_source
soup = BeautifulSoup(pagesource, "html.parser")
aboutWithTags = soup.find('div', attrs={'class', 'inline-show-more-text inline-show-more-text--is-collapsed'})

"""def remove_html_markup(s):
    tag = False
    quote = False
    out = ""

    for c in s:
            if c == '<' and not quote:
                tag = True
            elif c == '>' and not quote:
                tag = False
            elif (c == '"' or c == "'") and tag:
                quote = not quote
            elif not tag:
                out = out + c

    return out
"""


def remove_html_tags(text):
    """Remove html tags from a string"""
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)


tagsWithout = remove_html_tags(aboutWithTags)
print(tagsWithout)

"""
    To Switch Tabs by Index Number
    driver.switch_to.window(driver.window_handles[0])
"""
