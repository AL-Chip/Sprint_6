from locators.home_pages_locators import HomePageLocators
import pytest
from selenium import webdriver


@pytest.fixture
def create_list_question():
    driver = webdriver.Firefox()
    return list(range(1, len(driver.find_elements(*HomePageLocators.LIST_QUESTION_TITLE))))
