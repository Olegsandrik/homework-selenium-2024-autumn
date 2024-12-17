from ui.url.urls import Urls
from ui.pages.login_page import LoginPage
from ui.pages.base_page import BasePage
from ui.locators.main_locators import MainPageLocators

class MainPage(BasePage):
    url = Urls.main_page

    locators = MainPageLocators()

    def open_cabinet(self):
        self.click(self.locators.OPEN_CABINET, 20)
        return LoginPage(self.driver)
