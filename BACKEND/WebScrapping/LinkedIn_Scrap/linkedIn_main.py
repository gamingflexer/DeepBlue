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

firstBox = driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/div/div[2]/div/div/main/section[2]').text
print('First Box :' + firstBox)
f = open("blocks/1b.txt", "a")
f.write(firstBox)
f.close()

secondBox = driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/div/div[2]/div/div/main/section[3]').text
print('Second Box :' + secondBox)
f = open("blocks/2b.txt", "a")
f.write(secondBox)
f.close()

thirdBox = driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/div/div[2]/div/div/main/section[4]').text
print('Third Box :' + thirdBox)
f = open("blocks/3b.txt", "a")
f.write(thirdBox)
f.close()

fourthBox = driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/div/div[2]/div/div/main/section[5]').text
print('Fourth Box :' + fourthBox)
f = open("blocks/4b.txt", "a")
f.write(fourthBox)
f.close()

fifthBox = driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/div/div[2]/div/div/main/section[6]').text
print('Fifth Box :' + fifthBox)
f = open("blocks/5b.txt", "a")
f.write(fifthBox)
f.close()

sixthBox = driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/div/div[2]/div/div/main/section[7]').text
print('Sixth Box :' + sixthBox)
f = open("blocks/6b.txt", "a")
f.write(sixthBox)
f.close()

seventhBox = driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/div/div[2]/div/div/main/section[8]').text
print('Seventh Box :' + seventhBox)
f = open("blocks/7b.txt", "a")
f.write(seventhBox)
f.close()


class Link:

    def getAbout(self):
        link_About = soup.find_all('div', {"class": "display-flex ph5 pv3"})
        about = ''
        for ab in link_About:
            about = ab.text
            print(ab.text)

        return about

    def currentWork(self):
        current_work = soup.find_all('div', {"class": "text-body-medium break-words"})
        for data in current_work:
            print(data.text)
            return data.text


driver.quit()
