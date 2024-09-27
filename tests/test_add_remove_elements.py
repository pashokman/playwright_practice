from common_import import *

from page_objects.add_remove_elements_page import AddRemoveElementsPage


ar_page = AddRemoveElementsPage()


@pytest.mark.parametrize(["add", "remove", "count"], [(0, 0, 0), (1, 1, 0), (3, 2, 1), (5, 2, 3), (7, 3, 4)])
def test_add_remove_elements_with_params(add_rem_page, add, remove, count):
    add_button = ar_page.get_add_button(add_rem_page)
    delete_buttons = ar_page.get_delete_buttons(add_rem_page)

    for i in range(add):
        add_button.click()
    for i in range(remove):
        delete_buttons.nth(-1).click()
    expect(delete_buttons).to_have_count(count)


def test_add_remove_elements_page_header(add_rem_page):
    expect(ar_page.get_h3_elem(add_rem_page)).to_have_text(ar_page.HEADER_H3_TEXT)


def test_add_remove_elements_default_add_button_count(add_rem_page):
    buttons = ar_page.get_add_button(add_rem_page)
    expect(buttons).to_have_count(1)


def test_add_remove_elements_default_remove_button_count(add_rem_page):
    buttons = ar_page.get_delete_buttons(add_rem_page)
    expect(buttons).to_have_count(0)


def test_add_remove_elements_3_remove_buttons_added(add_rem_page):
    add_button = ar_page.get_add_button(add_rem_page)
    delete_buttons = ar_page.get_delete_buttons(add_rem_page)

    for i in range(3):
        add_button.click()
    expect(delete_buttons).to_have_count(3)
