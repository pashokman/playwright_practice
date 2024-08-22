from common_import import *
import requests
from utilities.read_configurations import read_configuration


def test_broken_images_total_images_count(broken_img_page):
    images = broken_img_page.locator("//img")
    expect(images).to_have_count(4)


def test_broken_images_count(broken_img_page):
    images = broken_img_page.locator("//img").all()
    broken_img_count = 0
    for i in range(len(images)):
        src = images[i].get_attribute("src")
        resp = requests.get(read_configuration("basic info", "url") + src)
        if resp.status_code >= 300:
            broken_img_count += 1

    assert broken_img_count == 2