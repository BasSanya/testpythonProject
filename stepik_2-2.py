from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:

    driver = webdriver.Chrome()
    driver.get('http://suninjuly.github.io/selects2.html')

    num1 = driver.find_element_by_id('num1').text
    num2 = driver.find_element_by_id('num2').text
    operation = driver.find_element_by_css_selector('.nowrap:nth-child(3)').text
    num = None
    if operation.strip() == '+':
        num = int(num1) + int(num2)
    elif operation.strip() == '-':
        num = int(num1) - int(num2)
    else:
        num = int(num1) + int(num2)

    select = Select(driver.find_element_by_id("dropdown"))
    select.select_by_value(str(num))

    btn = driver.find_element_by_css_selector('[type="submit"]')
    btn.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    driver.quit()