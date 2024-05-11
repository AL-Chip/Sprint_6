from locators.home_pages_locators import HomePageLocators
from page_objects.base_page import BasePage
from config import URl


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def open_home_page(self):
        self.navigate(URl, HomePageLocators.FAQ_QUESTION_FIRST_TITLE)

    def click_faq_question(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def check_attribute(self, locator):
        return self.driver.find_element(*locator).get_attribute('aria-disabled')

    def check_display_question_text(self, locator):
        return self.driver.find_element(*locator).get_attribute('hidden')







