class DragAndDropPage():
    
    ITEM_A_LOC = "#column-a"
    ITEM_B_LOC = "#column-b"

    def get_first_element(self, page):
        first_item = page.locator(self.ITEM_A_LOC)
        return first_item

    def get_second_element(self, page):
        second_item = page.locator(self.ITEM_B_LOC)
        return second_item
    
    def drag_first_and_drop_into_a_second(self, element1, element2):
        element1.drag_to(element2)