class DynamicControlsPage():

    CHECKBOX_LOC = "//div//input[@type='checkbox']"
    REMOVE_BTN_LOC = "//button[text()='Remove']"
    ADD_BTN_LOC = "//button[text()='Add']"
    ITS_GONE_MSG_LOC = "//form[@id='checkbox-example']//p[@id='message']"
    INPUT_LOC = "//input[@type='text']"
    ENABLE_BTN_LOC = "//button[text()='Enable']"
    DISABLE_BTN_LOC = "//button[text()='Disable']"
    ITS_ENABLE_MSG_LOC = "//form[@id='input-example']//p[@id='message']"

    def get_checkbox(self, page):
        return page.locator(self.CHECKBOX_LOC)

    def get_remove_btn(self, page):
        return page.locator(self.REMOVE_BTN_LOC)

    def get_add_btn(self, page):
        return page.locator(self.ADD_BTN_LOC)

    def get_its_gone_msg(self, page):
        return page.locator(self.ITS_GONE_MSG_LOC)

    def get_input(self, page):
        return page.locator(self.INPUT_LOC)

    def get_enable_btn(self, page):
        return page.locator(self.ENABLE_BTN_LOC)

    def get_disable_btn(self, page):
        return page.locator(self.DISABLE_BTN_LOC)

    def get_its_enable_msg(self, page):
        return page.locator(self.ITS_ENABLE_MSG_LOC)