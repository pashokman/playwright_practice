from common_import import *


@pytest.mark.parametrize(["add", "remove", "count"], [(0, 0, 0), (1, 1, 0), (3, 2, 1), (5, 2, 3), (7, 3, 4)])
def test_add_remove_lements_with_params(add_rem_page, add, remove, count):
    add_button = add_rem_page.get_by_role("button", name="Add Element")
    for i in range(add):
        add_button.click()
    delete_buttons = add_rem_page.get_by_role("button", name="Delete")
    for i in range(remove):
        delete_buttons.nth(-1).click()
    expect(delete_buttons).to_have_count(count)


def test_add_remove_elements_page_header(add_rem_page):
    expect(add_rem_page.locator("//h3")).to_have_text("Add/Remove Elements")


def test_add_remove_elements_default_add_button_count(add_rem_page):
    buttons = add_rem_page.get_by_role("button", name="Add Element")
    expect(buttons).to_have_count(1)


def test_add_remove_elements_default_remove_button_count(add_rem_page):
    buttons = add_rem_page.get_by_role("button", name="Delete")
    expect(buttons).to_have_count(0)


def test_add_remove_elements_3_remove_buttons_added(add_rem_page):
    add_button = add_rem_page.get_by_role("button", name="Add Element")
    for i in range(3):
        add_button.click()
    delete_buttons = add_rem_page.get_by_role("button", name="Delete")
    expect(delete_buttons).to_have_count(3)
