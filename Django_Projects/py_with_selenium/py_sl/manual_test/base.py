from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pytest
import time
import pdb

driver = None


def get_driver(browser):
    global driver
    if driver == None:
        if browser == "chrome":
            br_options = Options()
            driver = webdriver.Chrome(executable_path="E:\chrome driver\chromedriver.exe")
            driver.maximize_window()
            driver.implicitly_wait(2)

    return driver


class base_test_case():
    def get_driver(self):
        self.driver = get_driver("chrome")

    def quit(self):
        global driver
        driver.quit()
        driver = None








