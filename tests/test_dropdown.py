from common_import import *

from page_objects.dropdown_page import DropDownPage


dropd_page = DropDownPage()


def test_dropdown_default(dropdown_page):
    dropd_page.open_dropdown(dropdown_page)
    first_element = dropd_page.get_dropdown_elements_list(dropdown_page).first
    second_element = dropd_page.get_dropdown_elements_list(dropdown_page).nth(1)
    
    expect(first_element).to_be_disabled()
    expect(second_element).to_be_enabled()


def test_dropdown_select_option1(dropdown_page):
    dropdown = dropd_page.get_dropdown(dropdown_page)
    dropdown.select_option(index=1)
    # dropdown.select_option(value="1")
    # dropdown.select_option(label="Option 1")
    selected_value = dropd_page.get_dropdown_selected_value(dropdown_page)
    
    expect(selected_value).to_have_text('Option 1')