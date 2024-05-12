from selenium import webdriver
from page_objects.home_page import HomePage
from page_objects.order_page import OrderPage, OrderModalConfirmation, OrderModalSuccessful
from locators.order_page_locators import OrderModalSuccessfulLocators


class TestPlacingOrder:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    def test_placing_order_witch_home(self):
        home_page = HomePage(self.driver)
        order_page = OrderPage(self.driver)
        order_modal_page = OrderModalConfirmation(self.driver)
        home_page.open_home_page()
        home_page.click_button_order()
        order_page.filling_out_form_order('Александр', 'Лезин', 'Лозицкая 6', '89273840152')
        order_page.filling_out_form_rental()
        order_modal_page.click_button_confirmation()
        assert self.driver.find_element(*OrderModalSuccessfulLocators.BUTTON_VIEW_STATUS).is_displayed()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
