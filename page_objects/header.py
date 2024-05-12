from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class Header(BasePage):

    _BUTTON_ORDER_HEADER = By.XPATH, "//*[contains(@class, 'Header_Nav')]/button[text() = 'Заказать']" # Кнопка заказа