import os
from common_import import *


def test_file_download(file_download_page):
    with file_download_page.expect_download() as download_info:
        file_download_page.get_by_text("file_to_upload.txt").click()
    download = download_info.value

    work_dir_path = os.getcwd()
    final_path = os.path.join(work_dir_path, "files\\download\\file_to_upload.txt")
    download.save_as(final_path)

    if os.path.exists(final_path):
        os.remove(final_path)
        print(f"File removed successfully: {final_path}")
    else:
        print(f"File not found for removal: {final_path}")