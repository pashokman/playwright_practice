from common_import import *


def test_main_page_url(page_default):
    expect(page_default).to_have_url("https://the-internet.herokuapp.com/")


def test_main_page_title(page_default):
    expect(page_default).to_have_title("The Internet")


def test_main_page_header(page_default):
    expect(page_default.locator("#content .heading")).to_have_text("Welcome to the-internet")
