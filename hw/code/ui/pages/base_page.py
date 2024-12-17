import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DEFAULT_TIMER_LENGTH = 0
DEFAULT_IMPLICIT_WAIT = 1

class PageNotOpenedExeption(Exception):
    pass


class BasePage(object):
    url = 'https://ads.vk.com/'

    def __init__(self, driver):
        self.driver = driver
        
    def is_opened(self, timeout=10):
        started = time.time()
        while time.time() - started < timeout:
            if self.driver.current_url.split('?')[0] == self.url:
                return True
        raise PageNotOpenedExeption(f'{self.url} did not open in {timeout} sec, current url {self.driver.current_url}')

    def wait(self, timeout=DEFAULT_TIMER_LENGTH):
        if timeout is None:
            timeout = DEFAULT_TIMER_LENGTH
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=DEFAULT_TIMER_LENGTH):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))
    
    def click(self, locator, timeout=DEFAULT_TIMER_LENGTH) -> WebElement:
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        elem.click()
    
    def find_all(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_all_elements_located(locator))

    def input(self, input_field, data, timeout=DEFAULT_TIMER_LENGTH):
        elem = self.find(input_field, timeout)
        elem.clear()
        elem.send_keys(data)    

    def is_on_page(self, text):
        return text in self.driver.page_source
