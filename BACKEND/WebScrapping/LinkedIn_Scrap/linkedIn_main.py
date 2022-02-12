from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

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



def getAbout():
    spans = soup.find_all('span', "visually-hidden")
    dataArray = []
    for span in spans:
        dataArray.append(span.text)

    print(dataArray[7])
    print(dataArray[8])

    newDataArray = [dataArray[7],dataArray[8]]

    return newDataArray







"""
    To Switch Tabs by Index Number
    driver.switch_to.window(driver.window_handles[0])
"""

driver.quit()