from ui.pages.base_page import BasePage
from ui.locators.hq_base_locators import HqBaseLocators
from ui.url.urls import Urls

class HqBasePage(BasePage):
    url = Urls.hq_base_page
    base_locators = HqBaseLocators()

    def __init__(self, driver, overview_page_class, settings_page_class, leadforms_page_class):
        super().__init__(driver)
        self.overview_page_class = overview_page_class
        self.settings_page_class = settings_page_class
        self.leadforms_page_class = leadforms_page_class

    def open_settings(self):
        self.click(self.base_locators.SETTINGS, 15)
        return self.settings_page_class(self.driver, self.overview_page_class, self.leadforms_page_class)

    def open_leadforms(self):
        self.click(self.base_locators.LEADFORMS, 25)
        return self.leadforms_page_class(self.driver, self.overview_page_class, self.settings_page_class)
