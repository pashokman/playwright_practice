from common_import import *

from page_objects.entry_ad_page import EntryAdPage


e_ad_page = EntryAdPage()

def test_entry_ad_page_close_ad(entry_ad_page):
    ad_window = e_ad_page.get_ad_window(entry_ad_page)
    expect(ad_window).to_be_visible()

    e_ad_page.get_ad_close_btn(entry_ad_page).click()
    expect(ad_window).to_be_hidden()
