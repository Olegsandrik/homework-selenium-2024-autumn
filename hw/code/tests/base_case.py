import pytest
from contextlib import contextmanager
from _pytest.fixtures import FixtureRequest
from ui.pages.main_page import MainPage
from ui.pages.login_page import LoginPage


class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.login_page = LoginPage(driver)
