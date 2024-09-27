# import os
from common_import import *

from page_objects.file_upload_page import FileUploadPage


fu_page = FileUploadPage()


def test_file_upload(file_upload_page):
    fu_page.check_if_local_file_exist()
    fu_page.select_file_to_upload(file_upload_page)
    fu_page.upload_file(file_upload_page)
    
    header = fu_page.get_result_header(file_upload_page)
    uploaded_files = fu_page.get_uploaded_files_list(file_upload_page)

    expect(header).to_have_text("File Uploaded!")
    expect(uploaded_files).to_have_text("file_to_upload.txt")
