import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from ui.pages.base_page import BasePage
from ui.url.campany_urls import CampanyPageUrls
from selenium.webdriver.support import expected_conditions as EC


class CampanyPage(BasePage):

    def open_page(self):
        self.driver.get(CampanyPageUrls.dashboard)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.TAG_NAME, 'body'))
        )
