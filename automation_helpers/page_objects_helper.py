from ui import *
from ui.automation_helpers.webdriver import webDriver


class pageObjectHelper(webDriver):

       def check(self):
                print("loading the page objects")
                driver = webDriver.loadDriver(self)
                LOGIN_TEXTBOX = driver.find_element_by_name("email")
                print("TBs")
                #LOGIN_TEXTBOX = self.LOGIN_TEXTBOX
                LOGIN_PASSWORD = driver.find_element_by_name("pass")
                #LOGIN_PASSWORD = self.LOGIN_PASSWORD
                LOGIN_BUTTON =driver.find_element_by_id("loginbutton")
        #LOGIN_BUTTON = self.LOGIN_BUTTON
                return LOGIN_TEXTBOX, LOGIN_PASSWORD, LOGIN_BUTTON


