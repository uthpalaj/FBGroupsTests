# facebook_login_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FacebookLoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://www.facebook.com/")
        assert "Facebook" in self.driver.title

    def login(self, username, password):
        username_field = self.driver.find_element(By.ID, "email")
        username_field.send_keys(username)
        password_field = self.driver.find_element(By.ID, "pass")
        password_field.send_keys(password)
        password_field = self.driver.find_element(By.ID, "pass")
        password_field.send_keys(Keys.RETURN)

    def wait_for_login(self):
        try:
            element_present = EC.presence_of_element_located((By.ID, "userNav"))
            WebDriverWait(self.driver, 10).until(element_present)
        except Exception as e:
            print("Login failed:", e)
            self.driver.quit()
            return False

        print("Login successful!")
        return True
