import pytest
from helpers.get_file import get_file
from ui.url.urls import Urls
from tests.base_case import BaseCase
from selenium.webdriver.support import expected_conditions as EC

class TestLeadformsPage(BaseCase):
     
    def test_open_page(self):
        self.overview_page.open_leadforms()
        assert self.driver.current_url == Urls.leadforms_page
    
    def fill_main_form_data(self, leadforms_page, name, header, company_name):
        leadforms_page.open_new_form()
        leadforms_page.fill_main_leadform_data(name, header, company_name)
        leadforms_page.upload_new_logo(get_file('logo.jpg'))
        leadforms_page.wait_until_sidebar_closed()

    def fill_first_page_small(self, leadforms_page, name, header, company_name, description):
        self.fill_main_form_data(leadforms_page, name, header, company_name)
        leadforms_page.fill_small_leadform_data(description)
        leadforms_page.next_page()

    def fill_first_page_big(self, leadforms_page, name, header, company_name, description):
        self.fill_main_form_data(leadforms_page, name, header, company_name)
        leadforms_page.fill_big_leadform_data(description)
        leadforms_page.next_page()

    def fill_first_page_discount_rubles(self, leadforms_page, name, header, company_name, discount):
        self.fill_main_form_data(leadforms_page, name, header, company_name)
        leadforms_page.fill_discount_rubles_leadform_data(discount)
        leadforms_page.next_page()

    def fill_first_page_discount_percent(self, leadforms_page, name, header, company_name, discount):
        self.fill_main_form_data(leadforms_page, name, header, company_name)
        leadforms_page.fill_discount_percent_leadform_data(discount)
        leadforms_page.next_page()

    def test_fill_first_page_small(self):
        leadforms_page = self.overview_page.open_leadforms()
        new_leadform_params = {
            'name': 'name',
            'header': 'header',
            'company_name': 'company_name',
            'description': 'description'
        }
        self.fill_first_page_small(leadforms_page, **new_leadform_params)
        current_step = leadforms_page.get_current_step()
        assert  current_step == '2'

    def test_fill_first_page_big(self):
        leadforms_page = self.overview_page.open_leadforms()
        new_leadform_params = {
            'name': 'name',
            'header': 'header',
            'company_name': 'company_name',
            'description': 'description'
        }
        self.fill_first_page_big(leadforms_page, **new_leadform_params)
        current_step = leadforms_page.get_current_step()
        assert  current_step == '2'
    
    def test_fill_first_page_discount_rubles(self):
        leadforms_page = self.overview_page.open_leadforms()
        new_leadform_params = {
            'name': 'name',
            'header': 'header',
            'company_name': 'company_name',
            'discount': '400'
        }
        self.fill_first_page_discount_rubles(leadforms_page, **new_leadform_params)
        current_step = leadforms_page.get_current_step()
        assert  current_step == '2'

    def test_fill_first_page_discount_percent(self):
        leadforms_page = self.overview_page.open_leadforms()
        new_leadform_params = {
            'name': 'name',
            'header': 'header',
            'company_name': 'company_name',
            'discount': '20'
        }
        self.fill_first_page_discount_percent(leadforms_page, **new_leadform_params)
        current_step = leadforms_page.get_current_step()
        assert  current_step == '2'
    
    def test_add_question(self):
        leadforms_page = self.overview_page.open_leadforms()
        new_leadform_params = {
            'name': 'name',
            'header': 'header',
            'company_name': 'company_name',
            'description': 'description'
        }
        self.fill_first_page_small(leadforms_page, **new_leadform_params)
        leadforms_page.click_add_question()
        assert len(leadforms_page.get_questions) == 1

    def test_remove_question(self):
        leadforms_page = self.overview_page.open_leadforms()
        new_leadform_params = {
            'name': 'name',
            'header': 'header',
            'company_name': 'company_name',
            'description': 'description'
        }
        self.fill_first_page_small(leadforms_page, **new_leadform_params)
        leadforms_page.click_add_question()
        assert len(leadforms_page.get_questions) == 1
        leadforms_page.remove_question()
        assert len(leadforms_page.get_questions) == 0
    
    def test_create_leadform(self):
        leadforms_page = self.overview_page.open_leadforms()
        initial_items_count = len(leadforms_page.get_leadform_items())
        new_leadform_params = {
            'name': 'name',
            'header': 'header',
            'company_name': 'company_name',
            'description': 'description'
        }
        self.fill_first_page_small(leadforms_page, **new_leadform_params)
        leadforms_page.next_page()
        leadforms_page.next_page()

        agreement_params = {
            'surname': 'surname',
            'address': 'address',
        }
        leadforms_page.fill_agreement(**agreement_params)
        leadforms_page.next_page()
        leadforms_page.wait_until_sidebar_closed()

        new_items_count = len(leadforms_page.get_leadform_items())
        assert new_items_count - initial_items_count == 1
