from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

    driver = webdriver.Chrome()
    driver.get('http://suninjuly.github.io/get_attribute.html')

    x = driver.find_element_by_id('treasure')
    x = x.get_attribute('valuex')
    print(x)
    y = calc(x)

    field = driver.find_element_by_id('answer')
    field.send_keys(str(y))

    checkbox = driver.find_element_by_id('robotCheckbox')
    checkbox.click()

    radio_robot = driver.find_element_by_id('robotsRule')
    radio_robot.click()

    btn = driver.find_element_by_css_selector('[type="submit"]')

    btn.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    driver.quit()