from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

    driver = webdriver.Chrome()
    driver.get('http://suninjuly.github.io/alert_accept.html')

    #elements
    a_btn = driver.find_element_by_tag_name('button')
    a_btn.click()

    alert = driver.switch_to.alert
    alert.accept()

    num = driver.find_element_by_id('input_value').text
    answer = driver.find_element_by_id('answer')
    num = calc(num)
    answer.send_keys(str(num))

    btn = driver.find_element_by_css_selector('[type="submit"]')

    btn.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    driver.quit()