from hw.code.ui.pages.login_page import LoginPage
from hw.code.ui.pages.base_page import BasePage
from hw.code.ui.locators.main_locators import MainPageLocators
from hw.code.ui.url.urls import MainPageUrls

class MainPage(BasePage):
    url = MainPageUrls.MainPage

    locators = MainPageLocators()

    def open_cabinet(self):
        self.click(self.locators.OPEN_CABINET)
        return LoginPage(self.driver)