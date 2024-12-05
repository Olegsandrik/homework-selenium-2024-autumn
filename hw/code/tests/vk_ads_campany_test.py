import json
import os
import time

import pytest
from _pytest.fixtures import FixtureRequest
from selenium.common import TimeoutException
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
        

    def test_campany_filtr_open(self):
        campany_page = CampanyPage(self.driver)
        campany_page.open_page()
        campany_page.click(
            CampanyPageLocators.OPEN_FILTR, timeout=10
        )
        

    def test_campany_filtr_seved(self, credentials):
        campany_page = CampanyPage(self.driver)
        campany_page.open_page()
        campany_page.click(
            CampanyPageLocators.OPEN_FILTR, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.SAVED_FILTR, timeout=10
        )
        

    def test_campany_filtr_seved_click(self, credentials):
        campany_page = CampanyPage(self.driver)
        campany_page.open_page()
        campany_page.click(
            CampanyPageLocators.OPEN_FILTR, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.SAVED_FILTR, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.APPLY_FILTR, timeout=10
        )
        

    def test_campany_filtr_seved_delete(self, credentials):
        campany_page = CampanyPage(self.driver)
        campany_page.open_page()
        campany_page.click(
            CampanyPageLocators.OPEN_FILTR, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.SAVED_FILTR, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.DELETE_FILTR, timeout=10
        )
        

    def test_campany_filtr_new_delete_all(self, credentials):
        campany_page = CampanyPage(self.driver)
        campany_page.open_page()
        campany_page.click(
            CampanyPageLocators.OPEN_FILTR, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.FILTR_LAUNCHED, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.FILTR_DELETE_ALL_APPLY, timeout=10
        )
        

    def test_campany_filtr_new_delete_current_dir(self, credentials):
        campany_page = CampanyPage(self.driver)
        campany_page.open_page()
        campany_page.click(
            CampanyPageLocators.OPEN_FILTR, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.FILTR_LAUNCHED, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.FILTR_DELETE_CURR_DIR_APPLY, timeout=10
        )
        

    def test_campany_filtr_new_select_all_current_dir(self, credentials):
        campany_page = CampanyPage(self.driver)
        campany_page.open_page()
        campany_page.click(
            CampanyPageLocators.OPEN_FILTR, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.FILTR_APPLY_ALL, timeout=10
        )


    def test_campany_filtr_new_status_dir(self, credentials):
        campany_page = CampanyPage(self.driver)
        campany_page.open_page()
        campany_page.click(
            CampanyPageLocators.OPEN_FILTR, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.FILTR_STATUS_CAMPANY_LAUNCHED, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.FILTR_STATUS_CAMPANY_STOPED, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.FILTR_STATUS_SHOW_DELETED, timeout=10
        )

    def test_campany_filtr_new_status_moder_dir(self, credentials):
        campany_page = CampanyPage(self.driver)
        campany_page.open_page()
        campany_page.click(
            CampanyPageLocators.OPEN_FILTR, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.OPEN_FILTR_STATUS_MODER, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.FILTR_STATUS_MODER_ON_CHECK, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.FILTR_STATUS_MODER_DENIED, timeout=10
        )

    def test_campany_filtr_new_object_ads_dir(self, credentials):
        campany_page = CampanyPage(self.driver)
        campany_page.open_page()
        campany_page.click(
            CampanyPageLocators.OPEN_FILTR, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.FILTR_OPEN_OBJ_ADV, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.FILTR_STATUS_OBJ_ADV_MOBILE, timeout=10
        )

    def test_campany_filtr_new_translations_dir(self, credentials):
        campany_page = CampanyPage(self.driver)
        campany_page.open_page()
        campany_page.click(
            CampanyPageLocators.OPEN_FILTR, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.FILTR_OPEN_TRANSLATION, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.FILTR_TRANSLATION_ON, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.FILTR_TRANSLATION_OFF, timeout=10
        )

    def test_campany_filtr_new_campaign_effectiveness_dir(self, credentials):
        campany_page = CampanyPage(self.driver)
        campany_page.open_page()
        campany_page.click(
            CampanyPageLocators.OPEN_FILTR, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.FILTR_OPEN_EFFICIENCY, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.FILTR_EFFICIENCY_GOOD, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.FILTR_EFFICIENCY_MAKE_BETTER, timeout=10
        )


    def test_campany_filtr_cancellation(self, credentials):
        campany_page = CampanyPage(self.driver)
        campany_page.open_page()
        campany_page.click(
            CampanyPageLocators.OPEN_FILTR, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.FILTR_OPEN_EFFICIENCY, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.FILTR_EFFICIENCY_GOOD, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.FILTR_EFFICIENCY_MAKE_BETTER, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.FILTR_CANCEL, timeout=10
        )


    def test_campany_filtr_do(self, credentials):
        campany_page = CampanyPage(self.driver)
        campany_page.open_page()
        campany_page.click(
            CampanyPageLocators.OPEN_FILTR, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.FILTR_OPEN_EFFICIENCY, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.FILTR_EFFICIENCY_GOOD, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.FILTR_EFFICIENCY_MAKE_BETTER, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.FILTR_APPROVE, timeout=10
        )


    def test_campany_filtr_save_open(self, credentials):
        campany_page = CampanyPage(self.driver)
        campany_page.open_page()
        campany_page.click(
            CampanyPageLocators.OPEN_FILTR, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.FILTR_OPEN_EFFICIENCY, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.FILTR_EFFICIENCY_GOOD, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.FILTR_EFFICIENCY_MAKE_BETTER, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.FILTR_APPROVE, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.FILTR_SAVE_OPEN, timeout=10
        )
    

    def test_campany_filtr_save_close(self, credentials):
        campany_page = CampanyPage(self.driver)
        campany_page.open_page()
        campany_page.click(
            CampanyPageLocators.OPEN_FILTR, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.FILTR_OPEN_EFFICIENCY, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.FILTR_EFFICIENCY_GOOD, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.FILTR_EFFICIENCY_MAKE_BETTER, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.FILTR_APPROVE, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.FILTR_SAVE_OPEN, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.FILTR_SAVE_CLOSE, timeout=10
        )

    def test_campany_filtr_make_save(self, credentials):
        campany_page = CampanyPage(self.driver)
        campany_page.open_page()
        campany_page.click(
            CampanyPageLocators.OPEN_FILTR, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.FILTR_OPEN_EFFICIENCY, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.FILTR_EFFICIENCY_GOOD, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.FILTR_EFFICIENCY_MAKE_BETTER, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.FILTR_APPROVE, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.FILTR_SAVE_OPEN, timeout=10
        )
        campany_page.input(
            CampanyPageLocators.FILTR_SAVE_INPUT,
            "testinput",
        )
        campany_page.click(
            CampanyPageLocators.FILTR_SAVE_CLOSE, timeout=10
        )

    def test_campany_filtr_make_save_err_already_save(self, credentials):
        campany_page = CampanyPage(self.driver)
        campany_page.open_page()
        campany_page.click(
            CampanyPageLocators.OPEN_FILTR, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.FILTR_OPEN_EFFICIENCY, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.FILTR_EFFICIENCY_GOOD, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.FILTR_EFFICIENCY_MAKE_BETTER, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.FILTR_APPROVE, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.FILTR_SAVE_OPEN, timeout=10
        )
        campany_page.input(
            CampanyPageLocators.FILTR_SAVE_INPUT,
            "testinput",
        )
        campany_page.click(
            CampanyPageLocators.FILTR_SAVE_CLOSE, timeout=10
        )

    def test_campany_filtr_make_save_err_confused_field(self, credentials):
        campany_page = CampanyPage(self.driver)
        campany_page.open_page()
        campany_page.click(
            CampanyPageLocators.OPEN_FILTR, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.FILTR_OPEN_EFFICIENCY, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.FILTR_EFFICIENCY_GOOD, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.FILTR_EFFICIENCY_MAKE_BETTER, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.FILTR_APPROVE, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.FILTR_SAVE_OPEN, timeout=10
        )
        campany_page.input(
            CampanyPageLocators.FILTR_SAVE_INPUT,
            "",
        )
        campany_page.click(
            CampanyPageLocators.FILTR_SAVE_CLOSE, timeout=10
        )

    def test_campany_filtr_make_save_err_too_many_symbols(self, credentials):
        campany_page = CampanyPage(self.driver)
        campany_page.open_page()
        campany_page.click(
            CampanyPageLocators.OPEN_FILTR, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.FILTR_OPEN_EFFICIENCY, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.FILTR_EFFICIENCY_GOOD, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.FILTR_EFFICIENCY_MAKE_BETTER, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.FILTR_APPROVE, timeout=10
        )
        
        campany_page.click(
            CampanyPageLocators.FILTR_SAVE_OPEN, timeout=10
        )
        campany_page.input(
            CampanyPageLocators.FILTR_SAVE_INPUT,
            "testinput999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999444444444444444444444444444444444444444444444444444",
        )
        campany_page.click(
            CampanyPageLocators.FILTR_SAVE_CLOSE, timeout=10
        )

    def test_campany_filtr_remove(self, credentials):
        campany_page = CampanyPage(self.driver)
        campany_page.open_page()
        campany_page.click(
            CampanyPageLocators.OPEN_FILTR, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.FILTR_OPEN_EFFICIENCY, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.FILTR_EFFICIENCY_GOOD, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.FILTR_EFFICIENCY_MAKE_BETTER, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.FILTR_APPROVE, timeout=10
        )
        campany_page.click(
            CampanyPageLocators.FILTR_REMOVE, timeout=10
        )
       
