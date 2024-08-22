from common_import import *


def test_dropdown_default(dropdown_page):
    dropdown_page.locator("#dropdown").click()
    first_element = dropdown_page.locator("//option").first
    expect(first_element).to_be_disabled()
    second_element = dropdown_page.locator("//option").nth(1)
    expect(second_element).to_be_enabled()


def test_dropdown_select_option1(dropdown_page):
    dropdown = dropdown_page.locator("#dropdown")
    dropdown.select_option(index=1)
    # dropdown.select_option(value="1")
    # dropdown.select_option(label="Option 1")
    selected_value = dropdown_page.locator("select[id='dropdown'] > option[selected='selected']")
    expect(selected_value).to_have_text('Option 1')