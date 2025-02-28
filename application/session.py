from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        """Авторизация"""
        self.app.driver.get(self.app.base_url)  # Открываем главную страницу
        self.app.type(By.NAME, "user", username)  # Вводим логин
        self.app.type(By.NAME, "pass", password)  # Вводим пароль
        self.app.driver.find_element(By.XPATH, "//input[@value='Login']").click()  # Кликаем на кнопку входа

        # Проверка успешной авторизации
        WebDriverWait(self.app.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Logout")))

    def ensure_logout(self):
        """Завершает сеанс пользователя."""
        self.app.driver.find_element(By.LINK_TEXT, "Logout").click()
