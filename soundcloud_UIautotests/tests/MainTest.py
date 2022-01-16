import time

from soundcloud_UIautotests.pages.MainPage import MainPage
target_page = "https://soundcloud.com/bootleg-coleccion/radiohead-creep-live"


def test_soundcloud_creep(browser):
    main_page = MainPage(browser)
    main_page.go_to_site()
    time.sleep(1)
    main_page.click_cookies()
    time.sleep(1)
    main_page.input_sound("radiohead")
    time.sleep(3)
    main_page.click_input_sound()
    time.sleep(3)
    main_page.hover_track()
    time.sleep(3)
    main_page.click_track()
    time.sleep(3)
    main_page.click_play()
    time.sleep(3)
    main_page.click_photo()
    time.sleep(6)
    assert (browser.current_url, target_page)