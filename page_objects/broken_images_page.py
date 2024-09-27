from page_objects.main_page import MainPage


class BrokenImagePage(MainPage):

    IMG_LOC = "//img"

    def get_images_elem(self, page):
        imgs = page.locator(self.IMG_LOC)
        return imgs
    
    def get_images_list(self, page):
        imgs_list = page.locator(self.IMG_LOC).all()
        return imgs_list