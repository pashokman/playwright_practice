import pytest
# from playwright.sync_api import Page
from playwright.sync_api import sync_playwright

from utilities.read_configurations import read_configuration

# only chromium browser runs by default
# @pytest.fixture(autouse=True)
# def default_state(page: Page):
#     url = read_configuration("basic info", "url")    
#     page.goto(url)
#     yield page

# three browsers runs
@pytest.fixture(autouse=True)
def default_state():
    with sync_playwright() as p:
        options = {
            "headless": False,
            "slow_mo": 1000
        }

        url = read_configuration("basic info", "url")

        browserC = p.chromium.launch(**options)
        contextC = browserC.new_context()
        pageC = contextC.new_page()
        pageC.goto(url)

        browserF = p.firefox.launch(**options)
        contextF = browserF.new_context()
        pageF = contextF.new_page()
        pageF.goto(url)

        browserW = p.webkit.launch(**options)
        contextW = browserW.new_context()
        pageW = contextW.new_page()
        pageW.goto(url)
        
        yield pageC, pageF, pageW
