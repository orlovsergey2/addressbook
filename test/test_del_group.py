# test/test_del_group.py
import pytest
from application.application import Application  # Импортируем класс Application
from selenium.webdriver.common.by import By
from confest import app
def test_del_group(app):
    """Тест для удаления группы"""
    app.group.open_group_page()
    app.driver.find_element(By.NAME, "selected[]").click()  # Выбор группы
    app.driver.find_element(By.NAME, "delete").click()      # Удаление группы
    app.group.return_to_groups_page()                      # Возврат на страницу групп