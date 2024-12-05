from ui.pages.login_page import LoginPage
from ui.pages.base_page import BasePage
from ui.locators.main_locators import MainPageLocators
from ui.url.urls import MainPageUrls

class MainPage(BasePage):
    url = MainPageUrls.MainPage

    locators = MainPageLocators()

    def open_cabinet(self):
        self.click(self.locators.OPEN_CABINET)
        return LoginPage(self.driver)