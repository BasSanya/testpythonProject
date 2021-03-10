from selenium import webdriver
import time
import os

try:

    driver = webdriver.Chrome()
    driver.get('http://suninjuly.github.io/file_input.html')

    #elements
    f_name = driver.find_element_by_css_selector('[name="firstname"]')
    l_name = driver.find_element_by_css_selector('[name="lastname"]')
    email = driver.find_element_by_css_selector('[name="email"]')
    file_load = driver.find_element_by_id('file')
    curent_path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(curent_path, 'test_file.txt')
    btn = driver.find_element_by_css_selector('[type="submit"]')

    #filling
    f_name.send_keys('Sasha')
    l_name.send_keys('Sir')
    email.send_keys('ssir@mail.me')
    file_load.send_keys(file_path)

    btn.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    driver.quit()