

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


PASSWORD_RECOVERY_LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")
from locators import BASE_URL,  VALID_EMAIL,  VALID_PASSWORD, LOGIN_EMAIL_FIELD, LOGIN_PASSWORD_FIELD, LOGIN_SUBMIT_BUTTON, HOME_LOGIN_BUTTON, ORDER_BUTTON, REGISTRATION_LOGIN_LINK, CONSTRUCTOR_BUTTON, BUNS_TAB, LOGO, LOGOUT_BUTTON, LOGO_BUTTON, CONSTRUCTOR_INDICATOR, SAUCES_TAB, FILLINGS_TAB, PERSONAL_CABINET_BUTON


def test_login_from_homepage(driver):
    """
       Тест входа по кнопке «Войти в аккаунт» на главной странице.
       1. Открывается главная страница.
       2. Нажимается кнопка «Войти в аккаунт».
       3. Заполняется форма входа: ввод email и password.
       4. Нажимается кнопка входа.
       5. Открывается главная страница.
       6. Проверяется наличие кнопки "Оформить заказ".
       """
    driver.get(BASE_URL)

    # Ждем, пока кнопка "Войти в аккаунт" станет кликабельной и нажимаем по ней
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(HOME_LOGIN_BUTTON))
    driver.find_element(*HOME_LOGIN_BUTTON).click()

    # Ожидание страницы логина: дожидаемся появления поля ввода email
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LOGIN_EMAIL_FIELD))

    # Заполнение формы входа
    driver.find_element(*LOGIN_EMAIL_FIELD).send_keys(VALID_EMAIL)
    driver.find_element(*LOGIN_PASSWORD_FIELD).send_keys(VALID_PASSWORD)

    # Нажатие на кнопку входа
    driver.find_element(*LOGIN_SUBMIT_BUTTON).click()


    # Ожидание появления кнопки "Оформить заказ" на главной странице
    order_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(ORDER_BUTTON)
    )

    # Assert на наличие кнопки "Оформить заказ"
    assert order_button is not None, "Кнопка 'Оформить заказ' не найдена на главной странице после входа"

    # Закрытие драйвера
    driver.quit()


def test_login_from_personal_cabinet_button(driver):
    """
    Тест входа через кнопку «Личный кабинет».
    1. Открывается главная страница.
    2. Нажимается кнопка "Личный кабинет".
    3. На странице логина заполняется форма входа: ввод email и password.
    4. Нажимается на кнопку "Войти".
    5. После успешного входа, открывается главная страница.
    6. Проверяется наличие кнопки "Оформить заказ".
    """
    driver.get(BASE_URL)

    # Нажимаем на кнопку "Личный кабинет"
    driver.find_element(*PERSONAL_CABINET_BUTON).click()

    # Заполняем форму входа: ввод email
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys(VALID_EMAIL)

    # Вводим пароль
    driver.find_element(By.CSS_SELECTOR, "input.text.input__textfield.text_type_main-default[name='Пароль']").send_keys(
        VALID_PASSWORD)

    # Нажимаем на кнопку "Войти"
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()

    # Ожидаем появления кнопки "Оформить заказ" на главной странице
    order_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Оформить заказ')]"))
    )

    # Проверяем, что кнопка присутствует
    assert order_button is not None, "Кнопка 'Оформить заказ' не найдена на странице"

    # Закрытие драйвера
    driver.quit()





def test_login_from_registration_form(driver):

    """
        Тест входа через переход из формы регистрации.
        1. Открывается страница для регистрации.
        2. Нажимается на кнопку "Войти".
        3. На странице логина заполняется форма входа: ввод email и password.
        4. Нажимается на кнопку "Войти".
        5. После успешного входа, открывается главная страница.
        6. Проверяется наличие кнопки "Оформить заказ".
        """
    driver.get(f"{BASE_URL}/register")

    # Ждем, пока ссылка "Войти" станет кликабельной и кликаем по ней
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(REGISTRATION_LOGIN_LINK))
    driver.find_element(*REGISTRATION_LOGIN_LINK).click()

    # Заполнение формы логина
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LOGIN_EMAIL_FIELD))
    driver.find_element(*LOGIN_EMAIL_FIELD).send_keys(VALID_EMAIL)
    driver.find_element(*LOGIN_PASSWORD_FIELD).send_keys(VALID_PASSWORD)
    driver.find_element(*LOGIN_SUBMIT_BUTTON).click()

    # Ожидание появления кнопки "Оформить заказ" на главной странице
    order_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ORDER_BUTTON))

    # Проверка наличия кнопки "Оформить заказ"
    assert order_button is not None, "Кнопка 'Оформить заказ' не найдена на странице"

    # Закрытие драйвера
    driver.quit()


def test_login_from_password_recovery(driver):
    """
    Тест входа через переход из формы восстановления пароля (кликаем по ссылке 'Войти').
    1. Открывается страница восстановления пароля.
    2. Кликается по ссылке "Войти" для перехода на форму логина.
    3. Заполняется форма входа: ввод email и password.
    4. Нажимается на кнопку "Войти".
    5. Ожидается переход на главную страницу и проверяется наличие кнопки "Оформить заказ".
    """
    # Переходим на страницу восстановления пароля
    driver.get(f"{BASE_URL}/forgot-password")

    # Ожидаем, пока ссылка "Войти" станет кликабельной, и кликаем по ней
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(PASSWORD_RECOVERY_LOGIN_LINK))
    driver.find_element(*PASSWORD_RECOVERY_LOGIN_LINK).click()

    # Заполнение формы логина
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LOGIN_EMAIL_FIELD))
    driver.find_element(*LOGIN_EMAIL_FIELD).send_keys(VALID_EMAIL)
    driver.find_element(*LOGIN_PASSWORD_FIELD).send_keys(VALID_PASSWORD)
    driver.find_element(*LOGIN_SUBMIT_BUTTON).click()

    # Ожидаем появления кнопки "Оформить заказ" на главной странице
    order_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ORDER_BUTTON))

    # Проверяем, что кнопка "Оформить заказ" присутствует
    assert order_button is not None, "Кнопка 'Оформить заказ' не найдена на странице после входа"

    # Закрытие драйвера
    driver.quit()

