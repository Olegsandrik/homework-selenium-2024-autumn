from ui.pages.hq_base_page import HqBasePage
from ui.locators.settings_locators import MainSettingsLocators
from ui.url.urls import Urls

class OverviewPage(HqBasePage):
    url = Urls.overview_page

    def __init__(self, driver, settings_page_class, leadforms_page_class):
        super().__init__(driver, overview_page_class=OverviewPage, settings_page_class=settings_page_class, leadforms_page_class=leadforms_page_class)


