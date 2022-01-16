from selenium.webdriver.common.by import By

from iotvega_UIautotests.pages.BaseApp import BasePage


class ProductPageLocators:
    LOCATOR_PRODUCT_NAME_LIST = (By.XPATH, "//div[contains(@class, 'product-name')]/h2")


class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = "https://iotvega.com/product"

    def find_list_of_products(self):
        return self.find_list_of_elements(ProductPageLocators.LOCATOR_PRODUCT_NAME_LIST)
