from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SessionHelper:
    def __init__(self, app):
        self.app = app
        self.driver = self.app.driver

    def is_logged_in_as(self, login):
        """Проверяет, что пользователь авторизован под указанным логином."""
        # Используем относительный путь для поиска элемента <b> внутри формы
        user_element = self.driver.find_element(By.XPATH, ".//form//b")
        return user_element.text == f"({login})"

    def is_logged_in(self):
        """Проверяет, что пользователь авторизован."""
        try:
            # Используем относительный путь для поиска ссылки "Logout"
            self.driver.find_element(By.XPATH, ".//a[text()='Logout']")
            return True
        except:
            return False

    def login(self, username, password):
        """Авторизация"""
        self.driver.get(self.app.base_url)  # Открываем главную страницу
        self.app.type(By.NAME, "user", username)  # Вводим логин
        self.app.type(By.NAME, "pass", password)  # Вводим пароль
        # Используем относительный путь для поиска кнопки "Login"
        self.driver.find_element(By.XPATH, ".//input[@value='Login']").click()

        # Проверка успешной авторизации
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, ".//a[text()='Logout']"))
        )

    def logout(self):
        """Завершает сеанс пользователя."""
        # Используем относительный путь для поиска ссылки "Logout"
        self.driver.find_element(By.XPATH, ".//a[text()='Logout']").click()

    def ensure_logout(self):
        """Гарантирует, что пользователь вышел из системы."""
        if self.is_logged_in():
            self.logout()

    def ensure_login(self, username, password):
        """Гарантирует, что пользователь авторизован."""
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)