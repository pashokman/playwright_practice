from common_import import *
from page_objects.main_page import MainPage


main_page = MainPage()


def test_main_page_url(default_state):
    expect(default_state).to_have_url(main_page.URL)


def test_main_page_title(default_state):
    expect(default_state).to_have_title(main_page.TITLE)


def test_main_page_header(default_state):
    expect(main_page.get_header(default_state)).to_have_text(main_page.HEADER_H1_TEXT)
