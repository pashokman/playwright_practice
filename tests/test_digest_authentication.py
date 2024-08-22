import os

import requests

from common_import import *

from requests.auth import HTTPDigestAuth


def test_digest_authentication(page_default):
    url = page_default.url
    url = url + "digest_auth"
    response = requests.get(url, auth=HTTPDigestAuth('admin', 'admin'))
    # Save the response content to a temporary file
    with open("temp.html", "w") as f:
        f.write(response.text)
    
    page_default.goto("file:///" + os.path.abspath("temp.html"))
    msg_element = page_default.locator("text=Congratulations! You must have the proper credentials.")
    assert msg_element.is_visible(), "Expected message not found"
    os.remove("temp.html")