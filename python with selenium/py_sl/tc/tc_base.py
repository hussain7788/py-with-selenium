#from django.test import LiveServerTestCase
from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time
import pdb

driver = None
tc_wait_time = 0
def get_driver(browser, isHeadLess=True):
    # pdb.set_trace()
    global driver
    if driver == None:
        if browser == "chrome":
            from selenium.webdriver.chrome.options import Options
            chrome_options = Options()
            # chrome_options = webdriver.ChromeOptions()
            if isHeadLess:
                chrome_options.add_argument("headless")
                chrome_options.add_argument('--no-sandbox')
                chrome_options.add_argument('--disable-dev-shm-usage')
            driver = webdriver.Chrome(options=chrome_options)
            driver.implicitly_wait(3)
            driver.maximize_window()
        elif browser == "firefox":
            from selenium.webdriver.firefox.options import Options
            gecko_options = FirefoxOptions()
            gecko_options.headless = isHeadLess
            gecko_options.add_argument("--headless")
            gecko_options.add_argument("--width=2560")
            gecko_options.add_argument("--height=1440")
            driver = webdriver.Firefox(options=gecko_options)
        elif browser == "safari":
            driver = webdriver.Safari()
    return driver

def tc_pre_process():
    global tc_wait_time

def tc_post_process():
    global tc_wait_time

class base_test_case():
    def get_driver(self):
        self.driver = get_driver("chrome", False)

    def destroy_driver(self):
        global driver
        driver.quit()
        driver = None
