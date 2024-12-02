from tests.base_case import BaseCase

class TestLogin(BaseCase):
    def test_open(self):
        print(self.main_page.open_cabinet())
        assert 1 == 1