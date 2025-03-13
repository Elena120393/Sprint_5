
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PASSWORD_RECOVERY_LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")
from locators import BASE_URL, BUNS_TAB, SAUCES_TAB, FILLINGS_TAB



def test_constructor_navigation_tabs(driver):
    """
    Тест переходов в разделе "Конструктор":
      1. Заходим на главную страницу.
      2. Переходим по вкладкам "Булки", "Соусы" и "Начинки" с использованием клика.
      3. Проверяем, что на странице присутствует элемент-кнопка каждой вкладки.
    """
    driver.get(BASE_URL)

    # Вкладка "Булки" - проверка наличия кнопки (изображения) для булки
    buns_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(BUNS_TAB))
    buns_element.click()
    time.sleep(3)  # Ждем обновления состояния вкладки

    # Проверяем, что на странице присутствует элемент-кнопка с изображением булки
    buns_img = driver.find_element(By.XPATH,
                                   "//img[@src='https://code.s3.yandex.net/react/code/bun-01.png' and @alt='Флюоресцентная булка R2-D3']")
    assert buns_img.is_displayed(), "Кнопка для булки не отображается, несмотря на активную вкладку 'Булки'"

    # Вкладка "Соусы": переходим на вкладку и проверяем наличие кнопки соуса
    sauces_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(SAUCES_TAB))
    sauces_element.click()
    time.sleep(3)

    # Проверяем, что на странице присутствует кнопка соуса в виде элемента <p> с нужным текстом
    sauce_button = driver.find_element(By.XPATH,
                                       "//p[@class='BurgerIngredient_ingredient__text__yp3dH' and text()='Соус традиционный галактический']")
    assert sauce_button.is_displayed(), "Кнопка 'Соус традиционный галактический' не отображается при активной вкладке 'Соусы'"

    # Вкладка "Начинки": переходим на вкладку и проверяем активность, а также отсутствие кнопки "Соус фирменный Space Sauce"
    fillings_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(FILLINGS_TAB))
    fillings_element.click()
    time.sleep(3)

    # Проверяем, что на странице присутствует кнопка в виде элемента <a> с нужными атрибутами и текстом
    fillings_button = driver.find_element(
        By.XPATH,
        "//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6') and @href='/ingredient/61c0c5a71d1f82001bdaaa71' and contains(., 'Биокотлета из марсианской Магнолии')]"
    )
    assert fillings_button.is_displayed(), "Кнопка 'Биокотлета из марсианской Магнолии' не отображается на вкладке 'Начинки'"
