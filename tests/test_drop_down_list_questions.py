from selenium import webdriver
from page_objects.home_page import HomePage
import pytest
import allure


class TestDropDownListQuestions:

    @allure.title('Проверка выпадающего списка на главной странице')
    @pytest.mark.parametrize('number', list(range(0, 8)))
    def test_click_question(self, number, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.click_faq_question(number)
        assert (home_page.check_attribute(number) == 'true')

