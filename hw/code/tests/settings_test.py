import random
import time

import pytest
from ui.url.urls import Urls
from tests.base_case import BaseCase


 
class TestMainSettings(BaseCase):

    def test_change_correct_phone(self):
        settings_page = self.overview_page.open_settings()

        initial_phone = settings_page.get_phone()
        initial_phone_digits = list(initial_phone[2:])
        random.shuffle(initial_phone_digits)
        new_phone = '+7' + ''.join(initial_phone_digits)
        settings_page.change_phone(new_phone)
        assert settings_page.get_phone() == new_phone
        settings_page.change_phone(initial_phone)
        assert settings_page.get_phone() == initial_phone


    def test_max_phone_length(self):
        long_phone_number = '1234567890abcdefrgtyhjuik'
        settings_page = self.overview_page.open_settings()
        settings_page.input_phone_number(long_phone_number)
        assert len(settings_page.get_phone()) == 14
        settings_page.cancel_changes()
    

    def test_enter_incorrect_phone(self):
        settings_page = self.overview_page.open_settings()

        new_phone = 'abcdefg'
        settings_page.change_phone(new_phone)
        error_message = 'Некорректный номер телефона'

        assert settings_page.is_on_page(error_message)


    def test_delete_phone(self):
        settings_page = self.overview_page.open_settings()
        initial_phone = settings_page.get_phone()
        settings_page.change_phone('')
        assert settings_page.get_phone() == ''
        settings_page.change_phone(initial_phone)
    

    def test_max_email_length(self):
        long_email = '1' * 1000
        settings_page = self.overview_page.open_settings()
        settings_page.add_email(long_email)
        assert len(settings_page.get_email_input_with_index().get_attribute("value")) == 255
        settings_page.cancel_changes()
    

    def test_enter_incorrect_email(self):
        settings_page = self.overview_page.open_settings()

        incorrect_email = 'aaaaa1212'
        settings_page.add_email(incorrect_email)
        error_message = 'Некорректный email адрес'

        assert settings_page.is_on_page(error_message)
    

    def test_add_email(self):
        settings_page = self.overview_page.open_settings()
        new_email = 'abc@mail.ru'
        settings_page.add_email(new_email)
        assert settings_page.get_email_input_with_index().get_attribute("value") == new_email
        settings_page.delete_email_with_index()
    

    def test_change_correct_name(self):
        settings_page = self.overview_page.open_settings()

        initial_name = settings_page.get_name()
        new_name = 'Андрей'
        settings_page.change_name(new_name)
        assert settings_page.get_name() == new_name
        settings_page.change_name(initial_name)
        assert settings_page.get_name() == initial_name


    def test_max_name_length(self):
        long_name = 'a' * 1000
        settings_page = self.overview_page.open_settings()
        settings_page.input_name(long_name)
        assert len(settings_page.get_name()) == 255
        settings_page.cancel_changes()
    

    def test_enter_incorrect_name(self):
        settings_page = self.overview_page.open_settings()

        incorrect_name = 'abcdre4223+-='
        settings_page.change_name(incorrect_name)
        error_message = 'Некорректные символы. Разрешена только кириллица дефис и пробел'

        assert settings_page.is_on_page(error_message)


    def test_change_correct_account_name(self):
        settings_page = self.overview_page.open_settings()

        initial_account_name = settings_page.get_account_name()
        new_account_name = 'Андрей'
        settings_page.change_account_name(new_account_name)
        assert settings_page.get_account_name() == new_account_name
        settings_page.change_account_name(initial_account_name)
        assert settings_page.get_account_name() == initial_account_name


    def test_max_account_name_length(self):
        long_account_name = 'a' * 1000
        settings_page = self.overview_page.open_settings()
        settings_page.input_account_name(long_account_name)
        assert len(settings_page.get_account_name()) == 255
        settings_page.cancel_changes()


 
class TestNotificationsSettings(BaseCase):

    def test_open_notifications(self):
        notifications_settings_page = self.overview_page.open_settings().open_notifications()
        assert notifications_settings_page.driver.current_url == Urls.notifications_settings_page
    

    def test_turn_off_notifications(self):
        notifications_settings_page = self.overview_page.open_settings().open_notifications()
        turned_off_switches = notifications_settings_page.turn_off_switches()
        warning_message = 'Уведомления выключены'
        assert notifications_settings_page.is_on_page(warning_message)
        notifications_settings_page.turn_on_delivery_way(turned_off_switches)



 
class TestAccessSettings(BaseCase):
    def test_open_access_settings(self):
        settings_page = self.overview_page.open_settings()

        notifications_settings_page = settings_page.open_access()
        assert notifications_settings_page.driver.current_url == Urls.access_settings_page
    
