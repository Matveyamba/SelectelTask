# Selectel QA Automation Tests
## 🔹 Описание
Проект содержит автоматизированные тесты для сайта [Selectel](https://selectel.ru) с использованием Python, Selenium и pytest.  
Тесты покрывают базовую проверку доступности сайта, UI и функциональные элементы.

## Реализованные проверки

### API тесты:
- Проверка доступности главной страницы (статус код 200)

### UI тесты:
- Проверка заголовка главной страницы
- Проверка видимости кнопки **"Войти"** на главной странице

## Структура проекта

selectel-tests/
│
├── pages/ # Page Object классы для страниц

│ ├── base_page.py

│ └── main_page.py

├── tests/ # Автоматизированные тесты

│ └── test_smoke.py

├── utils/ # Конфигурации и вспомогательные файлы

│ └── config.py

├── conftest.py # Фикстуры pytest

├── pytest.ini # Настройки pytest

├── requirements.txt # Зависимости Python

├── README.md

└── .gitignore


## Используемые инструменты

- Python 3.10+
- pytest 
- Selenium WebDriver 
- requests
- Google Chrome + локальный chromedriver


## Установка и запуск проекта

1. Клонируйте репозиторий:
```bash
git clone <your-repo-url>
cd selectel-tests
```

Создайте виртуальное окружение (рекомендовано):
```bash
python -m venv venv
source venv/bin/activate     # Linux / MacOS
venv\Scripts\activate        # Windows
```

Установите зависимости:
```bash
pip install -r requirements.txt
```

Убедитесь, что chromedriver установлен и находится в PATH (если не используете webdriver-manager).
Запуск всех тестов:
```bash
pytest
```
Запуск тестов с отображением подробного отчета:

```bash
pytest -v
```

## Результат запуска тестов
При успешном прохождении всех тестов вы увидите примерно такой вывод:

tests/test_smoke.py::test_main_page_status_code PASSED        [ 33%]
tests/test_smoke.py::test_main_page_title PASSED              [ 66%]
tests/test_smoke.py::test_login_button PASSED                [100%]

================================================= 3 passed in 5.23s =================================================
