import requests
from pages.main_page import MainPage

BASE_URL = "https://selectel.ru"


def test_main_page_status_code():
    response = requests.get(BASE_URL)
    assert response.status_code == 200

def test_main_page_title(driver):
    driver.get("https://selectel.ru")
    assert "Selectel" in driver.title

def test_main_page_title(driver):
    page = MainPage(driver)
    page.open()
    assert "Selectel" in page.get_title()

def test_login_button(driver):
    page = MainPage(driver)
    page.open()
    assert page.is_login_button_visible()