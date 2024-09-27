class EntryAdPage():

    AD_LOC = "//div[@class='modal']"
    CLOSE_AD_LOC = "//div[@class='modal-footer']/p"

    def get_ad_window(self, page):
        return page.locator(self.AD_LOC)

    def get_ad_close_btn(self, page):
        return page.locator(self.CLOSE_AD_LOC)
