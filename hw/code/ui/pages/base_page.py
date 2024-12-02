import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DEFAULT_TIMER_LENGTH = 5

class PageNotOpenedExeption(Exception):
    pass

class BasePage(object):
    url = 'https://ads.vk.com/'

    def __init__(self, driver):
        self.driver = driver
        self.is_opened()
        
    def is_opened(self, timeout=15):
        started = time.time()
        while time.time() - started < timeout:
            if self.driver.current_url.find(self.url) != -1:
                return True
        raise PageNotOpenedExeption(f'{self.url} did not open in {timeout} sec, current url {self.driver.current_url}')

    def wait(self, timeout=DEFAULT_TIMER_LENGTH):
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=DEFAULT_TIMER_LENGTH):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))
    
    def click(self, locator, timeout=DEFAULT_TIMER_LENGTH) -> WebElement:
        self.find(locator, timeout=timeout)
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        elem.click()