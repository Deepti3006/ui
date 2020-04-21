from selenium import webdriver

class webDriver():


        def __init__(self):
                print("Addig the webdriver details")
                self.driver = webdriver.Firefox()
                self.version = webdriver.Firefox().save_screenshot("screenshot.png")
                driver = self.driver
                print("Loading the web driver")
                print("loading the page ...")
                driver.get("https://www.facebook.com/")







