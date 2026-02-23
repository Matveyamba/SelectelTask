from pages.base_page import BasePage


class MainPage(BasePage):

    def open(self):
        super().open("https://selectel.ru")