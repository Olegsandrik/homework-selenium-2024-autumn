from ui.pages.login_page import LoginPage
from ui.pages.base_page import BasePage
from ui.locators.main_locators import MainPageLocators


class MainPage(BasePage):
    url = "https://ads.vk.com/"

    locators = MainPageLocators()

    def open_cabinet(self):
        self.click(self.locators.OPEN_CABINET)
        return LoginPage(self.driver)