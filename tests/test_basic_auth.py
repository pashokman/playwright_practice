from common_import import *
from utilities.read_configurations import read_configuration

def test_basic_auth(page_default):
    username = read_configuration("basic info", "username")
    password = read_configuration("basic info", "password")
    
    basic_auth_url = f"https://{username}:{password}@{page_default.url[8:]}basic_auth"
    page_default.goto(basic_auth_url)
    header = page_default.locator("//h3")
    congratulations = page_default.locator(".example p")
    expect(header).to_have_text("Basic Auth")
    expect(congratulations).to_contain_text("Congratulations! You must have the proper credentials.")
