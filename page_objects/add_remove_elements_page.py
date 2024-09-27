
class AddRemoveElementsPage():
    
    ADD_ELEMENT_BTN_NAME = "Add Element"
    DELETE_ELEMENT_BTN_NAME = "Delete"
    
    HEADER_H3_LOC = "//h3"
    HEADER_H3_TEXT = "Add/Remove Elements"

    def get_add_button(self, page):
        add_button = page.get_by_role("button", name=self.ADD_ELEMENT_BTN_NAME)
        return add_button

    def get_delete_buttons(self, page):
        delete_buttons = page.get_by_role("button", name=self.DELETE_ELEMENT_BTN_NAME)
        return delete_buttons
    
    def get_h3_elem(self, page):
        t = page.locator(self.HEADER_H3_LOC)
        return t