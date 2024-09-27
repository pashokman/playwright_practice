from common_import import *

from page_objects.checkboxes_page import CheckboxesPage


cb_page = CheckboxesPage()


def test_checkboxes_change_statuses(checkboxes_page):
    checkboxes = cb_page.get_checkboxes_list(checkboxes_page)
    statuses = []

    for checkbox in checkboxes:
        checked_attr = checkbox.is_checked()
        statuses.append(1 if checked_attr else 0)
    assert statuses == cb_page.DEFAULT_STATUSES, "Default checkbox statuses do not match expectations"

    for checkbox in checkboxes:
        checkbox.click()

    statuses = []
    for checkbox in checkboxes:
        checked_attr = checkbox.is_checked()
        statuses.append(1 if checked_attr else 0)
    assert statuses == cb_page.CHANGED_STATUSEES, "Changed statuses do not match expectations"    


def test_checkboxes_count(checkboxes_page):
    checkboxes = cb_page.get_checkboxes_list(checkboxes_page)
    assert len(checkboxes) == 2


def test_checkboxes_default_statuses(checkboxes_page):
    checkboxes = cb_page.get_checkboxes_list(checkboxes_page)
    expect(checkboxes[0]).not_to_be_checked()
    expect(checkboxes[1]).to_be_checked()
