from selenium.webdriver.common.by import By

class HqBaseLocators:
    SETTINGS = (By.XPATH, "//a[@data-entityid='settings']")
    CHECKBOX = (By.XPATH, "//input[@type='checkbox']")
