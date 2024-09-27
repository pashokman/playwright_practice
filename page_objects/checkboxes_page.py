from page_objects.main_page import MainPage


class CheckboxesPage(MainPage):

    CHECKBOXES_LOC = "#checkboxes >> input"

    DEFAULT_STATUSES = [0, 1]
    CHANGED_STATUSEES = [1 if i == 0 else 0 for i in DEFAULT_STATUSES]

    def get_checkboxes_list(self, page):
        checkboxes_list = page.locator(self.CHECKBOXES_LOC).all()
        return checkboxes_list