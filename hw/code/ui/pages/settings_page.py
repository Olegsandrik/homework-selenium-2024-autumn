import time
from ui.pages.hq_base_page import HqBasePage
from ui.locators.settings_locators import SettingsLocators, MainSettingsLocators, NotificationsSettingsLocators, AccessSettingsLocators
from ui.url.urls import Urls
from selenium.webdriver.support import expected_conditions as EC


class NotificationsSettingsPage:
    pass


class AccessSettingsPage:
    pass


class SettingsPage(HqBasePage):
    url = Urls.setting_page
    base_settings_locators = SettingsLocators()

    def __init__(self, driver, overview_page_class, leadforms_page_class):
        super().__init__(driver, overview_page_class=overview_page_class, settings_page_class=MainSettingsPage, leadforms_page_class=leadforms_page_class)

    def cancel_changes(self):
        cancel_btn = self.find(self.base_settings_locators.CANCEL_BUTTON)
        if (cancel_btn):
            cancel_btn.click()

    def save_changes(self):
        save_btn = self.find(self.base_settings_locators.SAVE_BUTTON)
        if (save_btn):
            save_btn.click()
    
    def open_notifications(self) -> NotificationsSettingsPage:
        self.click(self.base_settings_locators.NOTIFICATIONS_TAB, 20)
        return NotificationsSettingsPage(self.driver, self.overview_page_class)

    def open_access(self) -> AccessSettingsPage:
        self.click(self.base_settings_locators.ACCESS_TAB, 20)
        return AccessSettingsPage(self.driver, self.overview_page_class)


class MainSettingsPage(SettingsPage):
    url = Urls.setting_page
    locators = MainSettingsLocators()

    def get_phone(self):
        return self.find(self.locators.INPUT_PHONE, 30).get_attribute("value")

    def input_phone_number(self, new_number):
        self.input(self.locators.INPUT_PHONE, new_number, 20)
    
    def change_phone(self, new_number):
        self.input_phone_number(new_number)
        self.save_changes()
    
    def get_email_input_with_index(self, index=-1):
        emails = self.find_all(self.locators.INPUT_EMAIL, 10)
        if index < 0 or index > len(emails) - 1:
            index = len(emails) - 1
        return emails[index]

    def enter_new_email(self, new_email):
        self.click(self.locators.ADD_EMAIL, 10)
        new_email_input = self.get_email_input_with_index()
        new_email_input.clear()
        new_email_input.send_keys(new_email)
    
    def add_email(self, new_email):
        self.enter_new_email(new_email)
        self.save_changes()
    
    def delete_email_with_index(self, index=-1):
        delete_btns = self.find_all(self.locators.DELETE_EMAIL, 10)
        if index < 0 or index > len(delete_btns) - 1:
            index = len(delete_btns) - 1
        delete_btns[index].click()
    
    def input_name(self, new_name):
        self.input(self.locators.INPUT_NAME, new_name, 20)
    
    def change_name(self, new_name):
        self.input_name(new_name)
        self.save_changes()
    
    def get_name(self):
        return self.find(self.locators.INPUT_NAME, 30).get_attribute("value")
    
    def input_account_name(self, new_account_name):
        self.input(self.locators.INPUT_ACCOUNT_NAME, new_account_name, 20)
    
    def change_account_name(self, new_account_name):
        self.input_account_name(new_account_name)
        self.save_changes()
    
    def get_account_name(self):
        return self.find(self.locators.INPUT_ACCOUNT_NAME, 30).get_attribute("value")


class NotificationsSettingsPage(SettingsPage):
    url = Urls.notifications_settings_page
    locators = NotificationsSettingsLocators()

    def get_delivery_switches(self):
        return self.find_all(self.locators.WAYS_OF_DELIVERY_SWITCHES)
    
    def turn_off_all_delivery(self):
        turned_off_switches = []
        for switch in self.get_delivery_switches():
            checkbox = switch.find_element(*self.base_locators.CHECKBOX)
            if checkbox.is_selected():
                turned_off_switches.append(switch)
                switch.click()
        return turned_off_switches
    
    def turn_on_delivery_ways(self, switches):
        for switch in switches:
            switch.click()


class AccessSettingsPage(SettingsPage):
    url = Urls.access_settings_page
    locators = AccessSettingsLocators()
    
    def __init__(self, driver, overview_page_class):
        super().__init__(driver, overview_page_class=overview_page_class, settings_page_class=MainSettingsPage)
