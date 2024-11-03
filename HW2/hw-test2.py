from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Инициализация веб-драйвера
driver = webdriver.Chrome()  # Используйте ваш драйвер по умолчанию
driver.get("https://example.com/login")  # URL страницы входа

# Вход на сайт
username = driver.find_element(By.NAME, "username")
password = driver.find_element(By.NAME, "password")
username.send_keys("ваш_логин")
password.send_keys("ваш_пароль")
driver.find_element(By.NAME, "submit").click()

# Ожидание перехода на главную страницу
WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))

# Шаг для добавления нового поста
driver.get("https://example.com/new_post")  # URL страницы создания поста

# Заполнение формы создания поста
post_title = "Новый пост"
post_description = "Это описание нового поста."
driver.find_element(By.NAME, "title").send_keys(post_title)
driver.find_element(By.NAME, "description").send_keys(post_description)

# Ожидание перед нажатием кнопки создания поста
time.sleep(2)  # Небольшая задержка
driver.find_element(By.NAME, "create_post").click()

# Ожидание перехода на страницу с созданным постом
WebDriverWait(driver, 10).until(EC.url_contains("posts"))

# Проверка наличия названия поста на странице
time.sleep(2)  # Ожидание загрузки страницы
posts = driver.find_elements(By.CLASS_NAME, "post-title")  # Предполагается, что заголовки имеют этот класс

# Поиск названия поста на странице
if any(post.text == post_title for post in posts):
    print("Пост успешно добавлен и найден на странице.")
else:
    print("Пост не найден на странице.")

# Закрытие драйвера
driver.quit()