from page_objects.base_page import BasePage
from locators.header_locators import HeaderLocators


class Header(BasePage):

    def click_button_order(self):
        self.driver.find_element(*HeaderLocators.BUTTON_ORDER_HEADER).click()

    def click_link_logo(self):
        self.driver.find_element(*HeaderLocators.LOGO_SCOOTER).click()

    def click_link_yandex(self):
        self.driver.find_element(*HeaderLocators.LINK_YANDEX).click()
