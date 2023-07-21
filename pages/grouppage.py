from selenium.webdriver.common.by import By

class FacebookGroupPage:
    def __init__(self, driver):
        self.driver = driver

    
    def assert_element_present(driver, by, value):
        try:
            driver.find_element(by, value)
            print("Element is present on the page.")
        except:
            raise AssertionError("Element is not present on the page.")

    def addReaction(self,reaction):
        username_field = self.driver.find_element(By.ID, "reaction")
        username_field.send_keys(reaction)


    def addComment(self,text):
        username_field = self.driver.find_element(By.ID, "comment")
        username_field.send_keys(text)