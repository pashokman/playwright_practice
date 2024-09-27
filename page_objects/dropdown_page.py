class DropDownPage():

    DROPDOWN_LOC = "#dropdown"
    DROPDOWN_ELEM_LOC = "//option"
    DROPDOWN_SELECTED_VALUE_LOC = "select[id='dropdown'] > option[selected='selected']"


    def get_dropdown(self, page):
        return page.locator(self.DROPDOWN_LOC)

    def open_dropdown(self, page):
        self.get_dropdown(page).click()

    def get_dropdown_elements_list(self, page):
        elements = page.locator(self.DROPDOWN_ELEM_LOC)
        return elements
    
    def get_dropdown_selected_value(self, page):
        return page.locator(self.DROPDOWN_SELECTED_VALUE_LOC)