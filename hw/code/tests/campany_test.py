import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def get_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
def test_homepage_title(get_driver):
    get_driver.get("https://vk.com")

def test_element_exists(get_driver):
    get_driver.get("https://vk.com")
