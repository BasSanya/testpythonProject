from selenium import webdriver
import time
import unittest

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input_name = browser.find_element_by_css_selector('.first_block>div:nth-child(1)>.first')
        input_name.send_keys('Sasha')

        input_lname = browser.find_element_by_css_selector('.first_block>div:nth-child(2)>.second')
        input_lname.send_keys('Joriko')

        input_email = browser.find_element_by_css_selector('.first_block>div:nth-child(3)>.third')
        input_email.send_keys('ad@ad.me')

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input_name = browser.find_element_by_css_selector('.first_block>div:nth-child(1)>.first')
        input_name.send_keys('Sasha')

        input_lname = browser.find_element_by_css_selector('.first_block>div:nth-child(2)>.second')
        input_lname.send_keys('Joriko')

        input_email = browser.find_element_by_css_selector('.first_block>div:nth-child(3)>.third')
        input_email.send_keys('ad@ad.me')

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

if __name__ == "__main__":
    unittest.main()