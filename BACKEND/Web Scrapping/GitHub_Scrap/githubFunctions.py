from selenium import webdriver
from selenium.webdriver.common.by import By

#PATH = 'D:\\Py New\\Py Softwares\\Selenium\\chromedriver.exe'
#driver = webdriver.Chrome(PATH)


def getContributions(driver):
    text = driver.find_element(By.XPATH, '//h2[@class="f4 text-normal mb-2"]')
    print(text.text)
    return text.text

