from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

PATH = 'D:\\Py New\\Py Softwares\\Selenium\\chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.get("https://www.linkedin.com")
driver.implicitly_wait(10)
#driver.find_element(By.XPATH, '//button[@class="authwall-join-form__form-toggle--bottom form-toggle"]').click()
#driver.maximize_window()
time.sleep(3)
