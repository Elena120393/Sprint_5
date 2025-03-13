
from selenium.webdriver.common.by import By
from urls import BASE_URL
from locators import BUNS_TAB, SAUCES_TAB, FILLINGS_TAB

class TestTabNavigation:
    def test_button_navigation_to_buns_tab(self, driver):
        # Переход на главную страницу
        driver.get(BASE_URL)
        # Переход в раздел "Булки"
        driver.find_element(*BUNS_TAB).click()
        # Проверка, что мы в разделе "Булки"
        buns_page = driver.find_element(*BUNS_TAB)
        assert buns_page.is_displayed(), "Не удалось перейти в раздел Булки."

    def test_button_navigation_to_sauces_tab(self, driver):
        # Переход на главную страницу
        driver.get(BASE_URL)
        # Переход в раздел "Соусы"
        driver.find_element(*SAUCES_TAB).click()
        # Проверка, что мы в разделе "Соусы"
        sauces_page = driver.find_element(*SAUCES_TAB)
        assert sauces_page.is_displayed(), "Не удалось перейти в раздел Соусы."

    def test_button_navigation_to_fillings_tab(self, driver):
        # Переход на главную страницу
        driver.get(BASE_URL)
        # Переход в раздел "Начинки"
        driver.find_element(*FILLINGS_TAB).click()
        # Проверка, что мы в разделе "Начинки"
        fillings_page = driver.find_element(*FILLINGS_TAB)
        assert fillings_page.is_displayed(), "Не удалось перейти в раздел Начинки."
