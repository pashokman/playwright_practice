import os


class FileUploadPage():

    FILE_PATH = os.path.abspath("files\\upload\\file_to_upload.txt")

    UPLOAD_FIELD_LOC = "#file-upload"
    SUBMIT_BTN_LOC = "#file-submit"

    RESULT_HEADER_LOC = "//h3"
    UPLOADED_FILES_LIST_LOC = "#uploaded-files"

    def check_if_local_file_exist(self):
        if not os.path.exists(self.FILE_PATH):
            raise FileNotFoundError(f"File not found: {self.FILE_PATH}")
        
    def get_upload_field(self, page):
        return page.locator(self.UPLOAD_FIELD_LOC)
    
    def select_file_to_upload(self, page):
        self.get_upload_field(page).set_input_files([self.FILE_PATH])

    def upload_file(self, page):
        page.locator(self.SUBMIT_BTN_LOC).click()

    def get_result_header(self, page):
        return page.locator(self.RESULT_HEADER_LOC)
    
    def get_uploaded_files_list(self, page):
        return page.locator(self.UPLOADED_FILES_LIST_LOC)

