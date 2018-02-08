from page_objects import PageObject, PageElement, MultiPageElement
from selenium import webdriver

class RegistrationPage(PageObject):
    registration_page_url   = 'https://sso.trade.great.gov.uk/accounts/signup/?next=https://www.great.gov.uk/triage/'
    confirmation_page_url   = 'https://sso.trade.great.gov.uk/accounts/confirm-email/'
    email                   = PageElement(name="email")
    confirm_email           = PageElement(name="email2")
    password                = PageElement(name="password1")
    confirm_password        = PageElement(name="password2")
    terms_and_conditions    = PageElement(id_="id_terms_agreed")
    register_button         = PageElement(css="#signup_form > button")
    registration_page_title = 'Register'
    confirmation_page_title = 'Verify your email address'

    def fill_registration_form(self,email1,email2,password1,password2, driver):
        self.email              = email1
        self.confirm_email      = email2
        self.password           = password1
        self.confirm_password   = password2
        driver.execute_script("window.scrollTo(0, 1200)") #make register button and terms checkbox visible
        self.terms_and_conditions.click()
        self.register_button.click()

    def get_title(self,driver):
        return driver.find_element_by_css_selector('#profile-register-intro > h1').text

    def get_confirmation_page_title(self,driver):
        return driver.find_element_by_css_selector('#content > div > div > h1').text

    def get_error(self,driver):
        return driver.find_element_by_css_selector('#signup_form > li.input-field-container.has-error > ul > li:nth-child(1)').text

