import pytest
from playwright.sync_api import Page

from utilities.read_configurations import read_configuration


@pytest.fixture(autouse=True)
def default_state(page: Page):
    url = read_configuration("basic info", "url")  
    page.set_viewport_size({"width": 1920, "height": 1080})
    page.goto(url)
    yield page