from selenium.webdriver.common.by import By

class SettingsLocators:
    SAVE_BUTTON = (By.XPATH, "//button[@data-testid='settings-save']")
    CANCEL_BUTTON = (By.XPATH, "//button[@data-testid='settings-cancel']")
    NOTIFICATIONS_TAB = (By.ID, "tab-settings.notifications")
    ACCESS_TAB = (By.ID, "tab-settings.access")
    WARNING_MESSAGE = (By.XPATH, "//div[contains(@class, 'Warning_warning')]")

class MainSettingsLocators:
    INPUT_PHONE = (By.XPATH, "//input[@data-testid='general-phone']")

class NotificationsSettingsLocators:
    pass

class AccessSettingsLocators:
    pass