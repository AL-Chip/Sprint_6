from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def navigate(self, url: str, locator):
        self.driver.get(url)
        WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(locator))

