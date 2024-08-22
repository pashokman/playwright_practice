import pytest

# Main page
@pytest.fixture
def page_default(default_state):
    for page in default_state:
        return page

# Add/Remove Elements page
@pytest.fixture
def add_rem_page(default_state):
    for page in default_state:
        page.get_by_text('Add/Remove Elements').click()
        return page

# Broken Images page
@pytest.fixture
def broken_img_page(default_state):
    for page in default_state:
        page.get_by_text('Broken Images').click()
        return page

# Checkboxes page
@pytest.fixture
def checkboxes_page(default_state):
    for page in default_state:
        page.get_by_text('Checkboxes').click()
        return page

# Context Menu page
@pytest.fixture
def context_menu_page(default_state):
    for page in default_state:
        page.get_by_text('Context Menu').click()
        return page

# Drag and Drop page
@pytest.fixture
def drag_and_drop_page(default_state):
    for page in default_state:
        page.get_by_text('Drag and Drop').click()
        return page

# Dropdown page
@pytest.fixture
def dropdown_page(default_state):
    for page in default_state:
        page.get_by_text('Dropdown').click()
        return page

# Dynamic Controls page
@pytest.fixture
def dynamic_controls_page(default_state):
    for page in default_state:
        page.get_by_text('Dynamic Controls').click()
        return page

# Entry Ad page
@pytest.fixture
def entry_ad_page(default_state):
    for page in default_state:
        page.get_by_text('Entry Ad').click()
        return page

# File Upload page
@pytest.fixture
def file_upload_page(default_state):
    for page in default_state:
        page.get_by_text('File Upload').click()
        return page

# File Download page
@pytest.fixture
def file_download_page(default_state):
    for page in default_state:
        page.get_by_text('File Download', exact=True).click()
        return page
