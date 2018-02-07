from behave import *
from ...utils import config
from ...pages import home
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(15)

page = home.HomePage(driver)

@given('I have navigated to home page')
def step_impl(context):
    url = config.get_property('general','home_url')
    driver.get(url)
    assert driver.current_url == url

@then('I should see the top navigation links')
def step_impl(context):
    assert page.home.text    == config.get_property('TopNavigation','home')
    assert page.journey.text == config.get_property('TopNavigation','journey')
    assert page.export.text  == config.get_property('TopNavigation','export')
    assert page.guide.text   == config.get_property('TopNavigation','guide')
    assert page.service.text == config.get_property('TopNavigation','service')
    driver.quit()