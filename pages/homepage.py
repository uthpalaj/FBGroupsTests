# facebook_homepage.py

from selenium.webdriver.common.by import By

class FacebookHomePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://www.facebook.com/")
        assert "Facebook" in self.driver.title


    def go_to_group_page(self, group_url):
        group_url = f"https://www.facebook.com/groups/{group_url}/"
        self.driver.get(group_url)

    def is_group_page_opened(self):
        return "groups" in self.driver.current_url
