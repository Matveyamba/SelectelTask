import requests

BASE_URL = "https://selectel.ru"


def test_main_page_status_code():
    response = requests.get(BASE_URL)
    assert response.status_code == 200

def test_main_page_title(driver):
    driver.get("https://selectel.ru")
    assert "Selectel" in driver.title