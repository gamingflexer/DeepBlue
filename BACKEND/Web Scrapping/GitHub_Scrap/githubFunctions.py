from selenium.webdriver.common.by import By

def getContributions(userURL, driver):
    driver.get(userURL)
    text = driver.find_element(By.XPATH, '//h2[@class="f4 text-normal mb-2"]')
    print(text.text)
    driver.quit()
    return text.text


def getUserRepos(repoURL, driver):
    driver.get(repoURL)
    repos = driver.find_element(By.ID, 'user-repositories-list')
    print(repos.text)
    driver.quit()
    return repos.text


