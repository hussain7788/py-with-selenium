from pm.test.locators.lc_admin import *
from pm.test.locators.lc_common import *
import pandas as pd
from django.conf import settings
from pm.test.selenium_utility.sl_functions import *

class common_utils():
    def __init__(self, driver):
        self.driver = driver

    def signin(self, params, response):
        driver = self.driver
        # settings.configure()
        # url = settings.BASE_URL
        url = lc_common.URL + "/signin"
        sl_get_url(driver, url)
        sl_send_keys(driver, lc_common.sign_in_email, params['user_name'])
        sl_send_keys(driver, lc_common.sign_in_password, params['password'])
        sl_button_click(driver, lc_common.sign_in_submit)

    def register_new_admin(self, params, response):
        driver = self.driver
        url = lc_common.URL + "/signin"
        sl_get_url(driver, url)
        sl_button_click(driver, lc_common.register_new_member)

    def signout(self, params, response):
        driver = self.driver
        # sl_time_sleep(0)
        sl_button_hover_click(driver, lc_all_common.profile_dropdown, lc_all_common.logout)

class navigation():
    def __init__(self, driver):
        self.driver = driver

    def drop_down_navigation(self, params, response):
        driver = self.driver
        #sl_time_sleep()
        sl_button_hover_click(driver, params['menu_option'], params['sub_menu_option'])
        # sl_button_click(driver, params['menu_option'])
        #sl_time_sleep()
        # sl_button_click(driver, params['sub_menu_option'])

    def menu_navigation(self, params, response):
        driver = self.driver
        sl_button_click(driver, params['menu_option'])

    def side_menu_navigation(self, params, response):
        driver = self.driver
        sl_button_click(driver, params['side_menu_option'])

    def tab_navigation(self, params, response):
        driver = self.driver
        sl_button_click(driver, params['tab_name'])

class table_validation():
    __instance = None
    @staticmethod
    def get_instance():
        """ Static access method """
        if table_validation.__instance == None:
            table_validation()
        return table_validation.__instance

    def __init__(self):
        """ Virtually private constructor """
        if table_validation.__instance != None:
            raise Exception("This class is a singleton")
        else:
            table_validation.__instance = self


    def __parse_html_table(self, params, response):
        driver = params['driver']
        table_id = params['table_id']
        table_html = sl_get_outer_html(driver, table_id)
        table = pd.read_html(table_html)
        response['table'] = table[0]
        return table[0]

    def __check_misc_value(self, params, response):
        row = params['row']
        misc_col = params['misc_col']
        misc_values = params['misc_values']
        if len(misc_col) != len(misc_values):
            raise Exception("The Misc Column and Misc Values list are not the same length")

        iter_count = 0
        for col in misc_col:
            if row[col] == misc_values[iter_count]:
                iter_count += 1
            else:
                return False
        return True

    def table_search(self, params, response):
        driver = params['driver'] #Driver obj
        table_id = params['table_id'] # String
        primary_col = params['l_primary_col'] #List
        primary_values = params['l_l_primary_values'] #List of List
        if len(primary_col) == str():
            raise Exception("Primary column is empty")

        if len(primary_values) == 0:
            raise Exception("Primary values is empty list")

        try:
            misc_col = params['l_misc_col']
        except KeyError:
            misc_col = False
        else:
            misc_col = params['l_misc_col']
            misc_values = params['l_l_misc_values']

        if misc_col != False:
            if len(primary_values) != len(misc_values):
                raise Exception("Primary values and misc values are not the same length")

        return_list = [False] * len(primary_values)
        table = self.__parse_html_table(params, response)
        #pdb.set_trace()

        for index, row in table.iterrows():
            check_misc = True
            index_to_insert = -1
            col_itercount = 0
            row_itercount = 0
            for value in primary_values:
                col_itercount = 0
                for col in primary_col:
                    if row[col] == primary_values[row_itercount][col_itercount]:
                        check_misc = True
                        index_to_insert = row_itercount
                    else:
                        check_misc = False
                        index_to_insert = -1
                        break
                    col_itercount += 1
                row_itercount += 1
                if check_misc == True:
                    break
            if check_misc == True:
                if misc_col != False:
                    this_misc_values = misc_values[index_to_insert]
                    miscParams = dict()
                    miscResponse = dict()
                    miscParams['misc_col'] = misc_col
                    miscParams['misc_values'] = this_misc_values
                    miscParams['row'] = row
                    misc_pass = self.__check_misc_value(miscParams, miscResponse)
                    return_list[index_to_insert] = misc_pass
                else:
                    return_list[index_to_insert] = True

        response['l_result_per_primary_value'] = return_list
        response['result'] = True
        for item_result in response['l_result_per_primary_value']:
            if item_result == False:
                response['result'] = False
                break
        return response['result']

    def table_row_count(self, params, response):
        driver = params['driver']
        table_id = params['table_id']
        table = self.__parse_html_table(params, response)

        count = 0
        for index, row in table.iterrows():
            if index == 0:
                continue
            count = count + 1
        return count
        # print(" row count is:", count)
