from selenium.webdriver.common.by import By


class HeaderLocators:

    BUTTON_ORDER_HEADER = By.XPATH, "//*[contains(@class, 'Header_Nav')]/button[text() = 'Заказать']" # Кнопка заказа\
    LOGO_SCOOTER = By.XPATH, "//*[contains(@class, 'Header_LogoScooter')]"
    LINK_YANDEX = By.XPATH, "//*[contains(@class, 'Header_LogoYandex')]"
