from selenium.webdriver.common.by import By

class LoginPageLocators:
    INPUT_LOGIN = (By.XPATH, "//input[@name='login']")
    SUBMIT = (By.XPATH, "//button[@type='submit']")
    CHOOSE_AUTH_METHOD = (By.XPATH, "//button[@data-test-id='other-verification-methods']")
    USE_PASSWORD_AUTH = (By.XPATH, "//div[@data-test-id='verificationMethod_password']")
    INPUT_PASSWORD = (By.XPATH, "//input[@type='password']")
    ORGANIZATION_ITEM = (By.XPATH, "//div[contains(@data-test-id, 'organization-item')]")
