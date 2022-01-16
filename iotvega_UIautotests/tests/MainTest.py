import time

from iotvega_UIautotests.pages.MainPage import MainPage
from iotvega_UIautotests.pages.ProductPage import ProductPage
from iotvega_UIautotests.pages.ss0102Page import ss0102Page, ss0102PageLocators


def test_iotvega_chek_ss0102(browser):
    main_page = MainPage(browser)
    ss0102_page = ss0102Page(browser)
    main_page.go_to_site()
    main_page.hover_products_navbar()
    main_page.click_smart_products_navbar()
    main_page.click_smart_device_ss0102()
    time.sleep(5)

    assert (ss0102_page.find_element(ss0102PageLocators.LOCATOR_PRODUCT_HEADER))


def test_iotvega_chek_url_ss0102(browser):
    main_page = MainPage(browser)
    ss0102_page = ss0102Page(browser)
    main_page.go_to_site()
    main_page.hover_products_navbar()
    main_page.click_smart_products_navbar()
    main_page.click_smart_device_ss0102()
    time.sleep(5)

    assert (browser.current_url, ss0102_page.base_url)


# def test_products(browser):
#     product_page = ProductPage(browser)
#     product_page.go_to_site()
#     # list = browser.find_elements_by_xpath("//div[contains(@class, 'product-name')]/h2")
#     # for i in list:
#     #     text = i.text
#     #     print(text)
#     list = product_page.find_list_of_products()
#     # for i in list:
#     #     text = i.text
#     #     print(text)
