from page_objects import PageObject, PageElement, MultiPageElement
from selenium import webdriver

class HomePage(PageObject):
    home     = PageElement(css="#header-home-link")
    journey  = PageElement(css="#header-custom-page-link")
    export   = PageElement(css="#export-readiness-links")
    guide    = PageElement(css="#header-guidance-links")
    service  = PageElement(css="#header-services-links")
    register = PageElement(css='#header-register-link')