# import web driver
from selenium import webdriver

# specifies the path to the chromedriver.exe
driver = webdriver.Chrome('D:\\Softwares\\chromedriver.exe')

# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com')

# locate email form by_class_name
username = driver.find_element_by_class_name('login-email')


# send_keys() to simulate key strokes
username.send_keys('adwaitg02@gmail.com')

# locate password form by_class_name
password = driver.find_element_by_class_name('login-password')

# send_keys() to simulate key strokes
password.send_keys('')

# locate submit button by_class_name
log_in_button = driver.find_element_by_class_name('login-submit')

# locate submit button by_class_id
log_in_button = driver.find_element_by_class_id('login submit-button')

# locate submit button by_xpath
log_in_button = driver.find_element_by_xpath('//*[@type="submit"]')

# .click() to mimic button click
log_in_button.click()