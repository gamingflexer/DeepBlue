from selenium.webdriver.common.by import By


class Github:
    def getContributions(self, userURL, driver):
        driver.get(userURL)
        text = driver.find_element(By.XPATH, '//h2[@class="f4 text-normal mb-2"]')
        print(text.text)
        return text.text

    def getUserRepos(self, repoURL, driver):
        driver.get(repoURL)
        repos = driver.find_element(By.ID, 'user-repositories-list')
        #print(repos.text)
        #driver.quit()
        value = driver.find_element_by_xpath('/html/body/div[4]/main/div[2]/div/div[2]/div[2]/div/div[2]/ul/li[1]/div[1]/div[3]/a/text()')
        print(value)
        return repos.text
