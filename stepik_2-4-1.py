from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

    driver = webdriver.Chrome()
    driver.get('http://suninjuly.github.io/explicit_wait2.html')
    price = WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
    btn_book = driver.find_element_by_id('book')
    btn_book.click()

    x = driver.find_element_by_id('input_value').text
    x = calc(x)

    answer = driver.find_element_by_id('answer')
    answer.send_keys(str(x))

    btn = driver.find_element_by_css_selector('[type="submit"]')
    btn.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    driver.quit()