from page_objects.base_page import BasePage
from locators.order_page_locators import OrderPageLocators, OrderModalConfirmationLocators, OrderModalSuccessfulLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class OrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def enter_name(self, text):
        self.enter_test(OrderPageLocators.INPUT_NAME, text)

    def enter_surname(self, text):
        self.enter_test(OrderPageLocators.INPUT_SURNAME, text)

    def enter_address(self, text):
        self.enter_test(OrderPageLocators.INPUT_ADDRESS, text)

    def enter_metro_station(self):
        self.enter_form_click(OrderPageLocators.INPUT_METRO_STATION, OrderPageLocators.BUTTON_STATION_METRO)

    def enter_phone(self, text):
        self.enter_test(OrderPageLocators.INPUT_PHONE, text)

    def click_button_next(self):
        self.driver.find_element(*OrderPageLocators.BUTTON_NEXT).click()

    def enter_deliver(self):
        self.enter_form_click(OrderPageLocators.WHEN_DELIVER, OrderPageLocators.CHECKBOX_TODAY)

    def enter_time_rental(self):
        self.enter_form_click(OrderPageLocators.TIME_RENTAL, OrderPageLocators.TIME_RENTAL_DURATION)

    def click_button_order(self):
        self.driver.find_element(*OrderPageLocators.BUTTON_ORDER).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(
                                                                            OrderModalConfirmationLocators.BUTTON_YES))

    def filling_out_form_order(self, name, surname, address, phone):
        self.enter_name(name)
        self.enter_surname(surname)
        self.enter_address(address)
        self.enter_metro_station()
        self.enter_phone(phone)
        self.click_button_next()

    def filling_out_form_rental(self):
        self.enter_deliver()
        self.enter_time_rental()
        self.click_button_order()


class OrderModalConfirmation(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_button_confirmation(self):
        self.driver.find_element(*OrderModalConfirmationLocators.BUTTON_YES).click()


class OrderModalSuccessful(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_button_confirmation(self):
        self.driver.find_element(*OrderModalSuccessfulLocators.BUTTON_VIEW_STATUS).click()

