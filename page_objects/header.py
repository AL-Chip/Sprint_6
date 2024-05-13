from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class Header(BasePage):

    _BUTTON_ORDER_HEADER = By.XPATH, "//*[contains(@class, 'Header_Nav')]/button[text() = 'Заказать']" # Кнопка заказа\
    _LOGO_SCOOTER = By.XPATH, "//*[contains(@class, 'Header_LogoScooter')]"
    _LINK_YANDEX = By.XPATH, "//*[contains(@class, 'Header_LogoYandex')]"

    def click_button_order(self):
        self.driver.find_element(*self._BUTTON_ORDER_HEADER).click()

    def click_link_logo(self):
        self.driver.find_element(*self._LOGO_SCOOTER).click()

    def click_link_yandex(self):
        self.driver.find_element(*self._LINK_YANDEX).click()
