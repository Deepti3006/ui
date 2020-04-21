from Documents.sample_automation_framework.automation_helpers import *
from Documents.sample_automation_framework.automation_helpers.webdriver import webDriver


class pageObjectHelper(webDriver):


    def __init__(self):
        print("loading the page objects")
        wb = webDriver()
        self.LOGIN_TEXTBOX = wb.driver.find_element_by_name("email")
        print("TBs")
        LOGIN_TEXTBOX = self.LOGIN_TEXTBOX
        self.LOGIN_PASSWORD = wb.driver.find_element_by_name("pass")
        LOGIN_PASSWORD = self.LOGIN_PASSWORD
        self.LOGIN_BUTTON = wb.driver.find_element_by_id("loginbutton")
        LOGIN_BUTTON = self.LOGIN_BUTTON


