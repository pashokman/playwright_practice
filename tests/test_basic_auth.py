from common_import import *
from utilities.read_configurations import read_configuration

def test_basic_auth(default_state):
    username = read_configuration("basic info", "username")
    password = read_configuration("basic info", "password")
    
    basic_auth_url = f"https://{username}:{password}@{default_state.url[8:]}basic_auth"
    default_state.goto(basic_auth_url)
    header = default_state.locator("//h3")
    congratulations = default_state.locator(".example p")
    expect(header).to_have_text("Basic Auth")
    expect(congratulations).to_contain_text("Congratulations! You must have the proper credentials.")
