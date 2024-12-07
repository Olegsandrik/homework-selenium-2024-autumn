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

    def test_campany_create_new_campany(self, credentials):
        campany_page = CampanyPage(self.driver)
        campany_page.open_page()

        campany_page.click(
            CampanyPageLocators.OPEN_CREATION_NEW_CAMPANY
        )

        campany_page.click(
            CampanyPageLocators.CHANGE_NAME_CAMPANY
        )
        
        campany_page.click(
            CampanyPageLocators.CHOOSE_SOCIETY
        )

        campany_page.click(
            CampanyPageLocators.DROPDOWN_ADVS_OBJECT
        )

        campany_page.click(
            CampanyPageLocators.INPUT_DESCRIPTION_APP
        )

        campany_page.input(
            CampanyPageLocators.INPUT_DESCRIPTION_APP,
            "Тестовое описаниеи ограничениефффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффФФФФФФ"
        )

        campany_page.input(
            CampanyPageLocators.INPUT_DESCRIPTION_APP,
            "Тестовое описание"
        )

        campany_page.click(
            CampanyPageLocators.INPUT_END_DATA_CAMPANY
        )

        campany_page.click(
            CampanyPageLocators.INPUT_SELECT_END_DATA
        )

        campany_page.click(
            CampanyPageLocators.DROPDOWN_MAIN_MOVEMENT
        )

        campany_page.click(
            CampanyPageLocators.SWITCH_OPTIMIZATION
        )

        campany_page.click(
            CampanyPageLocators.SWITCH_OPTIMIZATION
        )

        campany_page.click(
            CampanyPageLocators.DROPDOWN_STRATEGY
        )

        campany_page.input(
            CampanyPageLocators.INPUT_TARGETING,
            "90"
        )

        campany_page.input(
            CampanyPageLocators.INPUT_TARGETING,
            "99 999 999 999 999"
        )

        campany_page.input(
            CampanyPageLocators.INPUT_TARGETING,
            "101"
        )

        campany_page.click(
            CampanyPageLocators.DROPDOWN_TIME_STRATEGY
        )

        campany_page.click(
            CampanyPageLocators.BUTTON_CONTINUE
        )

        campany_page.click(
            CampanyPageLocators.BUTTON_SELECT_RUSSIA
        )

        campany_page.click(
            CampanyPageLocators.SWITCH_AUDIENCE
        )

        campany_page.click(
            CampanyPageLocators.BUTTON_SELECT_INTERESTS
        )

        campany_page.click(
            CampanyPageLocators.INPUT_INTERESTS,
        )

        campany_page.click(
            CampanyPageLocators.BUTTON_SELECT_INTERESTS_AUTO
        )

        campany_page.click(
            CampanyPageLocators.BUTTON_CONTINUE
        )

        campany_page.input(
            CampanyPageLocators.INPUT_DESCRIPTION_ADV,
            "Перспективная команда из Москвы"
        )

        campany_page.click(
            CampanyPageLocators.BUTTON_OPEN_AI
        )

        campany_page.click(
            CampanyPageLocators.BUTTON_SELECT_IMAGE_1
        )

        campany_page.click(
            CampanyPageLocators.BUTTON_SELECT_IMAGE_2
        )

        campany_page.click(
            CampanyPageLocators.BUTTON_ADD_IMAGE
        )

        video_element = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(
                CampanyPageLocators.BUTTON_NEW_VIDIO
            )
        )

        WebDriverWait(self.driver, 15).until(
            EC.visibility_of(video_element)
        )

        campany_page.click(
            CampanyPageLocators.BUTTON_PUBLISH
        )

        campany_page.click(
            CampanyPageLocators.BUTTON_CHECKBOX
        )

        campany_page.click(
            CampanyPageLocators.BUTTON_OPEN_OPTIONS
        )

        campany_page.click(
            CampanyPageLocators.BUTTON_OPEN_OPTIONS_DELETE
        )



