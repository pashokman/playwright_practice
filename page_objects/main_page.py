class MainPage():
    
    URL = "https://the-internet.herokuapp.com/"
    HEADER_H1_LOC = "#content .heading"

    TITLE = "The Internet"
    HEADER_H1_TEXT = "Welcome to the-internet"

    def get_header(self, page):
        header = page.locator(self.HEADER_H1_LOC)
        return header
