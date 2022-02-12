import webbrowser
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
        if browser == "chrome" or browser == "headless":
            options = Options()
            options.add_experimental_option(
                'excludeSwitches', ['enable-logging'])
            if browser == "headless":
                options.headless = True
            driver = webdriver.Chrome(
                executable_path="D:\Chrome_Driver\chromedriver.exe", chrome_options=options)
            driver.maximize_window()

    return driver


class Base():
    def get_driver(self):
        self.driver = get_driver("headless")

    def close_driver(self):
        global driver
        driver.quit()
        driver = None


@pytest.mark.test_page
class Test_web(Base):
    def test_0_open_web(self):
        super().get_driver()
        driver = self.driver
        driver.get("https://www.intelws.com/")
        time.sleep(5)
        text = driver.find_element_by_xpath(
            "/html/body/header/div/nav/ul/li[1]/a")
        time.sleep(2)
        # driver.find_element_by_xpath(
        #     "/html/body/header/div/nav/ul/li[2]/a").click()
        # time.sleep(2)
        # driver.find_element_by_xpath(
        #     "/html/body/header/div/nav/ul/li[3]/a").click()
        # time.sleep(2)
        # links = driver.find_elements_by_tag_name("a")
        # print("links::", links)
        # for link in links:
        #     print("attributes::", link)

    def test_1_quit(self):
        super().close_driver()
