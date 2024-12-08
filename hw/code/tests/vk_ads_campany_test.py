import json
import os
import time

import pytest
from _pytest.fixtures import FixtureRequest
from selenium.common import TimeoutException, NoSuchElementException
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
            CampanyPageLocators.OPEN_CREATION_NEW_CAMPANY, timeout=10
        )

        campany_page.click(
            CampanyPageLocators.CHANGE_NAME_CAMPANY, timeout=10
        )

        campany_page.input(
            CampanyPageLocators.INPUT_NEW_CAMPANY_NAME,
            "Тестовое название ограничениефффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффффФФФФФФ"
        )

        campany_page.input(
            CampanyPageLocators.INPUT_NEW_CAMPANY_NAME,
            "Тестовое название"
        )

        campany_page.click(
            CampanyPageLocators.CHOOSE_SOCIETY, timeout=10
        )

        campany_page.click(
            CampanyPageLocators.DROPDOWN_ADVS_OBJECT, timeout=10
        )

        campany_page.click(
            CampanyPageLocators.INPUT_DESCRIPTION_APP, timeout=10
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
            CampanyPageLocators.INPUT_END_DATA_CAMPANY, timeout=10
        )

        campany_page.click(
            CampanyPageLocators.INPUT_SELECT_END_DATA, timeout=10
        )

        campany_page.click(
            CampanyPageLocators.DROPDOWN_MAIN_MOVEMENT, timeout=10
        )

        campany_page.click(
            CampanyPageLocators.SWITCH_OPTIMIZATION, timeout=10
        )

        campany_page.click(
            CampanyPageLocators.SWITCH_OPTIMIZATION, timeout=10
        )

        campany_page.click(
            CampanyPageLocators.DROPDOWN_STRATEGY, timeout=10
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
            CampanyPageLocators.DROPDOWN_TIME_STRATEGY, timeout=10
        )

        campany_page.click(
            CampanyPageLocators.BUTTON_CONTINUE, timeout=10
        )

        campany_page.click(
            CampanyPageLocators.BUTTON_SELECT_RUSSIA, timeout=10
        )

        campany_page.click(
            CampanyPageLocators.SWITCH_AUDIENCE, timeout=10
        )

        campany_page.click(
            CampanyPageLocators.BUTTON_SELECT_INTERESTS, timeout=10
        )

        campany_page.click(
            CampanyPageLocators.INPUT_INTERESTS, timeout=10
        )

        campany_page.click(
            CampanyPageLocators.BUTTON_SELECT_INTERESTS_AUTO, timeout=10
        )

        campany_page.click(
            CampanyPageLocators.BUTTON_CONTINUE, timeout=10
        )

        campany_page.input(
            CampanyPageLocators.INPUT_DESCRIPTION_ADV,
            "Перспективная команда из Москвы"
        )

        campany_page.click(
            CampanyPageLocators.BUTTON_OPEN_AI, timeout=10
        )

        campany_page.click(
            CampanyPageLocators.BUTTON_SELECT_IMAGE_1, timeout=10
        )

        campany_page.click(
            CampanyPageLocators.BUTTON_SELECT_IMAGE_2, timeout=10
        )

        campany_page.click(
            CampanyPageLocators.BUTTON_ADD_IMAGE, timeout=10
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
            CampanyPageLocators.BUTTON_PUBLISH, timeout=10
        )

        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, CampanyPageLocators.CREATED_CAMPANY))
            )
        except NoSuchElementException:
            pytest.fail("Кампания не найдена.")

        campany_page.click(
            CampanyPageLocators.BUTTON_CHECKBOX, timeout=10
        )

        campany_page.click(
            CampanyPageLocators.BUTTON_OPEN_OPTIONS, timeout=10
        )

        campany_page.click(
            CampanyPageLocators.BUTTON_OPEN_OPTIONS_DELETE, timeout=10
        )

