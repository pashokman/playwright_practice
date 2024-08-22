from common_import import *


def test_entry_ad_page_close_ad(entry_ad_page):
    ad_window = entry_ad_page.locator("//div[@class='modal']")
    expect(ad_window).to_be_visible()

    close_btn = entry_ad_page.locator("//div[@class='modal-footer']/p")
    close_btn.click()
    
    expect(ad_window).to_be_hidden()
