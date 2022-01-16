from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://soundcloud.com/"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_all_elements_located(locator),
                                                      message=f"Can't find element by locator {locator}")[0]

    def click_button(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_all_elements_located(locator))[0].click()

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def hover_element(self, locator):
        hov = ActionChains(self.driver).move_to_element(self.find_element(locator))
        hov.perform()

    def send_keys(self, locator, line):
        print("send_keys")
        return self.find_element(locator).send_keys(line)
