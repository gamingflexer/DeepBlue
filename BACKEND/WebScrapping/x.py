password = "lucario123"











from linkedin_scraper import Person, actions
from selenium import webdriver
driver = webdriver.Chrome(executable_path=r"/Users/cosmos/chromedriver")
email = "omsurve570@gmail.com"
actions.login(driver, email, password) # if email and password isnt given, it'll prompt in terminal
person = Person("https://www.linkedin.com/in/sushopti-gawade-944111147/", driver=driver)

print("Person: " + person.name) #working
print(person.about) #not empty list
print(person.accomplishments) #not empty list
print(person.educations)
print(person.experiences)
print(person.interests)
print(person.contacts)



