
class ContextMenuPage():
    MENU_LOC = '#hot-spot'

    @staticmethod
    def handle_dialog(dialog):
        dialog.accept()

    def open_context_menu(self, page):
        return page.locator(self.MENU_LOC).click(button='right')
    
    def close_popup(self, page):
        return page.on("dialog", ContextMenuPage.handle_dialog)