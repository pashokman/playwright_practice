from common_import import *

from page_objects.basic_auth_page import BasicAuthPage


ba_page = BasicAuthPage()


def test_basic_auth(default_state):
    default_state.goto(ba_page.BASIC_AUTH_URL)
    header = ba_page.get_header(default_state)
    congratulations = ba_page.get_congratulations(default_state)
    
    expect(header).to_have_text(ba_page.HEADER_H3_TEXT)
    expect(congratulations).to_contain_text(ba_page.CONGRATULATIONS_TEXT)
