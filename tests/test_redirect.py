import time
from selenium import webdriver
from page_objects.home_page import HomePage
from page_objects.header import Header
from page_objects.order_page import OrderPage, OrderModalConfirmation, OrderModalSuccessful
from config import USER_SHERLOK, USER_JOHN, URl
import pytest


class TestRedirect:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @pytest.mark.parametrize('name, surname, address, phone', [USER_SHERLOK])
    def test_redirect_on_home_page(self, name, surname, address, phone):
        home_page = HomePage(self.driver)
        order_page = OrderPage(self.driver)
        header = Header(self.driver)
        order_modal_page = OrderModalConfirmation(self.driver)
        order_modal_successful = OrderModalSuccessful(self.driver)
        home_page.open_home_page()
        header.click_button_order()
        order_page.filling_out_form_order(name, surname, address, phone)
        order_page.filling_out_form_rental()
        order_modal_page.click_button_confirmation()
        order_modal_successful.click_button_confirmation()
        header.click_link_logo()
        assert self.driver.current_url == URl

    @pytest.mark.parametrize('name, surname, address, phone', [USER_SHERLOK])
    def test_redirect_on_yandex_zen(self, name, surname, address, phone):
        home_page = HomePage(self.driver)
        order_page = OrderPage(self.driver)
        header = Header(self.driver)
        order_modal_page = OrderModalConfirmation(self.driver)
        order_modal_successful = OrderModalSuccessful(self.driver)
        home_page.open_home_page()
        header.click_button_order()
        order_page.filling_out_form_order(name, surname, address, phone)
        order_page.filling_out_form_rental()
        order_modal_page.click_button_confirmation()
        order_modal_successful.click_button_confirmation()
        header.click_link_yandex()
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[1])
        url = self.driver.current_url
        assert 'https://dzen.ru' in url

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
