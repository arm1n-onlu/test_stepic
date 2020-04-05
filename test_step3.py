from selenium import webdriver
import time
import unittest

class Test325(unittest.TestCase):
    def test_1(self):
        link = " http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        first = browser.find_element_by_xpath('//input[@placeholder="Input your first name"]')
        first.send_keys('HIHIHIHIHI')
        next = browser.find_element_by_xpath('//input[@placeholder="Input your last name"]')
        next.send_keys('HIHIHIHIHI')
        phone = browser.find_element_by_xpath('//input[@placeholder="Input your email"]')
        phone.send_keys('wwww@tut.re')
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
        browser.close()
    def test_2(self):
        link = " http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        first = browser.find_element_by_xpath('//input[@placeholder="Input your first name"]')
        first.send_keys('HIHIHIHIHI')
        next = browser.find_element_by_xpath('//input[@placeholder="Input your last name"]')
        next.send_keys('HIHIHIHIHI')
        phone = browser.find_element_by_xpath('//input[@placeholder="Input your email"]')
        phone.send_keys('wwww@tut.re')
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
        browser.close()
if __name__ == "__main__": unittest.main()