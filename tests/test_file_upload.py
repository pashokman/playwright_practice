import os
from common_import import *


def test_file_upload(file_upload_page):
    file_path = os.path.abspath("files\\upload\\file_to_upload.txt")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    file_upload_page.locator("#file-upload").set_input_files([file_path])
    file_upload_page.locator("#file-submit").click()

    header = file_upload_page.locator("//h3")
    uploaded_files = file_upload_page.locator("#uploaded-files")

    expect(header).to_have_text("File Uploaded!")
    expect(uploaded_files).to_have_text("file_to_upload.txt")
