import time
from ui.pages.hq_base_page import HqBasePage
from ui.locators.settings_locators import SettingsLocators, MainSettingsLocators, NotificationsSettingsLocators, AccessSettingsLocators
from ui.url.urls import Urls
from selenium.webdriver.support import expected_conditions as EC


class SettingsPage(HqBasePage):
    url = Urls.setting_page
    base_settings_locators = SettingsLocators()

    def __init__(self, driver, overview_page_class):
        super().__init__(driver, overview_page_class=overview_page_class, settings_page_class=MainSettingsPage)

    def cancel_changes(self):
        cancel_btn = self.find(self.base_settings_locators.CANCEL_BUTTON)
        if (cancel_btn):
            cancel_btn.click()

    def save_changes(self):
        save_btn = self.find(self.base_settings_locators.SAVE_BUTTON)
        if (save_btn):
            save_btn.click()
    
    def open_notifications(self):
        self.click(self.base_settings_locators.NOTIFICATIONS_TAB, 20)
        return NotificationsSettingsPage(self.driver, self.overview_page_class, self.settings_page_class)

    def open_access(self):
        self.click(self.base_settings_locators.ACCESS_TAB, 20)
        return AccessSettingsPage(self.driver, self.overview_page_class, self.settings_page_class)


class MainSettingsPage(SettingsPage):
    url = Urls.setting_page
    locators = MainSettingsLocators()

    def get_phone(self):
        return self.find(self.locators.INPUT_PHONE, 30).get_attribute("value")

    def input_phone_number(self, new_number):
        self.input(self.locators.INPUT_PHONE, new_number, 20)

    def change_phone(self, new_number):
        self.input_phone_number(new_number)
        time.sleep(1)
        self.save_changes()


class NotificationsSettingsPage(HqBasePage):
    url = Urls.notifications_settings_page
    locators = NotificationsSettingsLocators()

class AccessSettingsPage(HqBasePage):
    url = Urls.access_settings_page
    locators = AccessSettingsLocators()