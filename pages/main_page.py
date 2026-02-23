from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    URL = "https://selectel.ru"
    LOGIN_BUTTON = (By.XPATH, "//a[contains(text(), 'Войти')]")

    def open(self):
        super().open(self.URL)

    def is_login_button_visible(self):
        return self.find_element(self.LOGIN_BUTTON).is_displayed()