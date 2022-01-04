import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

PATH = 'D:\\Py New\\Py Softwares\\Selenium\\chromedriver.exe'
driver = webdriver.Chrome(PATH)

email = 'idontknowimjustabirmd@gmail.com'
password = '12345Idontknow'
driver.get('https://www.linkedin.com/login')
driver.maximize_window()
driver.implicitly_wait(4)

driver.find_element_by_id('username').send_keys(email)
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
driver.find_element(By.ID, 'password').send_keys(password)
time.sleep(2)
driver.find_element(By.CLASS_NAME, 'login__form_action_container ').click()

time.sleep(10)
driver.quit()