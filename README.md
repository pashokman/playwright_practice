# playwright_practice
Documentation - https://playwright.dev/python/docs/test-assertions

# Tests set up
1. To create a test in console should run:
```
playwright codegen
```
2. Make needed actions/assertions.
3. Change `Targed` in a code window to Pytest.
4. Copy test code.
5. Paste the code in a test file.
6. Repeat previous steps needed amount of times.
7. Refactor the code - create a fixtures where neeeded, implement Page object model.
8. Run the tests.

# Recording a trace
To record traces by running tests, it will automaticaly creates a `test-results` folder with `trace.zip` file
```
pytest --tracing on -k test_not_working_name
```
To open trace file
```
playwright show-trace ./test-results/tests-test-example-py-test-not-working-chromium/trace.zip
```


# Debugging
This command will start the playwright debugger with browser window and code window
```
PWDEBUG=1 pytest -s
```
To set the breakpoint should add this code where test shoud stops
```
page.pause()
```
To debug one test file
```
PWDEBUG=1 pytest -s test_example.py
```

# Run tests
## Before running the tests:
1. Create venv - `python -m venv venv`.
2. Activate venv - `venv/bin/Activate.ps1`.
3. Install required modules - `pip install -r requirements.txt`.
4. Upgrade pip - `python.exe -m pip install --upgrade pip`.
5. Install playwright - `playwright install`
5. Run the test.  

Headless mode - (default) run all tests in  (without operning the browser)
```
pytest
```
Headed mode - run all tests with opening the browser
```
pytest --headed
```
Run in multiple browsers
```
pytest --browser webkit --browser firefox
```
Run specific tests
```
pytest test_login.py test_todo_page.py
```
Run tests with some key words (run all tests with word login in name)
```
pytest -k login
```
Run tests in parallel (should be installed pytest-xdist)
```
pytest --numprocesses 2
```


# Playwrite commands
## Basic configuration commands
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # create a browser instance
    browserC = p.chromium.launch()
    # create a context instance
    contextC = browserC.new_context()
    # create a page instance
    pageC = contextC.new_page()
    # open page with specific url
    pageC.goto(url)


## Work with elements
### Different type of fields
#### Text input
page.get_by_role("textbox").fill("Peter")
#### Date input
page.get_by_label("Birth date").fill("2020-02-02")
#### Check the checkbox/radio button
page.get_by_label('I agree to the terms above').check()
#### Single selection matching the label
page.get_by_label('Choose a color').select_option(label='Blue')
#### Multiple selected items
page.get_by_label('Choose multiple colors').select_option(['red', 'green', 'blue'])

### Mouse
#### Generic click
page.get_by_role("button").click()
#### Double click
page.get_by_text("Item").dblclick()
#### Right click
page.get_by_text("Item").click(button="right")
#### Shift + click
page.get_by_text("Item").click(modifiers=["Shift"])
#### Hover over element
page.get_by_text("Item").hover()
#### Click the top left corner
page.get_by_text("Item").click(position={ "x": 0, "y": 0})

### Keys and shortcuts
#### Dispatch Control+Right
page.get_by_role("textbox").press("Control+ArrowRight")
List of keys - Backquote, Minus, Equal, Backslash, Backspace, Tab, Delete, Escape, ArrowDown, End, Enter, Home, Insert, PageDown, PageUp, ArrowRight, ArrowUp, F1 - F12, Digit0 - Digit9,  eyA - KeyZ, etc.

### Upload files
page.get_by_label("Upload files").set_input_files(['file1.txt', 'file2.txt'])

### Drag and Drop
page.locator("#item-to-be-dragged").drag_to(page.locator("#item-to-drop-at"))