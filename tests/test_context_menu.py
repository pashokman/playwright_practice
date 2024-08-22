from common_import import *


def handle_dialog(dialog):
    dialog.accept()


def test_context_menu_right_click(context_menu_page):
    context_menu_page.locator('#hot-spot').click(button="right")
    context_menu_page.on("dialog", handle_dialog)