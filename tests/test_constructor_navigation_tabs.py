import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import BASE_URL
import pytest
from locators import BUNS_TAB, SAUCES_TAB, FILLINGS_TAB


class TestConstructorNavigation:
    """
    Класс содержит автотест для проверки перехода по табу "Булки" раздела "Конструктор".
    Для таба:
        1. Ожидается появление таба на странице.
        2. Выполняется клик по табу.
        3. Проверяется, что у родительского элемента (по xpath "./..") появляется подстрока 'current' в атрибуте "class".
    """

    def test_buns_tab_transition(self, driver):
        """
        Тест проверяет, что при клике на таб "Булки" в классе его родительского элемента появляется подстрока 'current'.
        """
        driver.get(BASE_URL)
        # Ожидаем появления таба и получаем его
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(BUNS_TAB))
        buns_tab = driver.find_element(*BUNS_TAB)
        buns_tab.click()

        # Находим родительский элемент (используя xpath './..')
        parent_element = buns_tab.find_element(By.XPATH, "./..")
        current_parent_class = parent_element.get_attribute("class")
        assert "current" in current_parent_class, (
            f"У родительского элемента таба 'Булки' ожидается наличие 'current' в классе, но получено: '{current_parent_class}'"
        )


    def test_sauces_tab_transition(self, driver):
        """
        Тест проверяет, что при клике на таб "Соусы" в классе его родительского элемента появляется подстрока 'current'.
        """
        driver.get(BASE_URL)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(SAUCES_TAB))
        sauces_tab = driver.find_element(*SAUCES_TAB)
        sauces_tab.click()

        parent_element = sauces_tab.find_element(By.XPATH, "./..")
        current_parent_class = parent_element.get_attribute("class")
        assert "current" in current_parent_class, (
            f"У родительского элемента таба 'Соусы' ожидается наличие 'current' в классе, но получено: '{current_parent_class}'"
        )

    def test_fillings_tab_transition(self, driver):
        """
        Тест проверяет, что при клике на таб "Начинки" в классе его родительского элемента появляется подстрока 'current'.
        """
        driver.get(BASE_URL)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(FILLINGS_TAB))
        fillings_tab = driver.find_element(*FILLINGS_TAB)
        fillings_tab.click()

        parent_element = fillings_tab.find_element(By.XPATH, "./..")
        current_parent_class = parent_element.get_attribute("class")
        assert "current" in current_parent_class, (
            f"У родительского элемента таба 'Начинки' ожидается наличие 'current' в классе, но получено: '{current_parent_class}'"
        )
