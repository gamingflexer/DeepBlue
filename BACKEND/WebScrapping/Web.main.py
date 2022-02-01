from linkedin_scraper import Person, actions
from selenium import webdriver
driver = webdriver.Chrome(executable_path=r"D:\\Softwares\\chromedriver.exe")
email = "adwaitg02@gmail.com"
password = ""
actions.login(driver, email, password) # if email and password isnt given, it'll prompt in terminal

person = Person("https://www.linkedin.com/in/aju-palleri-248798a4/", driver=driver)
print("Person: " + person.name)
print(person.about)
print(person.accomplishments)
print(person.educations)
print(person.experiences)















