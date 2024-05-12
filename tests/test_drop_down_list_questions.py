from selenium import webdriver
from page_objects.home_page import HomePage
import pytest


class TestDropDownListQuestions:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @pytest.mark.parametrize('number', list(range(0, 8)))
    def test_click_question(self, number):
        home_page = HomePage(self.driver)
        home_page.open_home_page()
        home_page.click_faq_question(number)
        assert (home_page.check_attribute(number) == 'true' and
                home_page.check_display_question_text(number) == None)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
