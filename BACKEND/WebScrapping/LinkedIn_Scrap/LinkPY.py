# importing required libraries
from bs4 import BeautifulSoup
from selenium import webdriver

# specifies the path to the chromedriver.exe
driver = webdriver.Chrome("D:\\Softwares\\chromedriver.exe")  # mention chromedriver's path inside the quotes

# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com')
driver.implicitly_wait(1)

# locate email form by_class_name
username = driver.find_element_by_xpath('//*[@type="text"]')
# send_keys() to simulate key strokes
username.send_keys('adwaitg02@gmail.com')  # Your log-in Email

# locate password form by_class_name
password = driver.find_element_by_xpath('//*[@type="password"]')
# send_keys() to simulate key strokes
password.send_keys('')  # Your password

# cliking on log in button
log_in_button = driver.find_element_by_xpath('//*[@class="sign-in-form__submit-button"]')
log_in_button.click()
driver.implicitly_wait(1)  # driver will wait for 1 second to load everything completely

# Navigating to profile
link = 'https://www.linkedin.com/in/aju-palleri-248798a4/'  # Profile link which you want to scrape
driver.get(link)
driver.implicitly_wait(1)

src = driver.page_source
soup = BeautifulSoup(src, 'lxml')

# one of the ways to get link of current page (profile link)
profile_link = (driver.current_url)

# personal details    
name_div = soup.find('div', {'class': 'display-flex mt2'})

# name
try:
    name = name_div.find('li', {'class': 'inline t-24 t-black t-normal break-words'}).get_text().strip()
except IndexError:  # To ignore any kind of error
    name = 'NULL'
except AttributeError:
    name = 'NULL'

# location
try:
    location = name_div.find('li', {'class': 't-16 t-black t-normal inline-block'}).get_text().strip()
except IndexError:
    location = 'NULL'
except AttributeError:
    location = 'NULL'

# degree_level
try:
    degree_level = name_div.find('span', {'class': 'dist-value'}).get_text().strip()
except IndexError:
    degree_level = 'NULL'
except AttributeError:
    degree_level = 'NULL'

# No. of connections            
try:
    c_div = name_div.find('ul', {'class': 'pv-top-card--list pv-top-card--list-bullet mt1'})
    connections = c_div.find('span', {'class': 't-16 t-black t-normal'}).get_text().strip()
except IndexError:
    connections = 'NULL'
except AttributeError:
    connections = 'NULL'

# Professional Details
Experience_div = soup.find('div', {'class': 'pv-entity__summary-info pv-entity__summary-info--background-section'})

# recent positions
try:
    job_title = Experience_div.find('h3', {'class': 't-16 t-black t-bold'}).get_text().strip()
except IndexError:
    job_title = 'NULL'
except AttributeError:
    job_title = 'NULL'

# company name
try:
    company_name = soup.find('p', {'class': 'pv-entity__secondary-title t-14 t-black t-normal'}).get_text().strip()
except IndexError:
    company_name = 'NULL'
except AttributeError:
    company_name = 'NULL'

# experience
try:
    experience = soup.find('span', {'class': 'pv-entity__bullet-item-v2'}).get_text().strip()
except IndexError:
    experience = 'NULL'
except AttributeError:
    experience = 'NULL'

# saving outputs
output = ({'Name': name, 'Location': location, 'Degree Level': degree_level,
           'No. of Connections': connections, 'Postion': job_title, 'Company': company_name,
           'Experience': experience, 'Linked Link': profile_link})

# Export to excel
# df.to_excel("output.xlsx")