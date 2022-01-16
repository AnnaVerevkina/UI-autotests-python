from selenium.webdriver.common.by import By

from soundcloud_UIautotests.pages.BasePage import BasePage


class MainPagesLocators:

    LOCATOR_SOUND_INPUT = (By.XPATH, "//body/div[@id='app']/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]/span[1]/form[1]/input[1]")
    LOCATOR_SOUND_INPUT_BTN = (By.XPATH, "//*[@id=\"content\"]/div/div/div[2]/div/div[1]/span/span/form/button")
    LOCATOR_ACCEPT_COOKIES = (By.XPATH, "//*[@id=\"onetrust-accept-btn-handler\"]")
    LOCATOR_FIRST_TRACK = (By.XPATH, "html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/ul[1]/li[2]/div[1]/div[1]/div[1]/div[1]/a[1]/div[1]/span[1]")
    LOCATOR_PLAY_BTN = (By.XPATH, "//body/div[@id='app']/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/a[1]")
    LOCATOR_PHOTO = (By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/span[1]")
    LOCATOR_INPUT_TRACK_URL = (By.XPATH, "/html/body/div[2]/div/center/form/div/input")
    LOCATOR_INPUT_TRACK_BTN = (By.XPATH, "/html/body/div[2]/div/center/form/div/div/input")


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_cookies(self):
        print("click accept cookies")
        return self.click_button(MainPagesLocators.LOCATOR_ACCEPT_COOKIES)

    def input_sound(self, line):
        print("input_sound")
        return self.send_keys(MainPagesLocators.LOCATOR_SOUND_INPUT, line)

    def click_input_sound(self):
        print("click input_sound")
        return self.click_button(MainPagesLocators.LOCATOR_SOUND_INPUT_BTN)

    def hover_track(self):
        return self.hover_element(MainPagesLocators.LOCATOR_FIRST_TRACK)

    def click_track(self):
        return self.click_button(MainPagesLocators.LOCATOR_FIRST_TRACK)

    def click_play(self):
        return self.click_button(MainPagesLocators.LOCATOR_PLAY_BTN)

    def click_photo(self):
        return self.click_button(MainPagesLocators.LOCATOR_PHOTO)
