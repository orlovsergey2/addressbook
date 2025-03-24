# application/application.py
from selenium import webdriver
from .contact_helper import ContactHelper
from .group_helper import GroupHelper
from .session import SessionHelper

class Application:
    def __init__(self, browser="firefox"):
        if browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser == "edge":
            self.driver = webdriver.Edge()
        else:
            raise ValueError(f"Unsupported browser: {browser}")

        self.base_url = "http://localhost/addressbook/addressbook/"
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.session = SessionHelper(self)
        self.verificationErrors = []

    def is_valid(self):
        try:
            self.driver.current_url
            return True
        except:
            return False

    def open_home_page(self):
        self.driver.get(self.base_url)

    def tear_down(self):
        self.driver.quit()

    def type(self, locator_type, locator, text):
        if text is not None:
            self.driver.find_element(locator_type, locator).clear()
            self.driver.find_element(locator_type, locator).send_keys(text)