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


@pytest.mark.skip('skip')
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
            CampanyPageLocators.BUTTON_SELECT_MOSCOW, timeout=10
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

        campany_page.click(
            CampanyPageLocators.BUTTON_OPEN_AI, timeout=10
        )

        campany_page.click(
            CampanyPageLocators.BUTTON_SELECT_IMAGE, timeout=10
        )

        campany_page.click(
            CampanyPageLocators.BUTTON_ADD_IMAGE, timeout=10
        )

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located(CampanyPageLocators.BUTTON_NEW_VIDIO)
        )

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(CampanyPageLocators.BUTTON_NEW_VIDIO)
        )

        campany_page.click(
            CampanyPageLocators.INPUT_TITLE_ADV_CLICK, timeout=10
        )

        campany_page.input(
            CampanyPageLocators.INPUT_TITLE_ADV,
            "Тест на ограничениеееееееееееееееееееееееееееееееееееееееееееееЕЕЕЕЕЕЕЕЕЕЕЕЕЕ"
        )

        campany_page.input(
            CampanyPageLocators.INPUT_TITLE_ADV,
            "ВК PRODIGY"
        )

        campany_page.click(
            CampanyPageLocators.INPUT_DESCRIPTION_ADV_CLICK, timeout=10
        )

        campany_page.input(
            CampanyPageLocators.INPUT_DESCRIPTION_ADV,
            "Перспективная команда из Москвы"
        )

        campany_page.click(
            CampanyPageLocators.BUTTON_PUBLISH, timeout=10
        )

        try:
            WebDriverWait(self.driver, 40).until(
                EC.presence_of_element_located(CampanyPageLocators.CREATED_CAMPANY)
            )
            WebDriverWait(self.driver, 40).until(
                EC.presence_of_element_located(CampanyPageLocators.DIV_CREATE_CAMPANY_NEW_BUDGET)
            )

            edit_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    CampanyPageLocators.BUTTON_EDIT_CAMPANY
                )
            )

            edit_element.click()

            WebDriverWait(self.driver, 40).until(
                EC.presence_of_element_located(CampanyPageLocators.DIV_CREATE_CAMPANY_NEW_ACTION)
            )
            campany_page.click(
                CampanyPageLocators.BUTTON_CREATE_CAMPANY_CLOSE_EDIT, timeout=10
            )

        except NoSuchElementException:
            pytest.fail("Созданная кампания не найдена.")

        campany_page.click(
            CampanyPageLocators.BUTTON_CHECKBOX, timeout=10
        )

        WebDriverWait(self.driver, 40).until(
            EC.element_to_be_clickable(CampanyPageLocators.BUTTON_OPEN_OPTIONS)
        )

        campany_page.click(
            CampanyPageLocators.BUTTON_OPEN_OPTIONS, timeout=10
        )

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                CampanyPageLocators.BUTTON_OPEN_OPTIONS_DELETE
            )
        )

        campany_page.click(
            CampanyPageLocators.BUTTON_OPEN_OPTIONS_DELETE, timeout=10
        )

    def test_campany_edit_campany(self, credentials):
        campany_page = CampanyPage(self.driver)
        campany_page.open_page()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                CampanyPageLocators.BUTTON_EDIT_CAMPANY
            )
        )

        campany_page.click(
            CampanyPageLocators.BUTTON_EDIT_CAMPANY, timeout=10
        )

        campany_page.click(
            CampanyPageLocators.BUTTON_EDIT_CAMPANY_SELECT_END_DATE, timeout=10
        )

        campany_page.click(
            CampanyPageLocators.BUTTON_EDIT_CAMPANY_SELECT_DATE_27, timeout=10
        )

        campany_page.input(
            CampanyPageLocators.INPUT_EDIT_CAMPANY_ADD_NEW_BUDGET,
            "121"
        )

        campany_page.click(
            CampanyPageLocators.BUTTON_EDIT_CAMPANY_OPEN_GROUPS, timeout=10
        )

        WebDriverWait(self.driver, 40).until(
            EC.element_to_be_clickable(CampanyPageLocators.INPUT_EDIT_CAMPANY_ADD_NEW_CITY)
        )

        campany_page.input(
            CampanyPageLocators.INPUT_EDIT_CAMPANY_ADD_NEW_CITY,
            "Санкт-Петербург"
        )

        campany_page.click(
            CampanyPageLocators.BUTTON_EDIT_CAMPANY_ADD_SAINT_P, timeout=10
        )

        campany_page.click(
            CampanyPageLocators.BUTTON_EDIT_CAMPANY_OPEN_ADV, timeout=10
        )

        WebDriverWait(self.driver, 40).until(
            EC.element_to_be_clickable(CampanyPageLocators.INPUT_DESCRIPTION_ADV)
        )

        campany_page.input(
            CampanyPageLocators.INPUT_DESCRIPTION_ADV,
            "Тестовое описание после редактирования"
        )

        campany_page.click(
            CampanyPageLocators.BUTTON_EDIT_CAMPANY_SUBMIT, timeout=10,
        )

        try:
            WebDriverWait(self.driver, 40).until(
                EC.presence_of_element_located(CampanyPageLocators.DIV_EDIT_CAMPANY_NEW_BUDGET)
            )

            WebDriverWait(self.driver, 40).until(
                EC.presence_of_element_located(CampanyPageLocators.DIV_EDIT_BUDGET_NEW_CAMPANY_NAME)
            )

            WebDriverWait(self.driver, 40).until(
                EC.presence_of_element_located(CampanyPageLocators.DIV_EDIT_BUDGET_NEW_END_DATE)
            )

            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    CampanyPageLocators.BUTTON_EDIT_CAMPANY
                )
            )

            campany_page.click(
                CampanyPageLocators.BUTTON_EDIT_CAMPANY, timeout=10
            )

            campany_page.click(
                CampanyPageLocators.BUTTON_EDIT_CAMPANY_OPEN_GROUPS, timeout=10
            )

            WebDriverWait(self.driver, 40).until(
                EC.presence_of_element_located(CampanyPageLocators.DIV_EDIT_BUDGET_NEW_CITY)
            )

            campany_page.click(
                CampanyPageLocators.BUTTON_EDIT_CAMPANY_OPEN_ADV, timeout=10
            )

            WebDriverWait(self.driver, 40).until(
                EC.presence_of_element_located(CampanyPageLocators.DIV_EDIT_BUDGET_NEW_DESCR)
            )

        except NoSuchElementException:
            pytest.fail("Изменения не были сохранены")

