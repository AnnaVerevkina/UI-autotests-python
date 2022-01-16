# from telnetlib import EC
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://iotvega.com/"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_all_elements_located(locator),
                                                      message=f"Can't find element by locator {locator}")[0]

    def find_list_of_elements(self, locator, time=10):
        list = self.driver.find_elements_by_xpath("//div[contains(@class, 'product-name')]/h2")
        sleep(15)
        for i in list:
            text = i.text
            print(text)

        return list

    def click_button(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_all_elements_located(locator))[0].click()

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def hover_element(self, locator):
        hov = ActionChains(self.driver).move_to_element(self.find_element(locator))
        hov.perform()
