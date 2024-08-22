from common_import import *

default_statuses = [0, 1]
changed_statuses = [1 if i == 0 else 0 for i in default_statuses]


def test_checkboxes_change_statuses(checkboxes_page):
    checkboxes = checkboxes_page.locator("//form/input").all()
    statuses = []

    for checkbox in checkboxes:
        checked_attr = checkbox.is_checked()
        statuses.append(1 if checked_attr else 0)
    assert statuses == default_statuses, "Default checkbox statuses do not match expectations"

    for checkbox in checkboxes:
        checkbox.click()

    statuses = []
    for checkbox in checkboxes:
        checked_attr = checkbox.is_checked()
        statuses.append(1 if checked_attr else 0)
    assert statuses == changed_statuses, "Changed statuses do not match expectations"    


def test_checkboxes_count(checkboxes_page):
    checkboxes = checkboxes_page.locator("#checkboxes >> input").all()
    assert len(checkboxes) == 2


def test_checkboxes_default_statuses(checkboxes_page):
    checkboxes = checkboxes_page.locator("#checkboxes >> input").all()
    expect(checkboxes[0]).not_to_be_checked()
    expect(checkboxes[1]).to_be_checked()
