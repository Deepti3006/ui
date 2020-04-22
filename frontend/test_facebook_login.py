#import pytest
from ui.automation_helpers.page_objects_helper import pageObjectHelper


class TestFacebook(pageObjectHelper):

    def test_login(self):

        self.LT,self.LP,self.LB =pageObjectHelper.check(self)

        self.LT.send_keys("deepti.madhuri@gmail.com")

        self.LP.send_keys("deepti1")
        self.LB.click()





