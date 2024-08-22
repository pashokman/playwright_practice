from common_import import *


def test_dynamic_control_default_checkbox_state(dynamic_controls_page):
    checkbox = dynamic_controls_page.locator("//div//input[@type='checkbox']")
    expect(checkbox).to_be_visible()


def test_dynamic_control_default_remove_button_state(dynamic_controls_page):
    remove_button = dynamic_controls_page.locator("//button[text()='Remove']")
    expect(remove_button).to_be_visible()


def test_dynamic_control_default_add_button_state(dynamic_controls_page):
    add_button = dynamic_controls_page.locator("//button[text()='Add']")
    expect(add_button).to_be_hidden()


def test_dynamic_control_default_its_gone_msg_state(dynamic_controls_page):
    its_gone_msg = dynamic_controls_page.locator("//form[@id='checkbox-example']//p[@id='message']")
    expect(its_gone_msg).to_be_hidden()


def test_dynamic_control_default_input_state(dynamic_controls_page):
    input = dynamic_controls_page.locator("//input[@type='text']")
    expect(input).to_be_disabled()


def test_dynamic_control_default_enable_button_state(dynamic_controls_page):
    enable_button = dynamic_controls_page.locator("//button[text()='Enable']")
    expect(enable_button).to_be_visible()
    

def test_dynamic_controls_remove_button_click(dynamic_controls_page):
    remove_button = dynamic_controls_page.locator("//button[text()='Remove']")
    remove_button.click()
    expect(remove_button).to_be_hidden()

    checkbox = dynamic_controls_page.locator("//div//input[@type='checkbox']")
    expect(checkbox).to_be_hidden()

    add_button = dynamic_controls_page.locator("//button[text()='Add']")
    expect(add_button).to_be_visible()
    
    its_gone_msg = dynamic_controls_page.locator("//form[@id='checkbox-example']//p[@id='message']")
    expect(its_gone_msg).to_be_visible()


def test_dynamic_control_enable_button_click(dynamic_controls_page):
    enable_button = dynamic_controls_page.locator("//button[text()='Enable']")
    enable_button.click()
    expect(enable_button).to_be_hidden()

    input = dynamic_controls_page.locator("//input[@type='text']")
    expect(input).to_be_enabled()

    disable_button = dynamic_controls_page.locator("//button[text()='Disable']")
    expect(disable_button).to_be_visible()

    its_enabled_msg = dynamic_controls_page.locator("//form[@id='input-example']//p[@id='message']")
    expect(its_enabled_msg).to_be_visible()


@pytest.mark.xfail
def test_filling_disabled_input(dynamic_controls_page):
    dynamic_controls_page.locator("//input[@type='text']").fill('some text')


def test_filling_enabled_input(dynamic_controls_page):
    enable_button = dynamic_controls_page.locator("//button[text()='Enable']")
    enable_button.click()

    text = 'some text'
    input = dynamic_controls_page.locator("//input[@type='text']")
    input.fill(text)
    expect(input).to_have_value(text)
