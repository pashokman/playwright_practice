import pytest


# Add/Remove Elements page
@pytest.fixture
def add_rem_page(default_state):
    default_state.get_by_text('Add/Remove Elements').click()
    return default_state

# Broken Images page
@pytest.fixture
def broken_img_page(default_state):
    default_state.get_by_text('Broken Images').click()
    return default_state

# Checkboxes page
@pytest.fixture
def checkboxes_page(default_state):
    default_state.get_by_text('Checkboxes').click()
    return default_state

# Context Menu page
@pytest.fixture
def context_menu_page(default_state):
    default_state.get_by_text('Context Menu').click()
    return default_state

# Drag and Drop page
@pytest.fixture
def drag_and_drop_page(default_state):
    default_state.get_by_text('Drag and Drop').click()
    return default_state

# Dropdown page
@pytest.fixture
def dropdown_page(default_state):
    default_state.get_by_text('Dropdown').click()
    return default_state

# Dynamic Controls page
@pytest.fixture
def dynamic_controls_page(default_state):
    default_state.get_by_text('Dynamic Controls').click()
    return default_state

# Entry Ad page
@pytest.fixture
def entry_ad_page(default_state):
    default_state.get_by_text('Entry Ad').click()
    return default_state

# File Upload page
@pytest.fixture
def file_upload_page(default_state):
    default_state.get_by_text('File Upload').click()
    return default_state

# File Download page
@pytest.fixture
def file_download_page(default_state):
    default_state.get_by_text('File Download', exact=True).click()
    return default_state
