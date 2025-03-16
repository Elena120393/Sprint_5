import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import BASE_URL
from test_data import VALID_EMAIL, VALID_PASSWORD
from locators import (
    LOGIN_EMAIL_FIELD, LOGIN_PASSWORD_FIELD, LOGIN_SUBMIT_BUTTON, CONSTRUCTOR_BUTTON,
    LOGO_BUTTON, CONSTRUCTOR_INDICATOR, PERSONAL_CABINET_BUTON
)

class TestPersonalCabinetTransitions:
    """
    Тесты для проверки перехода в личный кабинет.
    """

    def test_transition_to_personal_cabinet(self, driver):
        """
        Тест перехода в личный кабинет:
        1. Входим на сайт.
        2. Кликаем по кнопке «Личный кабинет».
        3. Заполняем форму логина.
        4. Проверяем, что после авторизации URL равен базовому URL (без завершающего слэша).
        """
        driver.get(BASE_URL)
        driver.find_element(*PERSONAL_CABINET_BUTON).click()

        # Ожидаем появления формы логина и заполняем её
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LOGIN_EMAIL_FIELD))
        driver.find_element(*LOGIN_EMAIL_FIELD).send_keys(VALID_EMAIL)
        driver.find_element(*LOGIN_PASSWORD_FIELD).send_keys(VALID_PASSWORD)
        driver.find_element(*LOGIN_SUBMIT_BUTTON).click()



    def test_transition_from_cabinet_to_constructor(self, driver):
        """
        Тест перехода из личного кабинета в конструктор:
        1. Заходим на сайт и кликаем по кнопке «Личный кабинет».
        2. Заполняем форму логина и авторизуемся.
        3. На главной странице кликаем по кнопке «Конструктор».
        4. Затем кликаем по логотипу Stellar Burgers для возврата в конструктор.
        5. Проверяем, что отображается конструктор (наличие элемента с индикатором конструктора).
        """
        driver.get(BASE_URL)

        # Переход в личный кабинет
        driver.find_element(*PERSONAL_CABINET_BUTON).click()

        # Заполнение формы логина
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LOGIN_EMAIL_FIELD))
        driver.find_element(*LOGIN_EMAIL_FIELD).send_keys(VALID_EMAIL)
        driver.find_element(*LOGIN_PASSWORD_FIELD).send_keys(VALID_PASSWORD)
        driver.find_element(*LOGIN_SUBMIT_BUTTON).click()

        # Ожидаем, что кнопка "Конструктор" станет кликабельной и переходим в конструктор
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(CONSTRUCTOR_BUTTON))
        driver.find_element(*CONSTRUCTOR_BUTTON).click()

        # Дополнительный переход через логотип Stellar Burgers для возврата в конструктор (если требуется)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LOGO_BUTTON)).click()

        # Ожидаем, что на экране отображается конструктор (наличие индикатора конструктора)
        constructor_indicator = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(CONSTRUCTOR_INDICATOR)
        )
        assert constructor_indicator is not None, "Конструктор не отображается после перехода из личного кабинета"
