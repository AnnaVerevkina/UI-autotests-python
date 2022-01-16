from selenium.webdriver.common.by import By

from iotvega_UIautotests.pages.BaseApp import BasePage


class ss0102PageLocators:
    LOCATOR_PRODUCT_HEADER = (By.XPATH, "/html[1]/body[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/h1[1]")


class ss0102Page(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = "https://iotvega.com/product/ss0102"
