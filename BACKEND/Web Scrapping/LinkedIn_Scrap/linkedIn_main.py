from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

PATH = 'D:\\Py New\\Py Softwares\\Selenium\\chromedriver.exe'

# USERNAME AND PASSWORD

USERNAME = ''
PASSWORD = ''

# open linkedin.com
driver = webdriver.Chrome(PATH)
driver.get("https://www.linkedin.com/login")
driver.implicitly_wait(2)

# get username , password tag
driver.find_element(By.ID, "username").send_keys(USERNAME)
driver.find_element(By.ID, "password").send_keys(PASSWORD)

# Cilck on sign in button
driver.find_element(By.XPATH, "//button[@type='submit']").click()

linkOfTab = 'https://www.github.com/'
# Open New Tab
driver.execute_script("window.open('"+linkOfTab+"','_blank');")

driver.find_element(By.CLASS_NAME, 'search-global-typeahead__input always-show-placeholder').send_keys(Keys.CONTROL + 't')

"""
    To Switch Tabs by Index Number
    driver.switch_to.window(driver.window_handles[0])
"""


