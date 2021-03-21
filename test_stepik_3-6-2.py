import pytest
from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


links = ['https://stepik.org/lesson/236895/step/1',
        'https://stepik.org/lesson/236896/step/1',
        'https://stepik.org/lesson/236897/step/1',
        'https://stepik.org/lesson/236898/step/1',
        'https://stepik.org/lesson/236899/step/1',
        'https://stepik.org/lesson/236903/step/1',
        'https://stepik.org/lesson/236904/step/1',
        'https://stepik.org/lesson/236905/step/1']

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize("link", links)
def test_localtime(browser, link):
    browser.get(link)
    textarea = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//textarea[contains(@id, 'ember')]")))

    answer = math.log(int(time.time()))

    textarea.send_keys(str(answer))

    btn_submit = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.submit-submission')))
    btn_submit.click()

    answer_result = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.smart-hints__hint')))

    assert answer_result.text == 'Correct!', 'Не корректно!'

