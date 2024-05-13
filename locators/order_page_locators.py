from selenium.webdriver.common.by import By


class OrderPageLocators:
    INPUT_NAME = By.XPATH, "//input[contains(@placeholder, 'Имя')]" # Поле ввода имени
    INPUT_SURNAME = By.XPATH, "//input[contains(@placeholder, 'Фамилия')]"  # Поле ввода фамилии
    INPUT_ADDRESS = By.XPATH, "//input[contains(@placeholder, 'Адрес')]"  # Поле ввода адреса
    INPUT_METRO_STATION = By.XPATH, "//input[contains(@placeholder, 'Станция метро')]"  # Поле ввода станции метро
    INPUT_PHONE = By.XPATH, "//input[contains(@placeholder, 'Телефон')]"  # Поле ввода телефона
    BUTTON_STATION_METRO = By.XPATH, "//button[@value= '2']" # Станция метро "Черкизовская"
    BUTTON_NEXT = By.XPATH, "//*[contains(@class, 'Order_NextButton')]/button" # Кнопка Далее
    WHEN_DELIVER = By.XPATH, "//input[contains(@placeholder, 'Когда привезти')]" # Поле ввода даты
    CHECKBOX_TODAY = By.XPATH, "//*[contains(@class, 'keyboard-selected')]" # Чекбокс сегодняшнего дня в календаре
    TIME_RENTAL = By.XPATH, "// *[contains(text(), 'Срок аренды')]" # Поле ввода срока аренды
    TIME_RENTAL_DURATION = By.XPATH,  "//*[text() = 'сутки']" # Чекбокс продолжительности аренды на сутки
    BUTTON_ORDER = By.XPATH, "//*[contains(@class, 'Order_Buttons')]/button[text() = 'Заказать']" # Кнопка заказа


class OrderModalConfirmationLocators:
    BUTTON_YES = By.XPATH, "//button[text() = 'Да']"  # Кнопка подтверждения заказа


class OrderModalSuccessfulLocators:
    BUTTON_VIEW_STATUS = By.XPATH, "//button[text() = 'Посмотреть статус']" # Кнопка просмотра статуса заказа



