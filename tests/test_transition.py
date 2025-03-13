
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


PASSWORD_RECOVERY_LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")
from locators import BASE_URL, VALID_EMAIL, VALID_PASSWORD, LOGIN_EMAIL_FIELD, LOGIN_PASSWORD_FIELD, LOGIN_SUBMIT_BUTTON, CONSTRUCTOR_BUTTON, LOGO_BUTTON, CONSTRUCTOR_INDICATOR, PERSONAL_CABINET_BUTON


def test_transition_to_personal_cabinet(driver):
    """
    Тест перехода в личный кабинет:
    1. Входим на сайт.
    2. Кликаем по кнопке «Личный кабинет».
    3. Проверяем, что страница личного кабинета открыта.
    """
    driver.get(BASE_URL)
    driver.find_element(*PERSONAL_CABINET_BUTON).click()
    # Заполнение формы логина
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LOGIN_EMAIL_FIELD))
    driver.find_element(*LOGIN_EMAIL_FIELD).send_keys(VALID_EMAIL)
    driver.find_element(*LOGIN_PASSWORD_FIELD).send_keys(VALID_PASSWORD)
    driver.find_element(*LOGIN_SUBMIT_BUTTON).click()

    # Ожидаем, что URL после авторизации будет равен базовому URL
    WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
    current_url = driver.current_url
    assert current_url == "https://stellarburgers.nomoreparties.site/", f"Ожидался URL: 'https://stellarburgers.nomoreparties.site/', а получен: {current_url}"

    # Закрытие драйвера
    driver.quit()

def test_transition_from_cabinet_to_constructor(driver):
    """
    Тест перехода из личного кабинета в конструктор:
    1. Заходим на сайт и кликаем по кнопке «Личный кабинет».
    2. Заполняем форму логина и авторизуемся.
    3. На главной странице кликаем по кнопке «Конструктор».
    4. Затем кликаем по логотипу Stellar Burgers для возврата в конструктор.
    5. Проверяем, что отображается конструктор (вкладка "Булки").
    """
    driver.get(BASE_URL)

    # Кликаем по кнопке "Личный кабинет"
    driver.find_element(*PERSONAL_CABINET_BUTON).click()

    # Заполнение формы логина
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LOGIN_EMAIL_FIELD))
    driver.find_element(*LOGIN_EMAIL_FIELD).send_keys(VALID_EMAIL)
    driver.find_element(*LOGIN_PASSWORD_FIELD).send_keys(VALID_PASSWORD)
    driver.find_element(*LOGIN_SUBMIT_BUTTON).click()

    # Ожидания изменения URL и, что кнопка "Конструктор" станет кликабельной.
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(CONSTRUCTOR_BUTTON))

    # Переход в конструктор – кликаем по кнопке "Конструктор".
    driver.find_element(*CONSTRUCTOR_BUTTON).click()

    # Если требуется дополнительный переход через логотип Stellar Burgers
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LOGO_BUTTON)).click()

    # Ожидаем, что на экране отображается конструктор (наличие элемента "Булки")
    constructor_indicator = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(CONSTRUCTOR_INDICATOR))
    assert constructor_indicator is not None, "Конструктор не отображается после перехода из личного кабинета"

    # Закрытие драйвера
    driver.quit()