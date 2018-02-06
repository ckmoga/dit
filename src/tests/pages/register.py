from page_objects import PageObject, PageElement, MultiPageElement
from selenium import webdriver

class RegistrationPage(PageObject):
    email      = PageElement(name="email")
    email2     = PageElement(name="email2")
    password1  = PageElement(name="password1")
    password2  = PageElement(name="password2")
    terms      = PageElement(id_="id_terms_agreed")
    button     = PageElement(css="#signup_form > button")