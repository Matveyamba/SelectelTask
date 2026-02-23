from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.config import DEFAULT_TIMEOUT

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = DEFAULT_TIMEOUT

    def open(self, url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def find_element(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(locator)
        )

    def click(self, locator):
        self.find_element(locator).click()

    def input_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)