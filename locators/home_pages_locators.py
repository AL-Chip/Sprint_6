from selenium.webdriver.common.by import By


class HomePageLocators:
    LIST_QUESTION_TITLE = By.XPATH, "//*[contains(@id, 'accordion__heading')]" # Список вопросов в блоке "Вопросы о важном"
    LIST_QUESTION_TEXT = By.XPATH, "//*[contains(@id, 'accordion__panel')]" # Список ответов на вопросы в блоке "Вопросы о важном"
    FAQ_QUESTION_FIRST_TITLE = By.XPATH, "//*[@id='accordion__heading-0']" # Заголовок первого вопроса в блоке "Вопросы о важном"
    BUTTON_ORDER = By.XPATH, "//*[contains(@class, 'Home_FinishButton')]/button" # Кнопка заказа
