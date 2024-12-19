import json
import os
import time

import pytest
from _pytest.fixtures import FixtureRequest
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
from ui.pages.base_page import BasePage
from ui.pages.campany_page import CampanyPage
from ui.pages.login_page import LoginPage
from tests.base_case import BaseCase
from ui.locators.campany_locators import CampanyPageLocators

load_dotenv()


@pytest.fixture(scope='session')
def credentials():
    return {
        'user': os.getenv('LOGIN'),
        'password': os.getenv('PASSWORD')
    }

 
class TestCampany(BaseCase):

    def test_open_campany_page(self, credentials):
        login_page = LoginPage(self.driver)
        login_page.login(credentials)

    def test_campany_create_new_campany(self, credentials):
        campany_page = CampanyPage(self.driver)
        campany_page.open_page()
        result = campany_page.create_campany()
        assert result == "OK", "Err: no such campany"

    def test_campany_edit_campany(self, credentials):
        campany_page = CampanyPage(self.driver)
        campany_page.open_page()
        result = campany_page.edit_campany()
        assert result == "OK", "Err: no changes in campany"

