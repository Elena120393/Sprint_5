
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import BASE_URL
from test_data import VALID_EMAIL, VALID_PASSWORD
from locators import LOGIN_EMAIL_FIELD, LOGIN_PASSWORD_FIELD, LOGIN_SUBMIT_BUTTON, LOGOUT_BUTTON, PERSONAL_CABINET_BUTON

class TestLogout:
    """
    Класс с тестами для проверки функционала выхода из аккаунта.
    """

    def test_logout(self, driver):
        """
        Тест выхода из аккаунта:
        1. Заходим на главную страницу и кликаем по кнопке «Личный кабинет» для входа.
        2. Вводим данные для авторизации и нажимаем «Войти».
        3. После входа кликаем по кнопке «Личный кабинет» для вызова меню аккаунта.
        4. Дожидаемся кликабельности кнопки «Выход» и кликаем по ней.
        5. Проверяем, что после логаута отображается форма для ввода логина.
        """
        driver.get(BASE_URL)

        # Кликаем по кнопке "Личный кабинет"
        driver.find_element(*PERSONAL_CABINET_BUTON).click()

        # Ожидаем появления формы логина и заполняем её
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LOGIN_EMAIL_FIELD))
        driver.find_element(*LOGIN_EMAIL_FIELD).send_keys(VALID_EMAIL)
        driver.find_element(*LOGIN_PASSWORD_FIELD).send_keys(VALID_PASSWORD)
        driver.find_element(*LOGIN_SUBMIT_BUTTON).click()

        # Кликаем по кнопке "Личный кабинет" для вызова меню аккаунта
        driver.find_element(*PERSONAL_CABINET_BUTON).click()

        # Явное ожидание появления и кликабельности кнопки "Выход"
        logout_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LOGOUT_BUTTON))
        logout_button.click()

        # Проверяем появление формы ввода логина после выхода из аккаунта
        login_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LOGIN_EMAIL_FIELD))
        assert login_field is not None, "После выхода из аккаунта не отображается форма логина"