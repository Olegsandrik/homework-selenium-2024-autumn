import time

import pytest
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from ui.pages.base_page import BasePage
from ui.url.campany_urls import CampanyPageUrls
from selenium.webdriver.support import expected_conditions as EC
from ui.locators.campany_locators import CampanyPageLocators
from ui.constants.constants_campany import CampanyPageConstants


class CampanyPage(BasePage):

    def open_page(self):
        self.driver.get(CampanyPageUrls.dashboard)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.TAG_NAME, 'body'))
        )

    def create_campany(self):
        self.click(
            CampanyPageLocators.OPEN_CREATION_NEW_CAMPANY, timeout=10
        )

        self.click(
            CampanyPageLocators.CHANGE_NAME_CAMPANY, timeout=10
        )

        self.click(
            CampanyPageLocators.CHOOSE_SOCIETY, timeout=10
        )

        self.click(
            CampanyPageLocators.DROPDOWN_ADVS_OBJECT, timeout=10
        )

        self.click(
            CampanyPageLocators.INPUT_DESCRIPTION_APP, timeout=10
        )

        self.input(
            CampanyPageLocators.INPUT_DESCRIPTION_APP,
            CampanyPageConstants.INPUT_DESCRIPTION_APP_MAX
        )

        self.input(
            CampanyPageLocators.INPUT_DESCRIPTION_APP,
            CampanyPageConstants.INPUT_DESCRIPTION_APP
        )

        self.click(
            CampanyPageLocators.INPUT_END_DATA_CAMPANY, timeout=10
        )

        self.click(
            CampanyPageLocators.INPUT_SELECT_END_DATA, timeout=10
        )

        self.click(
            CampanyPageLocators.DROPDOWN_MAIN_MOVEMENT, timeout=10
        )

        self.click(
            CampanyPageLocators.SWITCH_OPTIMIZATION, timeout=10
        )

        self.click(
            CampanyPageLocators.SWITCH_OPTIMIZATION, timeout=10
        )

        self.click(
            CampanyPageLocators.DROPDOWN_STRATEGY, timeout=10
        )

        self.input(
            CampanyPageLocators.INPUT_TARGETING,
            CampanyPageConstants.INPUT_TARGETING_MIN
        )

        self.input(
            CampanyPageLocators.INPUT_TARGETING,
            CampanyPageConstants.INPUT_TARGETING_MAX
        )

        self.input(
            CampanyPageLocators.INPUT_TARGETING,
            CampanyPageConstants.INPUT_TARGETING
        )

        self.click(
            CampanyPageLocators.DROPDOWN_TIME_STRATEGY, timeout=10
        )

        self.click(
            CampanyPageLocators.BUTTON_CONTINUE, timeout=10
        )

        self.click(
            CampanyPageLocators.BUTTON_SELECT_MOSCOW, timeout=10
        )

        self.click(
            CampanyPageLocators.SWITCH_AUDIENCE, timeout=10
        )

        self.click(
            CampanyPageLocators.BUTTON_SELECT_INTERESTS, timeout=10
        )

        self.click(
            CampanyPageLocators.INPUT_INTERESTS, timeout=10
        )

        self.click(
            CampanyPageLocators.BUTTON_SELECT_INTERESTS_AUTO, timeout=10
        )

        self.click(
            CampanyPageLocators.BUTTON_CONTINUE, timeout=10
        )

        self.click(
            CampanyPageLocators.BUTTON_OPEN_AI, timeout=10
        )

        self.click(
            CampanyPageLocators.BUTTON_SELECT_IMAGE, timeout=10
        )

        self.click(
            CampanyPageLocators.BUTTON_ADD_IMAGE, timeout=10
        )

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located(CampanyPageLocators.BUTTON_NEW_VIDIO)
        )

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(CampanyPageLocators.BUTTON_NEW_VIDIO)
        )

        self.click(
            CampanyPageLocators.INPUT_TITLE_ADV_CLICK, timeout=10
        )

        self.input(
            CampanyPageLocators.INPUT_TITLE_ADV,
            CampanyPageConstants.INPUT_TITLE_ADV_MAX
        )

        self.input(
            CampanyPageLocators.INPUT_TITLE_ADV,
            CampanyPageConstants.INPUT_TITLE_ADV
        )

        self.click(
            CampanyPageLocators.INPUT_DESCRIPTION_ADV_CLICK, timeout=10
        )

        self.input(
            CampanyPageLocators.INPUT_DESCRIPTION_ADV,
            CampanyPageConstants.INPUT_DESCRIPTION_ADV
        )

        self.click(
            CampanyPageLocators.BUTTON_PUBLISH, timeout=10
        )

        self.click(
            CampanyPageLocators.BUTTON_PUBLISH_SUBMIT, timeout=10
        )

        try:
            WebDriverWait(self.driver, 40).until(
                EC.presence_of_element_located(CampanyPageLocators.CREATED_CAMPANY)
            )
            WebDriverWait(self.driver, 40).until(
                EC.presence_of_element_located(CampanyPageLocators.DIV_CREATE_CAMPANY_NEW_BUDGET)
            )

            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    CampanyPageLocators.BUTTON_EDIT_CAMPANY
                )
            )

            self.click(
                CampanyPageLocators.BUTTON_EDIT_CAMPANY, timeout=10
            )

            WebDriverWait(self.driver, 40).until(
                EC.presence_of_element_located(CampanyPageLocators.DIV_CREATE_CAMPANY_NEW_ACTION)
            )

            self.click(
                CampanyPageLocators.BUTTON_CREATE_CAMPANY_CLOSE_EDIT, timeout=10
            )

        except (NoSuchElementException, TimeoutException):
            return CampanyPageConstants.ERR

        self.click(
            CampanyPageLocators.BUTTON_CHECKBOX, timeout=10
        )

        WebDriverWait(self.driver, 40).until(
            EC.element_to_be_clickable(CampanyPageLocators.BUTTON_OPEN_OPTIONS)
        )

        self.click(
            CampanyPageLocators.BUTTON_OPEN_OPTIONS, timeout=10
        )

        self.click(
            CampanyPageLocators.BUTTON_OPEN_OPTIONS, timeout=10
        )

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                CampanyPageLocators.BUTTON_OPEN_OPTIONS_DELETE
            )
        )

        self.click(
            CampanyPageLocators.BUTTON_OPEN_OPTIONS_DELETE, timeout=10
        )

        return CampanyPageConstants.STATUS_OK

    def edit_campany(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                CampanyPageLocators.BUTTON_EDIT_CAMPANY
            )
        )

        self.click(
            CampanyPageLocators.BUTTON_EDIT_CAMPANY, timeout=10
        )

        self.click(
            CampanyPageLocators.BUTTON_EDIT_CAMPANY_SELECT_END_DATE, timeout=10
        )

        self.click(
            CampanyPageLocators.BUTTON_EDIT_CAMPANY_SELECT_DATE_27, timeout=10
        )

        self.input(
            CampanyPageLocators.INPUT_EDIT_CAMPANY_ADD_NEW_BUDGET,
            CampanyPageConstants.INPUT_EDIT_CAMPANY_ADD_NEW_BUDGET
        )

        self.click(
            CampanyPageLocators.BUTTON_EDIT_CAMPANY_OPEN_GROUPS, timeout=10
        )

        WebDriverWait(self.driver, 40).until(
            EC.element_to_be_clickable(CampanyPageLocators.INPUT_EDIT_CAMPANY_ADD_NEW_CITY)
        )

        self.input(
            CampanyPageLocators.INPUT_EDIT_CAMPANY_ADD_NEW_CITY,
            CampanyPageConstants.INPUT_EDIT_CAMPANY_ADD_NEW_CITY
        )

        self.click(
            CampanyPageLocators.BUTTON_EDIT_CAMPANY_ADD_SAINT_P, timeout=10
        )

        self.click(
            CampanyPageLocators.BUTTON_EDIT_CAMPANY_OPEN_ADV, timeout=10
        )

        WebDriverWait(self.driver, 40).until(
            EC.element_to_be_clickable(CampanyPageLocators.INPUT_DESCRIPTION_ADV)
        )

        self.input(
            CampanyPageLocators.INPUT_DESCRIPTION_ADV,
            CampanyPageConstants.INPUT_DESCRIPTION_ADV_EDIT
        )

        self.click(
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

            self.click(
                CampanyPageLocators.BUTTON_EDIT_CAMPANY, timeout=10
            )

            self.click(
                CampanyPageLocators.BUTTON_EDIT_CAMPANY_OPEN_GROUPS, timeout=10
            )

            WebDriverWait(self.driver, 40).until(
                EC.presence_of_element_located(CampanyPageLocators.DIV_EDIT_BUDGET_NEW_CITY)
            )

            self.click(
                CampanyPageLocators.BUTTON_EDIT_CAMPANY_OPEN_ADV, timeout=10
            )

            WebDriverWait(self.driver, 40).until(
                EC.presence_of_element_located(CampanyPageLocators.DIV_EDIT_BUDGET_NEW_DESCR)
            )

        except (NoSuchElementException, TimeoutException):
            return CampanyPageConstants.ERR

        return CampanyPageConstants.STATUS_OK
