from selenium.webdriver.common.by import By

class HqBaseLocators:
    SETTINGS = (By.XPATH, "//a[@data-entityid='settings']")
    LEADFORMS = (By.XPATH, "//a[@data-entityid='leadads']")
    CHECKBOX = (By.XPATH, "//input[@type='checkbox']")