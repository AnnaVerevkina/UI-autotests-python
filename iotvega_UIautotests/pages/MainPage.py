from selenium.webdriver.common.by import By

from iotvega_UIautotests.pages.BaseApp import BasePage


class MainPagesLocators:
    LOCATOR_TELEGRAM_ICON = (By.XPATH, "//i[contains(@class, 'fa fa-telegram')]")
    LOCATOR_PRODUCTS_NAVBAR = (By.XPATH, "//li//a[contains(text(), 'Продукция')]")
    LOCATOR_SMART_NAVBAR_ITEM = (By.XPATH, "//a[contains(text(), 'Серия Smart')]")
    LOCATOR_SMART_DEVICE_SS0102 = {By.XPATH, "//a[contains(text(), 'Вега Smart-SS0102')]"}
    LOCATOR_SS0102_HEADER = {By.XPATH, "//h1[contains(text(),'Вега Smart-SS0102 - датчик дыма')]"}


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def hover_products_navbar(self):
        print("hover to product navbar")
        return self.hover_element(MainPagesLocators.LOCATOR_PRODUCTS_NAVBAR)

    def click_smart_products_navbar(self):
        return self.click_button(MainPagesLocators.LOCATOR_SMART_NAVBAR_ITEM)

    def click_smart_device_ss0102(self):
        print("ss0102")
        return self.click_button(MainPagesLocators.LOCATOR_SMART_DEVICE_SS0102)

    def click_telegram(self):
        print("The third breakpoint")
        return self.click_button(MainPagesLocators.LOCATOR_TELEGRAM_ICON, time=2)
