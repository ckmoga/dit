from behave import *
from ...utils import config
from ...pages import home
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.implicitly_wait(15)

page = home.HomePage(driver)
@given('I have navigated to the registration page')
def step_impl(context):
    url = config.get_property('general','home_url')


@when('I register with {email} and {password}')
def step_impl(context, email, password):
    url = config.get_property('general','home_url')


@then('I should see a confirmation message')
def step_impl(context):
    url = config.get_property('general','home_url')


@when('I register with {email},{password},{password2}')
def step_impl(context,email,password,password2):
    url = config.get_property('general','home_url')

@then('I should see {error}')
def step_impl(context, error):
    driver.quit()