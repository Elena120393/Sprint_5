
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

PASSWORD_RECOVERY_LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")
from locators import BASE_URL, VALID_EMAIL, PASSWORD_FIELD, VALID_PASSWORD, REGISTER_BUTTON,PERSONAL_CABINET_INDICATOR, INVALID_PASSWORD_ERROR, LOGIN_EMAIL_FIELD, LOGIN_EMAIL_FIELD, LOGIN_PASSWORD_FIELD, LOGIN_SUBMIT_BUTTON, HOME_LOGIN_BUTTON, HOME_LOGIN_BUTTON, PERSONAL_CABINET_BUTTON, ORDER_BUTTON, REGISTRATION_LOGIN_LINK, CONSTRUCTOR_BUTTON, BUNS_TAB, LOGO, LOGOUT_BUTTON, LOGO_BUTTON, CONSTRUCTOR_INDICATOR, SAUCES_TAB, FILLINGS_TAB, PERSONAL_CABINET_BUTON


def test_logout(driver):
    """
    Тест выхода из аккаунта:
    1. Заходим на главную страницу и кликаем по кнопке «Личный кабинет» для входа.
    2. Вводим данные для авторизации и нажимаем «Войти».
    3. После входа кликаем по кнопке «Выход».
    4. Проверяем, что после логаута обратно отображается форма для ввода логина.
    """
    driver.get(BASE_URL)

    # Кликаем по кнопке "Личный кабинет"
    driver.find_element(*PERSONAL_CABINET_BUTON).click()

    # Ожидаем появления формы логина и заполняем её
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LOGIN_EMAIL_FIELD))
    driver.find_element(*LOGIN_EMAIL_FIELD).send_keys(VALID_EMAIL)
    driver.find_element(*LOGIN_PASSWORD_FIELD).send_keys(VALID_PASSWORD)
    driver.find_element(*LOGIN_SUBMIT_BUTTON).click()

    # Кликаем по кнопке "Личный кабинет"
    driver.find_element(*PERSONAL_CABINET_BUTON).click()

    # Добавляем задержку (например, 2 секунды) перед нажатием кнопки "Выход"
    time.sleep(2)

    # Ожидаем появления и кликабельности кнопки "Выход"
    logout_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LOGOUT_BUTTON))
    logout_button.click()

    # После логаута должна отображаться форма входа – проверяем наличие поля email
    login_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LOGIN_EMAIL_FIELD))
    assert login_field is not None, "После выхода из аккаунта не отображается форма логина"

    # Закрытие драйвера
    driver.quit()
