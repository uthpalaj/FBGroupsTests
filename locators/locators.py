from selenium.webdriver.common.by import By


class GroupLocators:
    likeBtn = (By.XPATH, "//a[@data-name='like']")
    comment = (By.XPATH, "//a[@data-name='comments']")
    report = (By.XPATH, "//a[@data-name='report']")
    transfer_tab = (By.XPATH, "//a[@data-name='cars']")
    visa_tab = (By.XPATH, "//a[@data-name='visa']")