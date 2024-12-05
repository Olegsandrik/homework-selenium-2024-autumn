import time

from ui.pages.settings_page import MainSettingsPage
from ui.pages.overview_page import OverviewPage
from ui.pages.base_page import BasePage
from ui.locators.login_locators import LoginPageLocators
from ui.url.urls import Urls


class LoginPage(BasePage):

    url = Urls.login_page
    locators = LoginPageLocators()

    def login(self, credentials):
        self.input(
            self.locators.INPUT_LOGIN,
            credentials.get('user', ''),
            30
        )

        time.sleep(2)
        self.click(self.locators.SUBMIT, 15)

        self.click(self.locators.CHOOSE_AUTH_METHOD, 15)
        self.click(self.locators.USE_PASSWORD_AUTH, 10)

        self.input(self.locators.INPUT_PASSWORD, credentials.get('password', ''), 30)
        self.click(self.locators.SUBMIT, 10)
        self.click(self.locators.ORGANIZATION_ITEM, 15)

        return OverviewPage(self.driver, MainSettingsPage)