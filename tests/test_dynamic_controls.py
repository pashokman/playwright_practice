from common_import import *

from page_objects.dynamic_controls_page import DynamicControlsPage


dynamic_c_page = DynamicControlsPage()


def test_dynamic_control_default_checkbox_state(dynamic_controls_page):
    checkbox = dynamic_c_page.get_checkbox(dynamic_controls_page)
    expect(checkbox).to_be_visible()


def test_dynamic_control_default_remove_button_state(dynamic_controls_page):
    remove_button = dynamic_c_page.get_remove_btn(dynamic_controls_page)
    expect(remove_button).to_be_visible()


def test_dynamic_control_default_add_button_state(dynamic_controls_page):
    add_button = dynamic_c_page.get_add_btn(dynamic_controls_page)
    expect(add_button).to_be_hidden()


def test_dynamic_control_default_its_gone_msg_state(dynamic_controls_page):
    its_gone_msg = dynamic_c_page.get_its_gone_msg(dynamic_controls_page)
    expect(its_gone_msg).to_be_hidden()


def test_dynamic_control_default_input_state(dynamic_controls_page):
    input = dynamic_c_page.get_input(dynamic_controls_page)
    expect(input).to_be_disabled()


def test_dynamic_control_default_enable_button_state(dynamic_controls_page):
    enable_button = dynamic_c_page.get_enable_btn(dynamic_controls_page)
    expect(enable_button).to_be_visible()
    

def test_dynamic_controls_remove_button_click(dynamic_controls_page):
    remove_button = dynamic_c_page.get_remove_btn(dynamic_controls_page)
    remove_button.click()
    expect(remove_button).to_be_hidden()

    checkbox = dynamic_c_page.get_checkbox(dynamic_controls_page)
    expect(checkbox).to_be_hidden()

    add_button = dynamic_c_page.get_add_btn(dynamic_controls_page)
    expect(add_button).to_be_visible()
    
    its_gone_msg = dynamic_c_page.get_its_gone_msg(dynamic_controls_page)
    expect(its_gone_msg).to_be_visible()


def test_dynamic_control_enable_button_click(dynamic_controls_page):
    enable_button = dynamic_c_page.get_enable_btn(dynamic_controls_page)
    enable_button.click()
    expect(enable_button).to_be_hidden()

    input = dynamic_c_page.get_input(dynamic_controls_page)
    expect(input).to_be_enabled()

    disable_button = dynamic_c_page.get_disable_btn(dynamic_controls_page)
    expect(disable_button).to_be_visible()

    its_enabled_msg = dynamic_c_page.get_its_enable_msg(dynamic_controls_page)
    expect(its_enabled_msg).to_be_visible()


@pytest.mark.xfail
def test_filling_disabled_input(dynamic_controls_page):
    dynamic_c_page.get_input(dynamic_controls_page).fill('some text')


def test_filling_enabled_input(dynamic_controls_page):
    enable_button = dynamic_c_page.get_enable_btn(dynamic_controls_page)
    enable_button.click()

    text = 'some text'
    input = dynamic_c_page.get_input(dynamic_controls_page)
    input.fill(text)
    expect(input).to_have_value(text)
