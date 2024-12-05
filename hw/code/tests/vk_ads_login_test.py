from dotenv import load_dotenv
import json
import os
import time
import pytest
from _pytest.fixtures import FixtureRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage
from ui.pages.login_page import LoginPage
from tests.base_case import BaseCase
load_dotenv()


load_dotenv()

@pytest.mark.skip('skip')
class TestLogin(BaseCase):
    def test_login(self):
        print(self.driver.current_url)

    def _test_login(self, credentials):
        login_page = LoginPage(self.driver)
        login_page.login(credentials)
