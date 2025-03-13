
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PASSWORD_RECOVERY_LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")
from locators import BASE_URL, NAME_FIELD, VALID_NAME, EMAIL_FIELD, VALID_EMAIL, PASSWORD_FIELD, VALID_PASSWORD, REGISTER_BUTTON, INVALID_PASSWORD_ERROR


def test_registration_success(driver):
    """
    Тест успешной регистрации:
    1. Открывается страница регистрации.
    2. Вводятся корректные данные:
         - Имя (не пустое);
         - Email в формате login@domain, например, test_xxx@ya.ru;
         - Пароль, длиной не менее 6 символов.
    3. После нажатия на "Зарегистрироваться" ожидается появление индикатора успешной регистрации (например, "Личный кабинет").
    """
    driver.get(f"{BASE_URL}/register")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(NAME_FIELD))
    driver.find_element(*NAME_FIELD).send_keys('Alenka')
    driver.find_element(*EMAIL_FIELD).send_keys('Alenkaart_artemeva_19_789@gmail.com')
    driver.find_element(*PASSWORD_FIELD).send_keys(VALID_PASSWORD)
    driver.find_element(*REGISTER_BUTTON).click()
    # После нажатия на "Зарегистрироваться", ожидаем переход на страницу логина
    WebDriverWait(driver, 15).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login", "Переход на страницу логина не произошёл после регистрации"

    # Закрытие драйвера
    driver.quit()

def test_registration_invalid_password(driver):
    """
    Тест проверки ошибки регистрации при вводе некорректного пароля:
    1. Открывается страница регистрации.
    2. Вводятся корректные имя и email, но пароль короче 6 символов.
    3. После нажатия на "Зарегистрироваться" ожидается сообщение об ошибке.
    """
    driver.get(f"{BASE_URL}/register")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(NAME_FIELD))
    driver.find_element(*NAME_FIELD).send_keys(*VALID_NAME)
    driver.find_element(*EMAIL_FIELD).send_keys(*VALID_EMAIL)
    driver.find_element(*PASSWORD_FIELD).send_keys("123")  # неправильно: менее 6 символов
    driver.find_element(*REGISTER_BUTTON).click()
    error_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(INVALID_PASSWORD_ERROR))
    assert error_element.is_displayed(), "Сообщение об ошибке некорректного пароля не отображается"

    # Закрытие драйвера
    driver.quit()
