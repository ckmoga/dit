from behave import *
from ...utils import config
from ...pages import register
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(15)

page = register.RegistrationPage(driver)
@given('I have navigated to the registration page')
def step_impl(context):
    url = 'https://sso.trade.great.gov.uk/accounts/signup/?next=https://www.great.gov.uk/triage/'
    driver.get(url)
    title = driver.find_element_by_css_selector('#profile-register-intro > h1')
    assert title.text == 'Register'

@when('I register with {email} and {password}')
def step_impl(context, email, password):
    page.email = email
    page.email2 = email
    page.password1 = password
    page.password2 = password
    page.terms.click()

    driver.execute_script("window.scrollTo(0, 1200)") #bring button to view
    page.button.click()


@then('I should see a confirmation message')
def step_impl(context):
    url = 'https://sso.trade.great.gov.uk/accounts/confirm-email/'
    assert driver.current_url == url
    title = driver.find_element_by_css_selector('#content > div > div > h1')
    assert title.text == 'Verify your email address'

@when('I register with {email},{password},{password2}')
def step_impl(context,email,password,password2):
    url = config.get_property('general','home_url')

@then('I should see {error}')
def step_impl(context, error):
    driver.quit()