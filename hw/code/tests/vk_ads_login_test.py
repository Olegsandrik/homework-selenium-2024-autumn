from dotenv import load_dotenv
import pytest
from ui.pages.main_page import MainPage
from tests.base_case import BaseCase

load_dotenv()

@pytest.mark.skip('skip')
class TestLogin(BaseCase):
    def test_login(self):
        print(self.driver.current_url)
