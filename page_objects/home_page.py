from locators.home_pages_locators import HomePageLocators
from page_objects.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from config import URl


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def open_home_page(self):
        self.navigate(URl, HomePageLocators.FAQ_QUESTION_FIRST_TITLE)

    def click_faq_question(self, number):
        element = self.driver.find_elements(*HomePageLocators.LIST_QUESTION_TITLE)[number]
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        WebDriverWait(self.driver, 5)

    def check_attribute(self, number):
        return self.driver.find_elements(*HomePageLocators.LIST_QUESTION_TITLE)[number].get_attribute('aria-disabled')

    def check_display_question_text(self, number):
        return self.driver.find_elements(*HomePageLocators.LIST_QUESTION_TEXT)[number].get_attribute('hidden')

    def click_button_order(self):
        element = self.driver.find_element(*HomePageLocators.BUTTON_ORDER)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()









