from page_objects.main_page import MainPage

from utilities.read_configurations import read_configuration


class BasicAuthPage(MainPage):
    USERNAME = read_configuration("basic info", "username")
    PASSWORD = read_configuration("basic info", "password")
    
    BASIC_AUTH_URL = f"https://{USERNAME}:{PASSWORD}@{MainPage.URL[8:]}basic_auth"

    HEADER_H3_LOC = "//h3"
    HEADER_H3_TEXT = "Basic Auth"

    CONGRATULATIONS_LOC = ".example p"
    CONGRATULATIONS_TEXT = "Congratulations! You must have the proper credentials."

    def get_header(self, page):
        h = page.locator(self.HEADER_H3_LOC)
        return h

    def get_congratulations(self, page):
        c = page.locator(self.CONGRATULATIONS_LOC)
        return c
