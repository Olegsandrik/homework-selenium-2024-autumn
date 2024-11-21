import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_homepage_title(driver):
    driver.get("https://vk.com")



def test_element_exists(driver):
    driver.get("https://vk.com")
