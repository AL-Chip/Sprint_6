from selenium.webdriver.common.by import By


class HomePageLocators:
    LIST_QUESTION_TITLE = By.XPATH, "//*[contains(@id, 'accordion__heading')]"
    LIST_QUESTION_TEXT = By.XPATH, "//*[contains(@id, 'accordion__panel')]"
    FAQ_QUESTION_FIRST_TITLE = By.XPATH, "//*[@id='accordion__heading-0']" # Заголовок первого вопроса в блоке "Вопросы о важном"
