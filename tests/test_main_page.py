from common_import import *


def test_main_page_url(default_state):
    expect(default_state).to_have_url("https://the-internet.herokuapp.com/")


def test_main_page_title(default_state):
    expect(default_state).to_have_title("The Internet")


def test_main_page_header(default_state):
    expect(default_state.locator("#content .heading")).to_have_text("Welcome to the-internet")
