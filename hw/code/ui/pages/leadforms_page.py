import time
from ui.pages.hq_base_page import HqBasePage
from ui.locators.leadforms_locators import LeadFormsLocators
from ui.url.urls import Urls
from selenium.webdriver.support import expected_conditions as EC

INPUT_INDEXES = {
    'name': 0,
    'company_name': 1,
    'header': 2,
    'description': 3,
}

AGREEMENT_INPUTS_INDEXES = {
    'surname': 0,
    'address': 1,
    'email': 2,
    'INN': 3
}

FORM_TYPES_INDEXES = {
    'small': 0,
    'big': 1,
    'magnet': 2
}

class LeadformsPage(HqBasePage):
    url = Urls.leadforms_page
    base_leadforms_locators = LeadFormsLocators()

    def __init__(self, driver, overview_page_class, settings_page):
        super().__init__(driver, overview_page_class=overview_page_class, settings_page_class=settings_page, leadforms_page_class=LeadformsPage)

    def get_leadform_items(self):
        return self.find_all(self.base_leadforms_locators.LEADFORM_ITEM, 15)

    def remove_leadform_item(self, index):
        item = self.get_leadform_items()[index]
        item.find_element(*self.base_leadforms_locators.LEADFORM_ITEM_CHECKBOX).click()
        self.find_all(self.base_leadforms_locators.LEADFORM_STATUS_DROPDOWN, 15)[1].click()

    def open_new_form(self):
        self.click(self.base_leadforms_locators.CREATE_LEAD_FORM, 30)
    
    def get_create_landing_switch(self):
        return self.find(self.base_leadforms_locators, 15)

    def turn_off_create_landing(self):
        create_landing_switch = self.get_create_landing_switch()
        checkbox = create_landing_switch.find_element(*self.base_locators.CHECKBOX, 15)
        
        if checkbox.is_selected():
            create_landing_switch.click()

    def turn_on_create_landing(self):
        create_landing_switch = self.get_create_landing_switch()
        checkbox = create_landing_switch.find_element(*self.base_locators.CHECKBOX)

        if not checkbox.is_selected():
            create_landing_switch.click()
    
    def get_new_leadform_inputs(self):
        return self.find_all(self.base_leadforms_locators.NEW_LEADFORM_INPUTS, 15)
    
    def get_name_input(self):
        inputs = self.get_new_leadform_inputs()
        return inputs[INPUT_INDEXES['name']]
    
    def get_header_input(self):
        inputs = self.get_new_leadform_inputs()
        return inputs[INPUT_INDEXES['header']]
    
    def get_description_input(self):
        inputs = self.get_new_leadform_inputs()
        return inputs[INPUT_INDEXES['description']]
    
    def open_add_logo(self):
        self.click(self.base_leadforms_locators.ADD_LOGO, 15)
    
    def wait_until_sidebar_closed(self):
        self.wait(15).until(EC.invisibility_of_element_located(self.base_leadforms_locators.LOAD_IMAGE_SIDEBAR))
    
    def find_add_logo_input(self):
        sidebar = self.find(self.base_leadforms_locators.LOAD_IMAGE_SIDEBAR, 15)
        load_image_input = sidebar.find_element(*self.base_leadforms_locators.LOAD_IMAGE)
        return load_image_input

    def upload_new_logo(self, src):
        self.open_add_logo()
        self.find_add_logo_input().send_keys(src)
        self.click(self.base_leadforms_locators.UPLOADED_IMAGE_ITEM)

    def next_page(self):
        self.click(self.base_leadforms_locators.CONTINUE, 15)
    
    def select_small_form(self):
        self.find_all(self.base_leadforms_locators.FORM_TYPE, 15)[FORM_TYPES_INDEXES['small']].click()

    def select_big_form(self):
        self.find_all(self.base_leadforms_locators.FORM_TYPE, 15)[FORM_TYPES_INDEXES['big']].click()
    
    def select_magnet_form(self):
        self.find_all(self.base_leadforms_locators.FORM_TYPE, 15)[FORM_TYPES_INDEXES['magnet']].click()

    def get_current_step(self):
        return self.find(self.base_leadforms_locators.ACTIVE_STEP).text

    def fill_main_leadform_data(self, name, company_name, header, description, type):
        inputs = self.get_new_leadform_inputs()
        inputs[INPUT_INDEXES['name']].clear()
        inputs[INPUT_INDEXES['name']].send_keys(name)
        inputs[INPUT_INDEXES['company_name']].clear()
        inputs[INPUT_INDEXES['company_name']].send_keys(company_name)
        inputs[INPUT_INDEXES['header']].clear()
        inputs[INPUT_INDEXES['header']].send_keys(header)
    
    def fill_small_leadform_data(self, description):
        inputs = self.get_new_leadform_inputs()
        inputs[INPUT_INDEXES['description']].clear()
        inputs[INPUT_INDEXES['description']].send_keys(description)

    def fill_big_leadform_data(self, description):
        input = self.find(self.base_leadforms_locators.BIG_FORM_DESCRIPTION)
        input.clear()
        input.send_keys(description)
    
    def select_rubles_discount(self):
        self.find_all(self.base_leadforms_locators.DISCOUNT_TYPE, 15)[0].click()

    def select_percent_discount(self):
        self.find_all(self.base_leadforms_locators.DISCOUNT_TYPE, 15)[1].click()

    def fill_discount_rubles_leadform_data(self, discount):
        self.select_rubles_discount()
        self.input(self.base_leadforms_locators.DISCOUNT_INPUT, discount, 15)

    def fill_discount_percent_leadform_data(self, discount):
        self.select_percent_discount()
        self.input(self.base_leadforms_locators.DISCOUNT_INPUT, discount, 15)
    
    def click_add_question(self):
        self.find_all(self.base_leadforms_locators.ADD_BUTTON, 15)[0].click()
    
    def remove_question(self, index=0):
        self.find_all(self.base_leadforms_locators.REMOVE_QUESTION)[index].click()

    def get_questions(self):
        self.find_all(self.base_leadforms_locators.QUESTION, 15)
    
    def fill_agreement(self, surname, address, email=None, INN=None):
        inputs = self.get_new_leadform_inputs()
        inputs[AGREEMENT_INPUTS_INDEXES['surname']].clear()
        inputs[AGREEMENT_INPUTS_INDEXES['surname']].send_keys(surname)
        inputs[AGREEMENT_INPUTS_INDEXES['address']].clear()
        inputs[AGREEMENT_INPUTS_INDEXES['address']].send_keys(address)

        if email != None:
            inputs[AGREEMENT_INPUTS_INDEXES['email']].clear()
            inputs[AGREEMENT_INPUTS_INDEXES['email']].send_keys(email)
            
        if INN != None:
            inputs[AGREEMENT_INPUTS_INDEXES['INN']].clear()
            inputs[AGREEMENT_INPUTS_INDEXES['INN']].send_keys(INN)
            
    