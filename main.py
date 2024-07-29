from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

def main():
    # Запрашиваем номер телефона у пользователя
    phone_number = input("Введите номер телефона: ")

    # Опции для Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # если не нужен GUI
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Путь к ChromeDriver
    service = Service('D:/Робочий стол/bomb/bomb/chromedriver.exe')  # Укажите путь к вашему chromedriver

    # Инициализация драйвера
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Открываем веб-сайт
        driver.get("https://podorozhnyk.ua/")

        # Ждем, чтобы страница полностью загрузилась
        time.sleep(5)

        # Находим поле ввода номера телефона
        phone_input = driver.find_element(By.CSS_SELECTOR, 'input[type="tel"]')

        # Вводим номер телефона
        phone_input.send_keys(phone_number)

        # Вариант: нажать Enter (если требуется)
        # phone_input.send_keys(Keys.RETURN)

        # Задержка, чтобы увидеть результат (если не в headless режиме)
        time.sleep(5)
    
    finally:
        # Закрываем браузер
        driver.quit()

if __name__ == "__main__":
    main()
