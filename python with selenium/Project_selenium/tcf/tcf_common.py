from pm.test.pages.admin.pg_client_actions import *
from pm.test.pages.common.pg_client_dashboard import *
from pm.test.selenium_utility.sl_functions import *
import random

# dashboard functions
def tcf_navigate_admin_client_dashboard(params, response):
    obj = tcf_client_dashboard()
    obj.navigate_admin_client_dashboard(params, response)

def tcf_view_n_send_client_msg(params, response):
    obj = tcf_client_dashboard()
    obj.view_n_send_client_msg(params, response)

def tcf_view_n_send_team_msg(params, response):
    obj = tcf_client_dashboard()
    obj.view_n_send_team_msg(params, response)

def tcf_add_client_notes(params, response):
    obj = tcf_client_dashboard()
    obj.add_client_notes(params, response)

def tcf_open_todo_task(params, response):
    obj = tcf_client_dashboard()
    obj.open_todo_task(params, response)

def tcf_add_client_todo_task(params, response):
    obj = tcf_client_dashboard()
    obj.add_client_todo_task(params, response)

def tcf_complete_client_todo_task(params, response):
    obj = tcf_client_dashboard()
    obj.complete_client_todo_task(params, response)

def tcf_hide_todo_task(params, response):
    obj = tcf_client_dashboard()
    obj.hide_todo_task(params, response)

def tcf_navigate_to_client_active_engage(params, response):
    obj = tcf_client_dashboard()
    obj.navigate_to_client_active_engage(params, response)

# document functions
def tcf_navigate_admin_client_doc_tabs(params, response):
    obj = tcf_client_dashboard()
    obj.navigate_to_admin_client_doc_tabs(params, response)

def tcf_checking_admin_client_doc_checkboxes(params, response):
    obj = tcf_client_dashboard()
    obj.checking_admin_client_doc_checkboxes(params, response)

def tcf_view_admin_client_doc_file(params, response):
    obj = tcf_client_dashboard()
    obj.view_admin_client_doc_file(params, response)

def tcf_download_admin_client_doc_file(params, response):
    obj = tcf_client_dashboard()
    obj.download_admin_client_doc_file(params, response)

def tcf_delete_admin_client_doc_file(params, response):
    obj = tcf_client_dashboard()
    obj.delete_admin_client_doc_file(params, response)

# upload functions
# def tcf_click_client_add_files_btn(params, response):
#     obj = tcf_client_dashboard()
#     obj.click_client_add_files_btn(params, response)

def tcf_client_dashboard_upload(params, response):
    obj = tcf_client_dashboard()
    obj.client_file_upload(params, response)

# status functions
def tcf_update_admin_client_status(params, response):
    obj = tcf_client_dashboard()
    obj.update_admin_client_status(params, response)

def tcf_check_admin_client_history_status(params, response):
    obj_check_hist = tcf_client_dashboard()
    obj_check_hist.check_admin_client_history_status(params, response)

# business functions
def tcf_admin_client_add_business(params, response):
    obj_admin_client_add = tcf_client_dashboard()
    obj_admin_client_add.admin_client_add_business(params, response)

def tcf_client_edit_business(params, response):
    obj_edit = tcf_client_dashboard()
    obj_edit.client_edit_business(params, response)

# price est functions
def tcf_navigate_to_admin_client_price_est(params, response):
    obj_price = tcf_client_dashboard()
    obj_price.navigate_to_admin_client_price_est(params, response)

def tcf_update_admin_client_price_est(params, response):
    obj = tcf_client_dashboard()
    obj.update_admin_client_price_est(params, response)

# invoice func
def tcf_navigate_to_admin_client_invoice(params, response):
    obj = tcf_client_dashboard()
    obj.navigate_to_admin_client_invoice(params, response)

def tcf_add_admin_client_invoice(params, response):
    obj_invoice = tcf_client_dashboard()
    obj_invoice.add_admin_client_invoice(params, response)

def tcf_edit_client_invoice_details(params, response):
    obj = tcf_client_dashboard()
    obj.edit_client_invoice_details(params, response)

def tcf_client_invoice_paid(params, response):
    obj = tcf_client_dashboard()
    obj.client_invoice_paid(params, response)

class tcf_client_dashboard():

# dashboard test case function
    def navigate_admin_client_dashboard(self, params, response):
        driver = params['driver']
        obj_dashboard = pg_admin_client_dashboard(driver)
        obj_dashboard.navigate_admin_client_dashboard(params, response)

    def view_n_send_client_msg(self, params, response):
        driver = params['driver']
        obj_client = pg_admin_client_dashboard(driver)
        obj_client.navigate_admin_client_dashboard(params, response)
        obj_client.open_client_msgs(params, response)

        for client_msg in params['client_msg']:
            params['clientMessageText'] = client_msg
            obj_client.view_and_send_client_msg(params, response)

        obj_client.hide_client_msgs(params, response)

    def view_n_send_team_msg(self, params, response):
        driver = params['driver']
        obj_team = pg_admin_client_dashboard(driver)
        obj_team.navigate_admin_client_dashboard(params, response)
        obj_team.open_team_msgs(params, response)

        for team_msg in params['team_msg']:
            params['teamMessageText'] = team_msg
            obj_team.view_and_send_team_msg(params, response)

        obj_team.hide_team_msgs(params, response)

    def add_client_notes(self, params, response):
        driver = params['driver']
        obj_add = pg_admin_client_dashboard(driver)
        obj_add.update_client_dashboard_notes(params, response)

    def open_todo_task(self, params, response):
        driver = params['driver']
        obj_add = pg_admin_client_dashboard(driver)
        obj_add.open_todo_task(params, response)

    def add_client_todo_task(self, params, response):
        driver = params['driver']
        obj_add = pg_admin_client_dashboard(driver)
        obj_add.add_client_dashboard_todo_task(params, response)

    def complete_client_todo_task(self, params, response):
        driver = params['driver']
        obj = pg_admin_client_dashboard(driver)
        for task_name in params['l_todo_task_names']:
            params['todo_complete'] = str(str(task_name) + '-completed-' + 'checkbox')
            obj.complete_client_todo_task(params, response)

    def hide_todo_task(self, params, response):
        driver = params['driver']
        obj_add = pg_admin_client_dashboard(driver)
        obj_add.hide_todo_task(params, response)

    def navigate_to_client_active_engage(self, params, response):
        driver = params['driver']
        obj_active = pg_admin_client_dashboard(driver)

        l_l_primary_values = list()
        for mgr_name, emp_name  in zip(params['manager_names'], params['employee_names']):
            obj_active.navigate_client_dashboard_active_engage(params, response)
            l_l_primary_values.append([mgr_name, emp_name])

        params1 = dict()
        params1['misc'] = False
        params1['driver'] = params['driver']
        params1['tab_name'] = "personalTab"
        params1['table_id'] = "activeEngagementsTable"
        params1['l_primary_col'] = ["Manager", "Employee"]
        params1['l_l_primary_values'] = l_l_primary_values
        obj_table_validation = table_validation.get_instance()
        ret = obj_table_validation.table_search(params1, response)
        print("Result of active eng: " + str(response['result']))
        print("Result List of active eng: " + str(response['l_result_per_primary_value']))
        return ret

# document test case functions
    def navigate_to_admin_client_doc_tabs(self, params, response):
        driver = params['driver']
        obj = pg_admin_client_doc(driver)
        obj.navigate_to_client_doc(params, response)
        #sl_time_sleep()
        obj.navigate_to_client_doc_tabs(params, response)
        #sl_time_sleep()

    def checking_admin_client_doc_checkboxes(self, params, response):
        driver = params['driver']
        obj = pg_admin_client_doc(driver)

        for file_name in params['l_file_names']:
        # generating checkbox id
            params['file_checkbox'] = params['tax_year'] + '-' + file_name + '-' + params['checkbox_name']
            obj.check_admin_client_doc_checkboxes(params, response)

    def view_admin_client_doc_file(self, params, response):
        driver = params['driver']
        obj_actions = pg_admin_client_doc(driver)
        for file_name in params['l_file_names']:
            params['view_file'] = params['tax_year'] + '-' + file_name + '-' + "viewBtn"
            obj_actions.view_admin_client_doc_file(params, response)   #actions_on_admin_client_doc

    def download_admin_client_doc_file(self, params, response):
        driver = params['driver']
        obj_actions = pg_admin_client_doc(driver)
        for file_name in params['l_file_names']:
            params['downld_file'] = params['tax_year'] + '-' + file_name + '-' + "downloadBtn"
            obj_actions.download_admin_client_doc_file(params, response)

    def delete_admin_client_doc_file(self, params, response):
        driver = params['driver']
        obj_actions = pg_admin_client_doc(driver)
        for file_name in params['l_file_names']:
            params['del_file'] = params['tax_year'] + '-' + file_name + '-' + "deleteBtn"
            obj_actions.delete_admin_client_doc_file(params, response)

    def client_file_upload(self, params, response):
        if len(params['file_details']) == 0:
            response['result'] = True
            return True
        driver = params['driver']
        # Navigate to the client upload option
        obj = pg_admin_client_doc(driver)
        obj.navigate_to_client_doc(params, response)
        obj.click_client_add_files_btn(params, response)

        # Populate the client file upload details
        obj.populate_client_file_upload_dtls(params, response)

        # Upload the files and prepare the list for verification
        l_l_primary_values = list()
        l_l_misc_values = list()

        # file_details - file_path, file_name, file_year, file_type
        for count, file_details in enumerate(params['file_details'], start = 1):
            file_details['documentType'] = 'documentType' + str(count)
            file_details['chooseFileBtn'] = 'chooseFileBtn' + str(count)
            obj.client_add_files(file_details, response)
            if(params['tab_name']) == "personalTab":
                l_l_primary_values.append([int(params['tax_year']), file_details['file_name']])
            else:
                l_l_primary_values.append([int(params['tax_year']), params['bns_name'], file_details['file_name']])

            l_l_misc_values.append([file_details['file_type']])
            if len(params['file_details']) > 1 and count != len(params['file_details']):
                obj.add_new_doc()


        obj.client_upload_files(params, response)
        # Perform the table validation of the files
        params['misc'] = True

        if params['tab_name'] == "personalTab":
            params['l_primary_col'] = ["Year", "File Name"]
            params['l_misc_col'] = ["File Type"]
            params['table_id'] = "personal_fromClient"

        elif params['tab_name'] == "businessTab":
            params['l_primary_col'] = ["Year", "Business", "File Name"]
            params['l_misc_col'] = ["File Type"]
            params['table_id'] = "business_fromClient"
        else:
            print("Invalid Category")
            return False

        params['l_l_primary_values'] = l_l_primary_values
        params['l_l_misc_values'] = l_l_misc_values

        tcf_navigate_admin_client_doc_tabs(params, response)

        obj_table_validation = table_validation.get_instance()
        ret = obj_table_validation.table_search(params, response)
        print("Result of upload table : " + str(response['result']))
        print("Result List of upload  table : " + str(response['l_result_per_primary_value']))
        return ret

# status test case functionsutt

    def update_admin_client_status(self, params, response):
        driver = params['driver']
        obj = pg_admin_client_status(driver)
        obj.navigate_admin_client_status(params, response)

        l_l_primary_values = list()
        l_l_misc_values = list()
        if params['tab_name'] == "personalTab":
        # navigate to personal tab
            obj.navigate_to_admin_client_status_tabs(params, response)

            for st_val, year in zip(params['l_l_status_values'], params['l_years']):
                st_val['status_dropdown'] = str(year) + '-' + 'status'
                st_val['upload_complete_check'] = str(year) + '-' + "uploadCmp" + '-' + "checkbox"
                st_val['extension_checkbox'] = str(year) + '-' + "onExt" + '-' + "checkbox"
                obj.update_admin_client_status(st_val, response)
                l_l_primary_values.append([year])
                l_l_misc_values.append([st_val['manager_names'], st_val['employee_names'], st_val['status_name']])

        elif params['tab_name'] == "businessTab":
        # navigate to business tab
            obj.navigate_to_admin_client_status_tabs(params, response)

            for st_val, year, bns in zip(params['l_l_status_values'], params['l_years'], params['l_business']):
                st_val['status_dropdown'] = str(year) + '-' +  bns + '-' + 'status'
                st_val['upload_complete_check'] = str(year) + '-' + "uploadCmp" + '-' + "checkbox"
                st_val['extension_checkbox'] = str(year) + '-' + "onExt" + '-' + "checkbox"
                obj.update_admin_client_status(st_val, response)
                l_l_primary_values.append([year, bns])
                l_l_misc_values.append([st_val['manager_names'], st_val['employee_names'], st_val['status_name']])

        obj.clicking_on_admin_client_status_update(params, response)

        params1 = dict()
        params1['misc'] = True
        params1['driver'] = params['driver']

        if params['tab_name'] == "personalTab":
            params1['l_primary_col'] = ["Year"]
            params1['l_misc_col'] = ["Manager", "Employee", "Status"]
            params1['table_id'] = "clientStatusTable"

        elif params['tab_name'] == "businessTab":
            params1['l_primary_col'] = ["Year", "Business",]
            params1['l_misc_col'] = ["Manager", "Employee", "Status"]
            params1['table_id'] = "clientStatusTableBns"

        else:
            print("Invalid Category")
            return False

        params1['l_l_primary_values'] = l_l_primary_values
        params1['l_l_misc_values'] = l_l_misc_values
        obj_table_validation = table_validation.get_instance()
        ret = obj_table_validation.table_search(params1, response)
        print("Result of status table : " + str(response['result']))
        print("Result List of status  table : " + str(response['l_result_per_primary_value']))
        return ret

    def check_admin_client_history_status(self, params, response):
        driver = params['driver']
        obj_check_history = pg_admin_client_status(driver)
        obj_check_history.navigate_admin_client_status(params, response)

        for value in params['l_l_values']:
            obj_check_history.check_admin_client_history(value, response)


# business test case functions
# This navigation for recep login
    def navigate_to_admin_client_business(self, params, response):
        driver = params['driver']
        obj = pg_admin_client_business(driver)
        obj.navigate_admin_client_business(params, response)

    def admin_client_add_business(self, params, response):
        if len(params['l_bns_info']) == 0:
            response['result'] = True
            return True
        driver = params['driver']
        obj = pg_admin_client_business(driver)
        obj.navigate_admin_client_business(params, response)

        l_l_primary_values = list()
        l_l_misc_values = list()
        for bns in params['l_bns_info']:
            obj.client_add_business(bns, response)
            l_l_primary_values.append([bns['bns_name']])
            l_l_misc_values.append([bns['bns_type']])

        params1 = dict()
        params1['misc'] = True
        params1['driver'] = params['driver']
        params1['table_id'] = "businessTable"
        params1['l_primary_col'] = ["Business Name"]
        params1['l_l_primary_values'] = l_l_primary_values
        params1['l_misc_col'] = ["Business Type"]
        params1['l_l_misc_values'] = l_l_misc_values
        obj_table_validation = table_validation.get_instance()
        ret = obj_table_validation.table_search(params1, response)
        print("Result of business table : " + str(response['result']))
        print("Result List of business table : " + str(response['l_result_per_primary_value']))
        return ret

    def client_edit_business(self, params, response):
        driver = params['driver']
        obj = pg_admin_client_business(driver)
        obj.client_edit_business(params, response)

        for value in params['l_bns_val']:
            obj.client_update_business(value, response)

        obj.click_on_client_update_business(params, response)

# price est test case functions
    def navigate_to_admin_client_price_est(self, params, response):
        driver = params['driver']
        obj = pg_admin_client_price_est(driver)
        obj.navigate_admin_client_price_est(params, response)

    def update_admin_client_price_est(self, params, response):
        driver = params['driver']
        obj = pg_admin_client_price_est(driver)
        obj.navigate_admin_client_price_est(params, response)

        l_l_primary_values = list()
        l_l_misc_values = list()
        #sl_time_sleep()
        if params['tab_name'] == "personalTab":
        # navigate to the Personal tab
            obj.navigate_to_client_price_est_tabs(params, response)

        # generating adjustment id
            params['adjust_id'] = str(params['year'] + '-' + 'adjustments')
            params['adjust_value'] = random.randint(200, 400)
            print("total est amount:", params['estimated_pr'])

            total_price = params['estimated_pr'] + params['adjust_value']
            print("total price is:", total_price)
            obj.updating_client_price_est(params, response)
            l_l_primary_values.append([int(params['year']), params['estimated_pr']])
            l_l_misc_values.append([params['adjust_value'], total_price])

        elif params['tab_name'] == "businessTab":
        # navigate to the Business tab
            obj.navigate_to_client_price_est_tabs(params, response)

            # for year, bns in zip(params['l_years'], params['l_bns_names']):
            # generating adjustment id
            params['adjust_id'] = str(params['year'] + '-' + params['bns_name'] + '-' + "adjustments")
            params['adjust_value'] = random.randint(200, 400)

            print("total est amount:", params['estimated_pr'])

            total_price = params['estimated_pr'] + params['adjust_value']
            print("total price is:", total_price)
            obj.updating_client_price_est(params, response)
            l_l_primary_values.append([int(params['year']), params['bns_name'], params['estimated_pr']])
            l_l_misc_values.append([params['adjust_value'], total_price])

        obj.click_on_price_est_update_btn(params, response)

        params1 = dict()
        params1['misc'] = True
        params1['driver'] = params['driver']

        if params['tab_name'] == "personalTab":
            params1['l_primary_col'] = ["Year", "Estimated Price"]
            params1['l_misc_col'] = ["Adjustments", "Total Price"]
            params1['table_id'] = "priceEstTable"

        elif params['tab_name'] == "businessTab":
            params1['l_primary_col'] = ["Year", "Business", "Estimated Price"]
            params1['l_misc_col'] = ["Adjustments", "Total Price"]
            params1['table_id'] = "priceEstTableBns"

        else:
            print("Invalid Category")
            return False

        #sl_time_sleep()
        params1['l_l_primary_values'] = l_l_primary_values
        params1['l_l_misc_values'] = l_l_misc_values
        obj_table_validation = table_validation.get_instance()
        ret = obj_table_validation.table_search(params1, response)
        print("Result of price est table : " + str(response['result']))
        print("Result List of price est table : " + str(response['l_result_per_primary_value']))
        return ret

# invoice test cases functions
    def navigate_to_admin_client_invoice(self, params, response):
        driver = params['driver']
        obj = pg_admin_client_invoice(driver)
        obj.navigate_admin_client_invoice(params, response)

        l_l_primary_values = list()
        l_l_misc_values = list()
        for price in params['l_prices']:
            l_l_primary_values.append([int(price)])
            # l_l_misc_values.append([paid_date])

        params1 = dict()
        params1['misc'] = False
        params1['driver'] = params['driver']
        params1['table_id'] = "clientInvoiceTable"
        params1['l_primary_col'] = ["Price"]
        # params1['l_misc_col'] = ["Paid Date"]
        params1['l_l_primary_values'] = l_l_primary_values
        # params1['l_l_misc_values'] = l_l_misc_values
        obj_table_validation = table_validation.get_instance()
        ret = obj_table_validation.table_search(params1, response)
#        if ret == False:
        print("Result: " + str(response['result']))
        print("Result List: " + str(response['l_result_per_primary_value']))
        return ret

    def add_admin_client_invoice(self, params, response):
        driver = params['driver']
        obj = pg_admin_client_invoice(driver)
        obj.navigate_admin_client_invoice(params, response)
        obj.click_on_client_invoice_btn(params, response)

        number_of_invoices = len(params['l_descs'])
        count = 1
        l_invoice_pr = []
        l_l_primary_values = []
        l_l_misc_values = []
        for desc, qty, price in zip(params['l_descs'], params['l_qtys'], params['l_prices']):
            if number_of_invoices == count:
                params['last_invoice_indicator'] = 'y'
            else:
                params['last_invoice_indicator'] = 'n'

            params['description'] = desc
            params['quantity'] = qty
            params['price'] = price
            params['count'] = count
            count = count + 1
            t_price = int(qty) * int(price)
            obj.client_add_invoice(params, response)
            l_invoice_pr.append(t_price)
            print("l_invoice:", l_invoice_pr)
        obj.click_on_client_add_invoice(params, response)

        total_price = 0
        for pr in l_invoice_pr:
            total_price = total_price + pr
        print("total_price:", total_price)
        l_l_primary_values.append([total_price])
        # l_l_misc_values.append(["Pending"])
        print("l_primary:", l_l_primary_values)

        params1 = dict()
        params1['misc'] = False
        params1['driver'] = params['driver']
        params1['table_id'] = "clientInvoiceTable"
        params1['l_primary_col'] = ["Price"]
        # params1['l_misc_col'] = ['Paid Date']
        params1['l_l_primary_values'] = l_l_primary_values
        # params1['l_l_misc_values'] = l_l_misc_values
        obj_table_validation = table_validation.get_instance()
        ret = obj_table_validation.table_search(params1, response)
        print("Result of invoice table : " + str(response['result']))
        print("Result List of invoice table : " + str(response['l_result_per_primary_value']))
        return ret

    def edit_client_invoice_details(self, params, response):
        driver = params['driver']
        obj = pg_admin_client_invoice(driver)

        for ids in params['l_details']:
            params['details'] = ids + '-' + "showBtn"
        # click on invoice details
            obj.client_invoice_details(params, response)
        # click on edit btn
            obj.click_client_invoice_edit(params, response)
            count = 1
            for desc, qty, price in zip(params['l_descs'], params['l_qtys'], params['l_prices']):

                params['description'] = desc
                params['quantity'] = qty
                params['price'] = price
                params['count'] = count
                count = count + 1
                obj.edit_client_invoice_details(params, response)
            obj.click_on_client_add_invoice(params, response)

    def client_invoice_paid(self, params, response):
        driver = params['driver']
        obj = pg_admin_client_invoice(driver)

        for id in params['l_paid_dates']:
            params['paid_date'] = id + '-' + "paidBtn"
            obj.client_invoice_paid(params, response)

###########################################################################################################

# client login dashboard test cases
    def client_dashboard_click_todo_checkbox(self, params, response):
        driver = params['driver']
        obj_select = pg_client_login_main_dashboard(driver)

        for task_name in params['l_todo_task_names']:
            params['todo_check'] = str(str(task_name) + '-checkbox')
            obj_select.client_dashboard_check_todo_checkbox(params, response)

    def client_dashboard_unclick_todo_checkbox(self, params, response):
        driver = params['driver']
        obj_unselect = pg_client_login_main_dashboard(driver)

        for task_name in params['l_todo_task_names']:
            params['todo_check'] = str(str(task_name) + '-checkbox')
            obj_unselect.client_dashboard_uncheck_todo_checkbox(params, response)

#############################################################################################################

# employee login dashboard test cases
    def navigate_main_dashboard_to_client_dashboard(self, params, response):
        driver = params['driver']
        obj = pg_emp_login_main_dashboard(driver)

        if params['tab_name'] == "personalTab":
            params['emp_nav_link'] = params['client_name'] + '-'  + params['year'] + '-' + "dashboard"
        elif params['tab_name'] == "businessTab":
            params['emp_nav_link'] = params['client_name'] + '-' + params['bns_name'] + '-' + params['year'] + '-' + "dashboard"
        else:
            raise Exception("please provide tab name")
        obj.navigate_from_main_dashboard_to_client_dashboard(params, response)

###############################################################################################################

# recep login dashboard test cases
    def navigate_from_client_list_to_recep_dashboard(self, params, response):
        driver = params['driver']
        obj = pg_recep_login_main_dashboard(driver)
        params['recep_dashboard_link'] = params['client_link'] + '-' + 'dashboard'
        obj.navigate_from_client_list_to_recep_dashboard(params, response)
