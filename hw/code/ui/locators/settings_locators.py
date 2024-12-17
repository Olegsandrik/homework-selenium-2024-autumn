from selenium.webdriver.common.by import By

class SettingsLocators:
    SAVE_BUTTON = (By.XPATH, "//button[@data-testid='settings-save']")
    CANCEL_BUTTON = (By.XPATH, "//button[@data-testid='settings-cancel']")
    NOTIFICATIONS_TAB = (By.ID, "tab-settings.notifications")
    ACCESS_TAB = (By.ID, "tab-settings.access")
    WARNING_MESSAGE = (By.XPATH, "//div[contains(@class, 'Warning_warning')]")
    ERROR_MESSAGE = (By.XPATH, "//span[(@role='alert')]")

class MainSettingsLocators:
    INPUT_PHONE = (By.XPATH, "//input[@data-testid='general-phone']")
    ADD_EMAIL = (By.XPATH, "//span[text()='Добавить email']")
    INPUT_EMAIL = (By.XPATH, "//input[contains(@data-testid, 'email-')]")
    DELETE_EMAIL = (By.XPATH, "//button[@aria-label='Удалить']")
    INPUT_NAME = (By.XPATH, "//input[@data-testid='general-ord-name']")
    INPUT_ACCOUNT_NAME = (By.XPATH, "//input[@data-testid='account-item']")

class NotificationsSettingsLocators:
    WAYS_OF_DELIVERY_SWITCHES = (By.XPATH, "//div[contains(@class, 'vkuiCell')]//label[contains(@class, 'vkuiSwitch')]")

class AccessSettingsLocators:
    pass
