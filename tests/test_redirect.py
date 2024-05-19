import time
from page_objects.home_page import HomePage
from page_objects.header import Header
from page_objects.order_page import OrderPage, OrderModalConfirmation, OrderModalSuccessful
from config import USER_SHERLOK, USER_JOHN, URL, DZEN_URL
import pytest
import allure


class TestRedirect:

    @allure.title('Проверка редиректа на главную при нажатии на лого')
    @pytest.mark.parametrize('name, surname, address, phone', [USER_SHERLOK])
    def test_redirect_on_home_page(self, driver, name, surname, address, phone):
        home_page = HomePage(driver)
        order_page = OrderPage(driver)
        header = Header(driver)
        order_modal_page = OrderModalConfirmation(driver)
        order_modal_successful = OrderModalSuccessful(driver)
        home_page.open_home_page()
        header.click_button_order()
        order_page.filling_out_form_order(name, surname, address, phone)
        order_page.filling_out_form_rental()
        order_modal_page.click_button_confirmation()
        order_modal_successful.click_button_confirmation()
        header.click_link_logo()
        assert driver.current_url == URL

    @allure.title('Проверка редиректа на страницу яндекс дзен при нажатии на логотип яндекса')
    @pytest.mark.parametrize('name, surname, address, phone', [USER_JOHN])
    def test_redirect_on_yandex_zen(self, driver, name, surname, address, phone):
        home_page = HomePage(driver)
        order_page = OrderPage(driver)
        header = Header(driver)
        order_modal_page = OrderModalConfirmation(driver)
        order_modal_successful = OrderModalSuccessful(driver)
        home_page.open_home_page()
        header.click_button_order()
        order_page.filling_out_form_order(name, surname, address, phone)
        order_page.filling_out_form_rental()
        order_modal_page.click_button_confirmation()
        order_modal_successful.click_button_confirmation()
        header.click_link_yandex()
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[1])
        url = driver.current_url
        assert DZEN_URL in url

