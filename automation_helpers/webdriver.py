from selenium import webdriver

class webDriver():


        def loadDriver(self):
                print("Addig the webdriver details")
                #driver = webdriver.Firefox("/usr/local/bin/geckodriver")
                driver = webdriver.Firefox("usr/local/bin")
                #self.version = webdriver.Firefox()..save_screenshot("screenshot.png")
                driver = driver
                print("Loading the web driver")
                print("loading the page ...")
                driver.get("https://www.facebook.com/")
                return driver







