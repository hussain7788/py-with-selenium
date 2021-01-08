from pm.test.locators.lc_admin import *
from pm.test.locators.lc_common import *
from pm.test.locators.lc_client import *
from pm.test.utils.common_functions import *
from pm.test.pages.admin.pg_client_actions import *
from pm.test.selenium_utility.sl_functions import *
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class pg_admin_client_dashboard(navigation):
    def __init__(self, driver):
        self.driver = driver
        super(pg_admin_client_dashboard, self).__init__(driver)

    def navigate_admin_client_dashboard(self, params, response):
        driver = self.driver
        params = dict()
        response = dict()
        params['side_menu_option'] = lc_client_side_menu.client_file
        super(pg_admin_client_dashboard, self).side_menu_navigation(params, response)

    def update_client_dashboard_notes(self, params,  response):
        driver = self.driver
        # #sl_time_sleep(0)
        sl_button_click(driver, lc_client_dashboard.edit_notes)
        # #sl_time_sleep(0)
        sl_clear_text(driver, lc_client_dashboard.notes)
        sl_send_keys(driver, lc_client_dashboard.notes, params['notes'])
        sl_button_click(driver, lc_client_dashboard.update_notes)

    def open_client_msgs(self, params, response):
        driver = self.driver
        #sl_time_sleep(1)
        sl_button_click(driver, lc_client_dashboard.view_client_messages)

    def view_and_send_client_msg(self, params, response):
        driver = self.driver
        #sl_time_sleep(1)
        try:
            params['action']
        except KeyError:
            if params['send_msg_access'] == True:
                params['bodyText'] = sl_get_text(driver, 'clientMessageBody')
                sl_send_keys(driver, lc_client_dashboard.client_message_text, params['clientMessageText'])
                sl_button_click(driver, lc_client_dashboard.send_client_message)

        else:
            params['bodyText'] = sl_get_split_text(driver, 'clientMessageBody', '2020')

    def hide_client_msgs(self, params, response):
        driver = self.driver
        #sl_time_sleep(1)
        sl_button_click(driver, lc_client_dashboard.view_client_messages)

    def open_team_msgs(self, params, response):
        driver = self.driver
        #sl_time_sleep(1)
        sl_button_click(driver, lc_client_dashboard.view_team_messages)

    def view_and_send_team_msg(self, params, response):
        driver = self.driver
        #sl_time_sleep(1)
        try:
            params['action']
        except KeyError:
            if params['send_msg_access'] == True:
                params['bodyText'] = sl_get_text(driver, 'teamMessageBody',)
                sl_send_keys(driver, lc_client_dashboard.team_message_text, params['teamMessageText'])
                sl_button_click(driver, lc_client_dashboard.send_team_message)
        else:
            print("false")

    def hide_team_msgs(self, params, response):
        driver = self.driver
        #sl_time_sleep(1)
        sl_button_click(driver, lc_client_dashboard.view_team_messages)

    def open_todo_task(self, params, response):
        driver = self.driver
        #sl_time_sleep(1)
        sl_button_click(driver, lc_client_dashboard.view_todo_task)
        try:
            params['todo_task_length'] = sl_get_length(driver, 'todoTaskBody', 'ul')
        except:
            print("No todo tasks")
        else:
            print("todo task length is:", params['todo_task_length'])

    def add_client_dashboard_todo_task(self, params, response):
        driver = self.driver
        #sl_time_sleep(1)
        sl_button_click(driver, lc_client_dashboard.add_ToDo)
        sl_send_keys(driver, lc_client_dashboard.todo_Due_Date, params['todoDueDate'])
        sl_send_keys(driver, lc_client_dashboard.todo_Task, params['todoTask'])
        sl_button_click(driver, lc_client_dashboard.add_ToDo_Task)

    def complete_client_todo_task(self, params, response):
        driver = self.driver
        #sl_time_sleep(1)
        sl_button_click(driver, params['todo_complete'])

    def hide_todo_task(self, params, response):
        driver = self.driver
        #sl_time_sleep(1)
        sl_button_click(driver, lc_client_dashboard.view_todo_task)

    def navigate_client_dashboard_active_engage(self, params, response):
        driver = self.driver
        try:
            params['tab_name']
        except KeyError:
            pass
        else:
            params1 = dict()
            response1 = dict()
            if params['tab_name'] == "PersonalTab":
                params1['tab_name'] = lc_all_common.personal_tab
            elif params['tab_name'] == "BusinessTab":
                params1['tab_name'] = lc_all_common.business_tab
            else:
                print("Invalid active_eng tab selection")
            super(pg_admin_client_dashboard, self).tab_navigation(params1, response1)

class pg_admin_client_doc(navigation):
    def __init__(self, driver):
        self.driver = driver
        super(pg_admin_client_doc, self).__init__(driver)

    def navigate_to_client_doc(self, params, response):
        driver = self.driver
        params = dict()
        response = dict()
        ##sl_time_sleep()
        params['side_menu_option'] = lc_client_side_menu.client_documents
        super(pg_admin_client_doc, self).side_menu_navigation(params, response)

    def navigate_to_client_doc_tabs(self, params, response):
        driver = self.driver
        # sl_select_dropdown(driver, lc_all_common.tax_year, params['tax_year'])
        # import pdb; pdb.set_trace()
        if params['tab_name'] == "personalTab":
            sl_button_click(driver, lc_all_common.personal_tab)

        elif params['tab_name'] == "businessTab":
            sl_button_click(driver, lc_all_common.business_tab)
        #sl_time_sleep(1)
        sl_button_click(driver, params['sub_tab'])

    def check_admin_client_doc_checkboxes(self, params, response):
        driver = self.driver
        ##sl_time_sleep()
        if sl_checkbox_is_selected(driver, params['file_checkbox']) != True:
            sl_button_click(driver, params['file_checkbox'])
        else:
            print("file checkbox is Already selected")

    def view_admin_client_doc_file(self, params, response):
        driver = self.driver
        ##sl_time_sleep()
        main_window_handle = None
        while not main_window_handle:
            main_window_handle = driver.current_window_handle
        sl_button_click(driver, params['view_file'])

        signin_window_handle = None
        while not signin_window_handle:
            for handle in driver.window_handles:
                if handle != main_window_handle:
                    signin_window_handle = handle
                    break

        driver.switch_to.window(signin_window_handle)
        driver.switch_to.window(main_window_handle)

    def download_admin_client_doc_file(self, params, response):
        driver = self.driver
        ##sl_time_sleep()
        sl_button_click(driver, params['downld_file'])

    def delete_admin_client_doc_file(self, params, response):
        driver = self.driver
        sl_button_click(driver, params['del_file'])

    def click_client_add_files_btn(self, params, response):
        driver = self.driver
        import pdb
        pdb.set_trace()
        sl_button_click(driver, lc_client_documents.add_files_btn)

    def populate_client_file_upload_dtls(self, params, response):
        driver = self.driver
        # import pdb; pdb.set_trace()
        if params['tab_name'] == "personalTab":
            sl_button_click(driver, lc_all_common.personal_tab)

        elif params['tab_name'] == "businessTab":
            sl_button_click(driver, lc_all_common.business_tab)
            sl_select_dropdown(driver, lc_client_documents.bns_name, params['bns_name'])
        sl_time_sleep(1)
        sl_select_dropdown(driver, lc_all_common.tax_year, params['tax_year'])

        if params['client_login_access'] != True:
            sl_select_dropdown(driver, lc_client_documents.document_source, params['document_source'])

    def client_add_files(self, params, response):
        driver = self.driver
        sl_time_sleep(1)
        sl_select_dropdown(driver, params['documentType'], params['file_type'])
        sl_send_keys(driver, params['chooseFileBtn'], params['full_file_name'])

    def add_new_doc(self):
        driver = self.driver
        sl_time_sleep(1)
        sl_button_click(driver, lc_client_documents.add_document_btn)

    def client_upload_files(self, params, response):
        driver = self.driver
        sl_button_click(driver, lc_all_common.save_btn)
        sl_button_click(driver, lc_all_common.close_btn)
        sl_refresh(driver)

class pg_admin_client_status(navigation):
    def __init__(self, driver):
        self.driver = driver
        super(pg_admin_client_status, self).__init__(driver)

    def navigate_admin_client_status(self, params, response):
        driver = self.driver
        params = dict()
        response = dict()
        params['menu_option'] = lc_client_side_menu.client_status
        super(pg_admin_client_status, self).menu_navigation(params, response)

    def navigate_to_admin_client_status_tabs(self, params, response):
        driver = self.driver
        ##sl_time_sleep()

        if params['tab_name'] == "PersonalTab":
            sl_button_click(driver, lc_all_common.personal_tab)
            sl_button_click(driver, lc_client_status.edit_btn)

        elif params['tab_name'] == "BusinessTab":
            sl_button_click(driver, lc_all_common.business_tab)
            sl_button_click(driver, lc_client_status.edit_btn)

    def update_admin_client_status(self, params, response):
        driver =  self.driver
        ##sl_time_sleep()

        if params['emp_status_access'] != True:
            sl_select_dropdown(driver, params['manager_dropdown'], params['manager_names'])
            sl_select_dropdown(driver,  params['employee_dropdown'], params['employee_names'])

        ##sl_time_sleep()
        # driver.find_element_by_id(params['extension_checkbox'])
        ##sl_time_sleep()
        sl_select_dropdown(driver, params['status_dropdown'], params['status_name'])
        ##sl_time_sleep()

    def clicking_on_admin_client_status_update(self, params, response):
        driver = self.driver
        sl_button_click(driver, lc_client_status.update_btn)

    def check_admin_client_history(self, params, response):
        driver = self.driver
        ##sl_time_sleep()
        sl_button_click(driver, params['history_button'])
        sl_button_click(driver, lc_all_common.close_btn)

class pg_admin_client_business(navigation):
    def __init__(self, driver):
        self.driver = driver
        super(pg_admin_client_business, self).__init__(driver)

    def navigate_admin_client_business(self, params, response):
        driver = self.driver
        params = dict()
        response = dict()
        params['menu_option'] = lc_client_side_menu.client_business
        super(pg_admin_client_business, self).menu_navigation(params, response)

    def client_add_business(self, params, response):
        driver = self.driver
        sl_button_click(driver, lc_client_business.add_business)
        sl_send_keys(driver, lc_client_business.bns_name, params['bns_name'])
        sl_select_dropdown(driver, lc_client_business.bns_type, params['bns_type'])
        sl_select_dropdown(driver, lc_client_business.bns_inc_state, params['bns_inc_state'])
        sl_send_keys(driver, lc_client_business.bns_inc_date, params['bns_inc_date'])

        if params['bk_checkbox'] == True:
            sl_button_click(driver, lc_client_business.bk_checkbox)
            sl_select_dropdown(driver, lc_client_business.bk_frequency, params['bk_frequency'])

        if params['pr_checkbox'] == True:
            sl_button_click(driver, lc_client_business.pr_checkbox)
            sl_select_dropdown(driver, lc_client_business.pr_frequency, params['pr_frequency'])

        if params['st_checkbox'] == True:
            sl_button_click(driver, lc_client_business.st_checkbox)
            sl_select_dropdown(driver, lc_client_business.st_frequency, params['st_frequency'])

        if params['tp_checkbox'] == True:
            sl_button_click(driver, lc_client_business.tp_checkbox)
            sl_select_dropdown(driver, lc_client_business.tp_frequency, params['tp_frequency'])

        sl_button_click(driver, lc_all_common.save_btn)
        sl_refresh(driver)

    def client_edit_business(self, params, response):
        driver = self.driver
        ##sl_time_sleep()
        sl_button_click(driver, lc_client_business.edit_business_btn)

    def client_update_business(self, params, response):
        driver = self.driver
        ##sl_time_sleep()
        sl_select_dropdown(driver, params['bk_frequency'], params['bk_frequency_value'])
        ##sl_time_sleep()
        sl_select_dropdown(driver, params['pr_frequency'], params['pr_frequency_value'])
        sl_select_dropdown(driver, params['st_frequency'], params['st_frequency_value'])
        sl_select_dropdown(driver, params['tp_frequency'], params['tp_frequency_value'])

    def click_on_client_update_business(self, params, response):
        driver = self.driver
        ##sl_time_sleep()
        sl_button_click(driver, lc_client_business.update_business_btn)

class pg_admin_client_price_est(navigation):
    def __init__(self, driver):
        self.driver = driver
        super(pg_admin_client_price_est, self).__init__(driver)

    def navigate_admin_client_price_est(self, params, response):
        driver = self.driver
        params = dict()
        response = dict()
        params['side_menu_option'] = lc_client_side_menu.client_price_est
        super(pg_admin_client_price_est, self).side_menu_navigation(params, response)

    def navigate_to_client_price_est_tabs(self, params, response):
        driver = self.driver
        #sl_time_sleep(1)

        if params['tab_name'] == "PersonalTab":
            sl_button_click(driver, lc_all_common.personal_tab)
            sl_button_click(driver, lc_client_price_est.edit_btn)

        elif params['tab_name'] == "BusinessTab":
            sl_button_click(driver, lc_all_common.business_tab)
            sl_button_click(driver, lc_client_price_est.edit_btn)

    def updating_client_price_est(self, params, response):
        driver =  self.driver
        #sl_time_sleep(1)
        sl_clear_text(driver, params['adjust_id'])
        sl_send_keys(driver, params['adjust_id'], params['adjust_value'])

    def click_on_price_est_update_btn(self, params, response):
        driver =  self.driver
        sl_button_click(driver, lc_client_price_est.update_btn)

class pg_admin_client_invoice(navigation):
    def __init__(self, driver):
        self.driver = driver
        # #sl_time_sleep(0)
        super(pg_admin_client_invoice, self).__init__(driver)

    def navigate_admin_client_invoice(self, params, response):
        driver = self.driver
        params = dict()
        response = dict()
        #sl_time_sleep(1)
        params['side_menu_option'] = lc_client_side_menu.client_invoice
        super(pg_admin_client_invoice, self).side_menu_navigation(params, response)
        #sl_time_sleep(1)

    def click_on_client_invoice_btn(self, params, response):
        driver = self.driver
        #sl_time_sleep(1)
        sl_button_click(driver, lc_client_invoice.add_invoice_btn)

    def client_add_invoice(self, params, response):
        driver = self.driver
        formblock = str("formBlock"+ str(params['count']))
        sl_send_keys_2(driver, formblock, lc_client_invoice.description, params['description'])
        #sl_time_sleep(0.99)
        sl_send_keys_2(driver, formblock, lc_client_invoice.qty, params['quantity'])
        sl_send_keys_2(driver, formblock, lc_client_invoice.price, params['price'])
        if params['last_invoice_indicator'] == 'n':
            sl_button_click(driver, lc_client_invoice.add_invoice_row)

    def click_on_client_add_invoice(self, params, response):
        driver = self.driver
        sl_button_click(driver, lc_client_invoice.add_invoice_btn2)

    def client_invoice_details(self, params, response):
        driver = self.driver
        sl_button_click(driver, params['details'])

    def click_client_invoice_edit(self, params, response):
        driver = self.driver
        ##sl_time_sleep()
        sl_button_click(driver, lc_main_dashboard.edit_button)

    def edit_client_invoice_details(self, params, response):
        driver = self.driver
        formblock = str("formBlock"+ str(params['count']))
        ##sl_time_sleep()
        sl_clear_text_2(driver, formblock, lc_client_invoice.description)
        sl_send_keys_2(driver, formblock, lc_client_invoice.description, params['description'])
        sl_clear_text_2(driver, formblock, lc_client_invoice.qty)
        sl_send_keys_2(driver, formblock, lc_client_invoice.qty, params['quantity'])
        sl_clear_text_2(driver, formblock, lc_client_invoice.price)
        sl_send_keys_2(driver, formblock, lc_client_invoice.price, params['price'])
        # if params['last_invoice_indicator'] == 'n':
        #     driver.find_element_by_id(lc_client_invoice.add_invoice_row).click()

    def client_invoice_paid(self, params, response):
        driver = self.driver
        ##sl_time_sleep()
        sl_button_click(driver, params['paid_date'])

################################################################################################################################

# client login dashboard page objects

class pg_client_login_main_dashboard(navigation):
    def __init__(self, driver):
        self.driver = driver
        super(pg_client_login_main_dashboard, self).__init__(driver)

    def client_dashboard_check_todo_checkbox(self, params, response):
        driver = self.driver
        #sl_time_sleep(1)
        if sl_checkbox_is_selected(driver, params['todo_check']) != True:
            sl_button_click(driver, params['todo_check'])
        else:
            print("Already checkbox is selected")

    def client_dashboard_uncheck_todo_checkbox(self, params, response):
        driver = self.driver
        # #sl_time_sleep(0)
        if sl_checkbox_is_selected(driver, params['todo_check']) == True:
            sl_button_click(driver, params['todo_check'])
        else:
            print("Already checkbox is unselected")

class pg_client_login_template(navigation):
    def __init__(self, driver):
        self.driver = driver
        super(pg_client_login_template, self).__init__(driver)

    def navigate_client_template(self, params, response):
        driver = self.driver
        params = dict()
        response = dict()
        params['side_menu_option'] = lc_client_side_menu.client_templates
        super(pg_client_login_template, self).side_menu_navigation(params, response)
        try:
            params['tab_name']
        except KeyError:
            pass
        else:
            params1 = dict()
            response1 = dict()
            if params['tab_name'] == "PersonalTab":
                params1['tab_name'] = lc_all_common.personal_tab
            if params['tab_name'] == "BusinessTab":
                params1['tab_name'] = lc_all_common.business_tab
            else:
                raise Exception("Invalid active_eng tab selection")
            super(pg_client_login_template, self).tab_navigation(params1, response1)

    def actions_on_client_login_template(self, params, response):
        driver = self.driver
        ##sl_time_sleep()
        main_window_handle = None
        while not main_window_handle:
            main_window_handle = driver.current_window_handle
        sl_button_click(driver, params['view_file'])

        signin_window_handle = None
        while not signin_window_handle:
            for handle in driver.window_handles:
                if handle != main_window_handle:
                    signin_window_handle = handle
                    break

        driver.switch_to.window(signin_window_handle)
        driver.switch_to.window(main_window_handle)
        sl_button_click(driver, params['download_file'])

############################################################################################################

# employee login dashboard page objects
class pg_emp_login_main_dashboard(navigation):
    def __init__(self, driver):
        self.driver = driver
        super(pg_emp_login_main_dashboard, self).__init__(driver)

    def navigate_from_main_dashboard_to_client_dashboard(self, params, response):
        driver = self.driver
        #sl_time_sleep(1)
        params['menu_option'] = lc_admin_menu.task_option
        params['sub_menu_option'] = lc_task.all_task_list
        super(pg_emp_login_main_dashboard, self).drop_down_navigation(params, response)
        #sl_time_sleep(1)
        sl_select_dropdown(driver, lc_all_common.tax_year, "All")
        if params['tab_name'] == 'PersonalTab':
            sl_button_click(driver, lc_all_common.personal_tab)

        elif params['tab_name'] == 'BusinessTab':
            sl_button_click(driver, lc_all_common.business_tab)
        #sl_time_sleep(0.99)
        sl_button_click(driver, params['emp_nav_link'])
###############################################################################################################

# recep login dashboard page objects
class pg_recep_login_main_dashboard(navigation):
    def __init__(self, driver):
        self.driver = driver
        super(pg_recep_login_main_dashboard, self).__init__(driver)

    def navigate_from_client_list_to_recep_dashboard(self, params, response):
        driver = self.driver
        ##sl_time_sleep()
        sl_button_click(driver, params['recep_dashboard_link'])
