import random
import time

import pytest
from ui.url.urls import Urls
from tests.base_case import BaseCase


class TestMainSettings(BaseCase):
    @pytest.mark.skip('skip')
    def test_change_phone(self):
        settings_page = self.overview_page.open_settings()

        initial_phone = settings_page.get_phone()
        initial_phone_digits = list(initial_phone[2:])
        random.shuffle(initial_phone_digits)
        new_phone = '+7' + ''.join(initial_phone_digits)
        settings_page.change_phone(new_phone)
        assert settings_page.get_phone() == new_phone
        time.sleep(1)
        settings_page.change_phone(initial_phone)
        assert settings_page.get_phone() == initial_phone

    @pytest.mark.skip('skip')
    def test_max_phone_length(self):
        long_phone_number = '1234567890abcdefrgtyhjuik'
        settings_page = self.overview_page.open_settings()
        settings_page.input_phone_number(long_phone_number)
        assert len(settings_page.get_phone()) == 14
    
    @pytest.mark.skip('skip')
    def test_cancel_changes(self):
        settings_page = self.overview_page.open_settings()

        initial_phone = settings_page.get_phone()
        initial_phone_digits = list(initial_phone[2:])
        random.shuffle(initial_phone_digits)
        new_phone = '+7' + ''.join(initial_phone_digits)
        settings_page.input_phone_number(new_phone)
        time.sleep(1)
        settings_page.cancel_changes()
        assert settings_page.get_phone() == initial_phone

class TestNotificationsSettings(BaseCase):
    @pytest.mark.skip('skip')
    def test_open_notifications(self):
        settings_page = self.overview_page.open_settings()

        notifications_settings_page = settings_page.open_notifications()
        assert notifications_settings_page.driver.current_url == Urls.notifications_settings_page
    
class TestAccessSettings(BaseCase):
    def test_open_access_settings(self):
        settings_page = self.overview_page.open_settings()

        notifications_settings_page = settings_page.open_access()
        assert notifications_settings_page.driver.current_url == Urls.access_settings_page
    
