from common_import import *


def test_drag_and_drop(drag_and_drop_page):
    first_element = drag_and_drop_page.locator(".column header").first
    expect(first_element).to_contain_text("A")
    drag_and_drop_page.locator("#column-a").drag_to(drag_and_drop_page.locator('#column-b'))
    expect(first_element).to_contain_text("B")