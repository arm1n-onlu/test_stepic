import time
import math
import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(3)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('number', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
class TestPage():
    def test_stepick_adress(self, browser, number):
        link = f"https://stepik.org/lesson/{number}/step/1"
        browser.get(link)
        putanswer = browser.find_element_by_xpath('//textarea')
        answer = math.log(int(time.time()))
        answer1 = answer.__str__()
        putanswer.send_keys(answer1)
        button = browser.find_element_by_xpath('//button[@class="submit-submission"]')
        button.click()
        message = browser.find_element_by_css_selector('[class="smart-hints__hint"]')
        assert "Correct!" in message.text, "Error output"

