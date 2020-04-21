import pytest
from ui.automation_helpers.page_objects_helper import pageObjectHelper
pg = pageObjectHelper()


def test_login():



    pg.LOGIN_TEXTBOX.send_keys("deepti.madhuri@gmail.com")
    pg.LOGIN_PASSWORD.send_keys("deepti1")
    pg.LOGIN_BUTTON.click()



