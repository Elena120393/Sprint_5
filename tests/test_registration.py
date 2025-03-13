from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_data import VALID_NAME, VALID_PASSWORD
from urls import BASE_URL_REGISTOR
from locators import NAME_FIELD, EMAIL_FIELD, PASSWORD_FIELD, REGISTER_BUTTON, INVALID_PASSWORD_ERROR
from helpers import generate_unique_email


def test_registration_success(driver):
    """
    Тест успешной регистрации:
    1. Открывается страница регистрации.
    2. Вводятся корректные данные:
         - Имя (не пустое);
         - Email в формате login@domain, генерируется динамически;
         - Пароль, длиной не менее 6 символов.
    3. После нажатия на "Зарегистрироваться" ожидается переход на страницу логина.
    """
    driver.get(BASE_URL_REGISTOR)

    # Ожидаем видимость и заполняем поле "Имя"
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(NAME_FIELD))
    driver.find_element(*NAME_FIELD).send_keys(VALID_NAME)

    # Генерируем уникальный email для регистрации
    unique_email = generate_unique_email("ya.ru")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(EMAIL_FIELD))
    driver.find_element(*EMAIL_FIELD).send_keys(unique_email)

    # Ожидаем видимость и заполняем поле "Пароль"
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(PASSWORD_FIELD))
    driver.find_element(*PASSWORD_FIELD).send_keys(VALID_PASSWORD)

    # Ожидаем кликабельность кнопки "Зарегистрироваться" и нажимаем её
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(REGISTER_BUTTON)).click()

    # Ждем перехода на страницу логина после регистрации
    WebDriverWait(driver, 15).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login", "Переход на страницу логина не произошёл после регистрации"


def test_registration_invalid_password(driver):
    """
    Тест проверки ошибки регистрации при вводе некорректного пароля:
    1. Открывается страница регистрации.
    2. Вводятся корректные имя и email (email генерируется динамически), но пароль короче 6 символов.
    3. После нажатия на "Зарегистрироваться" ожидается сообщение об ошибке.
    """
    driver.get(BASE_URL_REGISTOR)

    # Заполняем поле "Имя"
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(NAME_FIELD))
    driver.find_element(*NAME_FIELD).send_keys(VALID_NAME)

    # Генерируем уникальный email для регистрации
    unique_email = generate_unique_email("ya.ru")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(EMAIL_FIELD))
    driver.find_element(*EMAIL_FIELD).send_keys(unique_email)

    # Заполняем поле "Пароль" некорректным значением (менее 6 символов)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(PASSWORD_FIELD))
    driver.find_element(*PASSWORD_FIELD).send_keys("123")

    # Ждем кликабельность кнопки "Зарегистрироваться" и нажимаем её
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(REGISTER_BUTTON)).click()

    # Ожидаем появления сообщения об ошибке для некорректного пароля
    error_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(INVALID_PASSWORD_ERROR))
    assert error_element.is_displayed(), "Сообщение об ошибке некорректного пароля не отображается"