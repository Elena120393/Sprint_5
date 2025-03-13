
import time
from selenium.webdriver.common.by import By


BASE_URL = "https://stellarburgers.nomoreparties.site"  #Базовый URL сайта

# Учетные данные для входа и регистрации
VALID_NAME = "EalenaAlena"
# Для избежания повторной регистрации генерируем уникальный email
VALID_EMAIL = "ea78elena_artemeva_19_789@gmail.com"
VALID_PASSWORD = "aelena_artemeva_19_789@gmail.com"  # Корректный пароль, длиной >= 6 символов

# Локаторы для страницы регистрации
NAME_FIELD = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input")
EMAIL_FIELD = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input")
PASSWORD_FIELD = (By.NAME, "Пароль")
REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
# Локатор сообщения об ошибке (для некорректного пароля)
INVALID_PASSWORD_ERROR = (By.XPATH, "//*[contains(text(), 'Некорректный пароль')]")

# Локаторы для входа
# На главной странице (кнопка "Войти в аккаунт")
HOME_LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
# На странице входа (форма)
LOGIN_EMAIL_FIELD = (By.CSS_SELECTOR, "#root > div > main > div > form > fieldset:nth-child(1) > div > div > input")
LOGIN_PASSWORD_FIELD = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input')
LOGIN_SUBMIT_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/form/button')

# Локатор для кнопки "Личный кабинет"
PERSONAL_CABINET_BUTTON = (By.XPATH, "//*[text()='Личный кабинет']")



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
PERSONAL_CABINET_BUTON = (By.XPATH, '//*[@id="root"]/div/header/nav/a/p')

# Локаторы для раздела “Конструктор”
BUNS_TAB = (By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[3]/span")
SAUCES_TAB = (By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[2]/span")
FILLINGS_TAB = (By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[3]/span")