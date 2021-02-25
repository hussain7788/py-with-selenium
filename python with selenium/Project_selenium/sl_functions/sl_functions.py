from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *

import time

EXPLICIT_WAIT_TIME = 10
POLL_FREQUENCY = 1


def sl_time_sleep(sec=0):
    time.sleep(sec)


def wait_for_exceptions(driver):
    l_exceptions = [ElementNotVisibleException,
                    ElementNotInteractableException,
                    ElementNotSelectableException,
                    StaleElementReferenceException,
                    NoSuchElementException,
                    ]
    return WebDriverWait(driver, EXPLICIT_WAIT_TIME, poll_frequency=POLL_FREQUENCY, ignored_exceptions=l_exceptions)


def sl_get_url(driver, url):
    driver.get(url)


def sl_find_locator(driver, locator):
    driver.execute_script("manage().timeouts().implicitlyWait(0, TimeUnit.SECONDS)")
    element = driver.find_element_by_id(locator)
    driver.execute_script("manage().timeouts().implicitlyWait(3, TimeUnit.SECONDS)")
    return element


def sl_find_locator_wait(driver, locator):
    try:
        wait = wait_for_exceptions(driver)
        element = wait.until(
            EC.presence_of_element_located((By.ID, locator))
        )
        return element
    finally:
        pass


def sl_find_locator_xpath_wait(driver, locator):
    try:
        wait = wait_for_exceptions(driver)
        element = wait.until(
            EC.presence_of_element_located((By.XPATH, locator))
        )
        return element
    finally:
        pass


def sl_button_click(driver, locator):
    try:
        wait = wait_for_exceptions(driver)
        button = wait.until(
            EC.element_to_be_clickable((By.ID, locator))
        )
        driver.execute_script("arguments[0].click();", button)
    finally:
        pass


def sl_button_click_xpath(driver, locator):
    try:
        wait = wait_for_exceptions(driver)
        button = wait.until(
            EC.element_to_be_clickable((By.XPATH, locator))
        )
        driver.execute_script("arguments[0].click();", button)
    finally:
        pass


def sl_button_hover_click(driver, locator1, locator2):
    try:
        action = ActionChains(driver)
        menu = sl_find_locator_wait(driver, locator1)
        action.move_to_element(menu).perform()
        option = sl_find_locator_wait(driver, locator2)
        driver.execute_script("arguments[0].click();", option)
    finally:
        pass


def sl_send_keys(driver, locator, value):
    # sl_find_locator_wait(driver, locator).send_keys(value)
    element = sl_find_locator_wait(driver, locator)
    driver.execute_script("arguments[0].setAttribute('value', arguments[1])", element, value)


def sl_send_keys_xpath(driver, locator, value):
    # sl_find_locator_xpath_wait(driver, locator).send_keys(value)
    element = sl_find_locator_xpath_wait(driver, locator)
    driver.execute_script("arguments[0].setAttribute('value', arguments[1])", element, value)


def sl_send_keys_2(driver, locator1, locator2, value):
    sl_find_locator_wait(driver, locator1).find_element_by_id(locator2).send_keys(value)


def sl_send_keys_alt(driver, locator, date):
    sl_find_locator_wait(driver, locator).send_keys(date)


def sl_send_date_time(driver, locator, date, time):
    date_time = sl_find_locator_wait(driver, locator)
    date_time.send_keys(date)
    date_time.send_keys(Keys.TAB)
    date_time.send_keys(time)


def sl_select_dropdown(driver, locator, value):
    sl_time_sleep(0.1)
    Select(sl_find_locator_wait(driver, locator)).select_by_visible_text(value)


def sl_select_dropdown_2(driver, locator1, locator2, value):
    sl_time_sleep(0.1)
    Select(sl_find_locator_wait(driver, locator1).find_element_by_id(locator2)).select_by_visible_text(value)


def sl_get_text(driver, locator):
    return sl_find_locator_wait(driver, locator).get_attribute('innerText')


def sl_get_split_text(driver, locator, delimiter):
    return sl_find_locator_wait(driver, locator).text.split(delimiter)


def sl_clear_text(driver, locator):
    element = sl_find_locator_wait(driver, locator)
    driver.execute_script("arguments[0].setAttribute('value', arguments[1])", element, '')


def sl_clear_text_2(driver, locator1, locator2):
    sl_find_locator_wait(driver, locator1).find_element_by_id(locator2).clear()


def sl_get_outer_html(driver, locator):
    return sl_find_locator_wait(driver, locator).get_attribute('outerHTML')


def sl_checkbox_is_selected(driver, locator):
    return sl_find_locator_wait(driver, locator).is_selected()


def sl_get_current_window_handle(driver):
    return driver.current_window_handle


def sl_get_window_handles(driver):
    return driver.window_handles


def sl_switch_to_window(driver, window_handle):
    driver.switch_to.window(window_handle)


def sl_get_length(driver, locator, tag_name):
    script_text = "return document.getElementById(" + "'" + str(
        locator) + "'" + ")" + ".getElementsByTagName(" + "'" + str(tag_name) + "'" + ")" + ".length"
    return driver.execute_script(script_text)
