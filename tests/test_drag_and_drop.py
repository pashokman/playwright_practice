from common_import import *

from page_objects.drag_and_drop_page import DragAndDropPage


dd_page = DragAndDropPage()


def test_drag_and_drop_default_state(drag_and_drop_page):
    first_element = dd_page.get_first_element(drag_and_drop_page)
    second_element = dd_page.get_second_element(drag_and_drop_page)
    
    expect(first_element).to_contain_text("A")
    expect(second_element).to_contain_text("B")


def test_drag_and_drop(drag_and_drop_page):
    first_element = dd_page.get_first_element(drag_and_drop_page)
    second_element = dd_page.get_second_element(drag_and_drop_page)

    dd_page.drag_first_and_drop_into_a_second(first_element, second_element)
    expect(first_element).to_contain_text("B")