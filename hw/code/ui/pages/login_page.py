import time

from selenium.webdriver.common.by import By
from ui.pages.base_page import BasePage
from ui.locators.main_locators import MainPageLocators
from ui.locators.main_locators import LoginPageLocators
from ui.url.urls import MainPageUrls


class LoginPage(BasePage):

    url = MainPageUrls.MainPage

    def login(self, credentials):
        self.driver.maximize_window()
        self.click(
            MainPageLocators.OPEN_CABINET, timeout=10
        )
        time.sleep(2)
        self.input(
            LoginPageLocators.INPUT_PHONE,
            credentials.get('user', ''),
        )
        time.sleep(2)
        self.click(
            LoginPageLocators.SUBMIT_PHONE
        )
        time.sleep(15) # это для двухфакторки
        self.input(
            LoginPageLocators.INPUT_PASSWORD,
            credentials.get('password', ''),
        )
        time.sleep(2)
        self.click(
            LoginPageLocators.SUBMIT_PASSWORD
        )
        time.sleep(10) # капча
        self.click(
            LoginPageLocators.COUNTIUE_LOGIN
        )