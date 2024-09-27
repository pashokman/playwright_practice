from common_import import *

from page_objects.context_menu_page import ContextMenuPage

cm_page = ContextMenuPage()


def test_context_menu_right_click(context_menu_page):
    cm_page.open_context_menu(context_menu_page)
    cm_page.close_popup(context_menu_page)