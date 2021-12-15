from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

PATH = 'D:\\Py New\\Py Softwares\\Selenium\\chromedriver.exe'
driver = webdriver.Chrome(PATH)

for i in range(5):
    driver.get("https://www.linkedin.com/in/aju-palleri-248798a4/")
    driver.implicitly_wait(10)
    time.sleep(5)
    # driver.find_element(By.XPATH, '//button[@class="authwall-join-form__form-toggle--bottom form-toggle"]').click()
    # driver.maximize_window()
    # driver.find_element(By.XPATH, '//input[@id="username"]').send_keys