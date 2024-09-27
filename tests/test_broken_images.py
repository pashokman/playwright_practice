from common_import import *
import requests
from utilities.read_configurations import read_configuration
from page_objects.broken_images_page import BrokenImagePage


bi_page = BrokenImagePage()


def test_broken_images_total_images_count(broken_img_page):
    images = bi_page.get_images_elem(broken_img_page)
    expect(images).to_have_count(4)


def test_broken_images_count(broken_img_page):
    images = bi_page.get_images_list(broken_img_page)
    broken_img_count = 0
    for i in range(len(images)):
        src = images[i].get_attribute("src")
        resp = requests.get(read_configuration("basic info", "url") + src)
        if resp.status_code >= 300:
            broken_img_count += 1

    assert broken_img_count == 2