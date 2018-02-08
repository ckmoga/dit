from behave import *
from ...pages import register
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(15)

page = register.RegistrationPage(driver)
@given('I have navigated to the registration page')
def step_impl(context):
    driver.get(page.registration_page_url)
    assert page.get_title(driver) == page.registration_page_title

@when('I register with {email} and {password}')
def step_impl(context, email, password):
    page.fill_registration_form(email,email,password,password,driver)

@then('I should see a confirmation message')
def step_impl(context):
    assert page.get_confirmation_page_title(driver) == page.confirmation_page_title

@when('I register with {email},{password},{password2}')
def step_impl(context,email,password,password2):
    page.fill_registration_form(email,email,password,password2,driver)

@then('I should see error {error}')
def step_impl(context, error):
    assert page.get_error(driver) == error

@when('I register with {email},{email2}')
def step_impl(context,email,email2):
    page.fill_registration_form(email,email2,'assignmenT18','assignmenT18',driver)

@then('the form will not be submitted')
def step_impl(context):
    assert page.get_title(driver) == page.registration_page_title

@then('I should see the error {error} displayed')
def step_impl(context, error):
    assert page.get_error(driver) == error
    driver.quit()