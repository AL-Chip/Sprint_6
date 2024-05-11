from selenium import webdriver
from page_objects.home_page import HomePage
from locators.home_pages_locators import HomePageLocators
import pytest


class TestDropDownListQuestions:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @pytest.mark.parametrize(
        'question_title,question_text',
        [
            [HomePageLocators.FAQ_QUESTION_FIRST_TITLE, HomePageLocators.FAQ_QUESTION_FIRST_TEXT],
            [HomePageLocators.FAQ_QUESTION_SECOND_TITLE, HomePageLocators.FAQ_QUESTION_SECOND_TEXT],
            [HomePageLocators.FAQ_QUESTION_THIRD_TITLE, HomePageLocators.FAQ_QUESTION_THIRD_TEXT],
            [HomePageLocators.FAQ_QUESTION_FOURTH_TITLE, HomePageLocators.FAQ_QUESTION_FOURTH_TEXT],
            [HomePageLocators.FAQ_QUESTION_FIFTH_TITLE, HomePageLocators.FAQ_QUESTION_FIFTH_TEXT],
            [HomePageLocators.FAQ_QUESTION_SIXTH_TITLE, HomePageLocators.FAQ_QUESTION_SIXTH_TEXT],
            [HomePageLocators.FAQ_QUESTION_SEVENTH_TITLE, HomePageLocators.FAQ_QUESTION_SEVENTH_TEXT],
            [HomePageLocators.FAQ_QUESTION_EIGHTH_TITLE, HomePageLocators.FAQ_QUESTION_EIGHTH_TEXT]
        ]
    )
    def test_click_first_question(self, question_title, question_text):
        home_page = HomePage(self.driver)
        home_page.open_home_page()
        home_page.click_faq_question(question_title)
        assert (home_page.check_attribute(question_title) == 'true' and
                home_page.check_display_question_text(question_text) == None)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
