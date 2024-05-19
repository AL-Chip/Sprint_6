from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def navigate(self, url: str, locator):
        self.driver.get(url)
        WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(locator))

    def enter_test(self, locator, text: str):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(text)

    def enter_form_click(self, input, element):
        self.driver.find_element(*input).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(element))
        self.driver.find_element(*element).click()
