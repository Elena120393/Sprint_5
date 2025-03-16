
import time
from selenium.webdriver.common.by import By


# Локаторы для страницы регистрации
NAME_FIELD = (By.XPATH, "//input[@name='name']")
EMAIL_FIELD = (By.XPATH, "//label[normalize-space()='Email']/following-sibling::input")
PASSWORD_FIELD = (By.NAME, "Пароль")

REGISTER_BUTTON = (By.XPATH, "//button[normalize-space()='Зарегистрироваться']")
# Локатор сообщения об ошибке (для некорректного пароля)
INVALID_PASSWORD_ERROR = (By.XPATH, "//*[contains(text(), 'Некорректный пароль')]")

# Локаторы для входа
# На главной странице (кнопка "Войти в аккаунт")
HOME_LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")


# Локатор для кнопки "Личный кабинет"
PERSONAL_CABINET_BUTTON = (By.XPATH, "//*[text()='Личный кабинет']")

# Локаторы для формы логина, используемые в тесте "test_login_from_personal_cabinet_button"
LOGIN_EMAIL_FIELD = (By.CSS_SELECTOR, "input.text.input__textfield.text_type_main-default[name='name']")
LOGIN_PASSWORD_FIELD = (By.CSS_SELECTOR, "form input[name='Пароль']")
LOGIN_SUBMIT_BUTTON = (By.CSS_SELECTOR, "button.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa")

# Алиасы для сохранения обратной совместимости с тестами, которые ждут имена с префиксом LOGIN_FORM_
LOGIN_FORM_EMAIL_FIELD = LOGIN_EMAIL_FIELD
LOGIN_FORM_PASSWORD_FIELD = LOGIN_PASSWORD_FIELD
LOGIN_FORM_SUBMIT_BUTTON = LOGIN_SUBMIT_BUTTON


# Локаторы для проверки активного состояния табов
BUNS_TAB_ACTIVE = (By.XPATH, "//div[contains(@class, 'constructor-tab_type_current') and contains(., 'Булки')]")
SAUCES_TAB_ACTIVE = (By.XPATH, "//div[contains(@class, 'constructor-tab_type_current') and contains(., 'Соусы')]")
FILLINGS_TAB_ACTIVE = (By.XPATH, "//div[contains(@class, 'constructor-tab_type_current') and contains(., 'Начинки')]")


# Локатор индикатора успешной авторизации (наличие элемента кабинета)
PERSONAL_CABINET_INDICATOR = (By.XPATH, "//*[contains(text(), 'Личный кабинет')]")
ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")

# Локаторы для перехода в форму входа из других форм
# На странице регистрации (ссылка "Войти")
REGISTRATION_LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")
# На странице восстановления пароля (ссылка "Войти")
PASSWORD_RECOVERY_LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")


# Локаторы для перехода из личного кабинета в конструктор
CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
# Локатор логотипа Stellar Burgers, ведущего на главную/конструктор
LOGO = (By.XPATH, "//a[@href='/']")

# Локаторы для навигации в конструктор

LOGO_BUTTON = (By.XPATH, "//a[@href='/']")

# Локатор, определяющий отображение конструктора, например наличие вкладки "Булки"
CONSTRUCTOR_INDICATOR = (By.XPATH, "//*[contains(text(),'Булки')]")

# Локатор для кнопки "Выйти" в личном кабинете
LOGOUT_BUTTON = (By.XPATH, "//button[@type='button' and text()='Выход']")

#Локатор для личного кабинета
PERSONAL_CABINET_BUTON = (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText') and normalize-space(text())='Личный Кабинет']")

# Локаторы для раздела “Конструктор”
BUNS_TAB = (By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[3]/span")
SAUCES_TAB = (By.XPATH, "//span[contains(@class, 'text_type_main-default') and normalize-space(text())='Соусы']")
FILLINGS_TAB = (By.XPATH, "//span[contains(@class, 'text_type_main-default') and normalize-space(text())='Начинки']")


BUNS_IMAGE = (By.XPATH, "//img[@src='https://code.s3.yandex.net/react/code/bun-01.png' and @alt='Флюоресцентная булка R2-D3']")
SAUCE_BUTTON = (By.XPATH, "//p[@class='BurgerIngredient_ingredient__text__yp3dH' and text()='Соус традиционный галактический']")
FILLINGS_BUTTON = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6') and @href='/ingredient/61c0c5a71d1f82001bdaaa71' and contains(., 'Биокотлета из марсианской Магнолии')]")

TAB_PARENT = (By.XPATH, "./..")