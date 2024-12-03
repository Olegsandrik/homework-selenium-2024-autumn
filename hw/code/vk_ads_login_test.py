import os
import time

import pytest
from _pytest.fixtures import FixtureRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
from hw.code.ui.pages.base_page import BasePage
from hw.code.ui.pages.main_page import MainPage
from hw.code.ui.pages.login_page import LoginPage
load_dotenv()


class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.login_page = LoginPage(driver)


@pytest.fixture(scope='session')
def credentials():
    return {
        'user': os.getenv('LOGIN'),
        'password': os.getenv('PASSWORD')
    }


class TestLogin(BaseCase):
    def test_login(self, credentials):
        login_page = LoginPage(self.driver)
        login_page.login(credentials)


