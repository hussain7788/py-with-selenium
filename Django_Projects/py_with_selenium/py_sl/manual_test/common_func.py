from selenium import webdriver
from selenium.webdriver.support.ui import Select

class navigation():
    def __init__(self, driver):
        self.driver = driver

    def manu_nav(self, params, response):
        driver = self.driver
        driver.find_element_by_id(params['main_menu']).click()

class common_utils():
    def __init__(self, driver):
        self.driver = driver

    def signin(self, params, response):
        driver = self.driver
        url = "https://www.cpasage.com/signin/"
        driver.get(url)
        driver.find_element_by_id("user").send_keys(params['user_name'])
        driver.find_element_by_id("password").send_keys(params['password'])
        driver.find_element_by_id("submit").click()