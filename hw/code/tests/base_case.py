import pytest
from contextlib import contextmanager
from _pytest.fixtures import FixtureRequest
from ui.pages.main_page import MainPage


class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest, credentials):
        self.driver = driver
        self.config = config

        if self.authorize:
            main_page = MainPage(self.driver)
            login_page = main_page.open_cabinet()
            self.overview_page = login_page.login(credentials)
