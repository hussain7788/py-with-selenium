from pm.test.test_cases.tc_base import *
from pm.test.utils.common_functions import *
from pm.test.test_case_func.admin.tcf_admin_add import *
from pm.test.test_case_func.common.tcf_client_dashboard import *
from pm.test.test_case_func.common.tcf_appointment import *
from pm.test.test_case_func.admin.tcf_client_actions import *
from pm.test.test_case_func.admin.tcf_admin_client_dashboard import *
from pm.test.test_case_func.client.tcf_client_login_dashboard import *
from pm.test.test_case_func.client.tcf_client_update_profile import *
from pm.test.test_case_func.receptionist.tcf_recep_client_dashboard import *

from pm.test.test_case_func.admin.tcf_admin_profile import *
from pm.test.test_case_func.common.tcf_notifications import *

from pm.test.test_case_func.admin.tcf_admin_task import *
from pm.test.test_case_func.employee.tcf_emp_tasks import *
from pm.test.test_case_func.employee.tcf_emp_client_dashboard import *
from pm.test.test_case_func.admin.tcf_admin_add import *
from pm.test.test_case_func.admin.tcf_admin_tickets import *
from pm.test.test_case_func.super_admin.tcf_super_admin_tickets import *
from pm.test.test_case_func.admin.tcf_team_actions import *
from pm.test.test_case_func.admin.tcf_admin_insights_practice import *
from pm.test.test_case_func.admin.tcf_admin_insights_client import *
from pm.test.test_case_func.admin.tcf_admin_insights_growth import *
from pm.test.test_case_func.common.tcf_change_password import *


# data classes import
from pm.test.test_data.test_data_class.test_data_tasks import *
from pm.test.test_data.test_data_class.test_data_admin import *
from pm.test.test_data.test_data_class.test_data_emp import *
from pm.test.test_data.test_data_class.test_data_client import *
from pm.test.test_data.test_data_class.test_data_tickets import *
from pm.test.test_data.test_data_class.test_data_admin_client_dashboard import *
from pm.test.test_data.test_data_class.test_data_appointment import *
from pm.test.test_data.test_data_class.test_data_update_client_profile import *

from pm.test.test_data.test_data_class.test_data_admin_profile import *
from pm.test.test_data.test_data_class.test_data_insights_practice import *
from pm.test.test_data.test_data_class.test_data_insights_client import *
from pm.test.test_data.test_data_class.test_data_insights_growth import *
from pm.test.test_data.test_data_class.test_data_change_password import *


from pm.test.selenium_utility.sl_functions import *
import random
import pdb
import os

class test_transaction():
    key = None #string
    obj = None #obj

    def __init__(self, key, obj):
        self.key = key
        self.obj = obj

    def execute(self, driver):
        params = {}
        response = {}
        params['driver'] = driver
        if self.key == "pm_key_signin":
            params.update(self.obj.get_data_signin())
            obj_common_utils = common_utils(driver)
            obj_common_utils.signin(params, response)
        elif self.key == "pm_key_signout":
            obj_common_utils = common_utils(driver)
            obj_common_utils.signout(params, response)
        elif self.key == "pm_key_add_admin":
            params.update(self.obj.get_data())
            obj_common_utils = common_utils(driver)
            obj_common_utils.register_new_admin(params, response)
            tcf_add_admin(params, response)
        elif self.key == "pm_key_add_client":
            params['l_client'] = []
            for client in self.obj:
                params['l_client'].append(client.get_client_data())
            tcf_admin_add_client(params, response)
            assert(response['result'] == True)
        elif self.key == "pm_key_add_emp":
            params['l_emp_info'] = []
            for emp in self.obj:
                params['l_emp_info'].append(emp.get_data())
            tcf_admin_add_emp(params, response)
            assert(response['result'] == True)
        elif self.key == "pm_key_c_add_bns":
            params['l_bns_info'] = []
            for bns in self.obj.get_c_bns_data():
                params['l_bns_info'].append(bns)
            tcf_navigate_n_add_client_business(params, response)
            assert(response['result'] == True)
        elif self.key == "pm_key_c_upload_files":
            for files in self.obj.get_c_files_data():
                params.update(files.get_data())
                tcf_client_upload_files(params, response)
            assert(response['result'] == True)
        elif self.key == "pm_key_task_action":
            params.update(self.obj.get_data())
            tcf_admin_task_ops(params, response)
            assert(response['result'] == params['assert_result'])
        elif self.key == "pm_key_emp_process_client_docs":
            params.update(self.obj.get_data())
            tcf_navigate_main_dashboard_to_client_dashboard(params, response)
            #sl_time_sleep()
            tcf_navigate_admin_client_doc_tabs(params, response)
            #sl_time_sleep()
            tcf_actions_on_emp_login_doc(params, response)
        elif self.key == "pm_key_mgr_process_client_docs":
            params.update(self.obj.get_data())
            tcf_navigate_main_dashboard_to_client_dashboard(params, response)
            #sl_time_sleep()
            tcf_navigate_admin_client_doc_tabs(params, response)
            #sl_time_sleep()
            tcf_actions_on_mgr_login_doc(params, response)
        elif self.key == "pm_key_admin_process_client_docs":
            params.update(self.obj.get_data())
            tcf_navigate_main_dashboard_to_client_dashboard(params, response)
            #sl_time_sleep()
            tcf_navigate_admin_client_doc_tabs(params, response)
            #sl_time_sleep()
            tcf_actions_on_client_doc(params, response)
    # messages test_transactions
        elif self.key == "pm_key_send_client_msg":
            params.update(self.obj.get_data())
            tcf_view_n_send_client_msg(params, response)
        elif self.key == "pm_key_send_team_msg":
            params.update(self.obj.get_data())
            tcf_view_n_send_team_msg(params, response)

        elif self.key == "pm_key_navigation_to_admin_client":
            params.update(self.obj.get_client_link())
            tcf_navigate_admin_client_page(params, response)
            tcf_navigate_admin_to_client_dashboard(params, response)

        elif self.key == "pm_key_nav_to_client_dashboard":
            params.update(self.obj.get_data())
            tcf_navigate_main_dashboard_to_client_dashboard(params, response)
 # ticket
    # Add ticket
        elif self.key == "pm_key_add_ticket":
            tcf_admin_profile_support_tickets(params, response)
            params.update(self.obj.get_data())
            tcf_admin_add_tickets(params, response)
    # super_admin reply to Ticket
        elif self.key == "pm_key_super_admin_ticket_reply":
            tcf_super_admin_profile_support_tickets(params, response)
            params.update(self.obj.get_data())
            tcf_super_admin_ticket_reply(params, response)
    # CPA reply to ticket
        elif self.key == "pm_key_admin_ticket_reply":
            tcf_admin_profile_support_tickets(params, response)
            #sl_time_sleep()
            params.update(self.obj.get_data())
            tcf_admin_ticket_reply(params, response)
    # CPA Close ticket
        elif self.key == "pm_key_close_ticket":
            params.update(self.obj.get_data())
            tcf_admin_ticket_close(params, response)
    # super_admin closed ticket validation
        elif self.key == "pm_key_super_admin_close_ticket_validation":
            params.update(self.obj.get_data())
            tcf_super_admin_close_tab_table_validate(params, response)
    # admin team actions
        elif self.key == "pm_key_admin_team_actions":
            params.update(self.obj.get_data())
            tcf_admin_perform_team_action(params, response)
            if params['action'] == 'deleteBtn':
                assert(response['result'] == False)
            else:
                assert(response['result'] == True)
    # admin Client actions
        elif self.key == "pm_key_admin_client_actions":
            params.update(self.obj.get_data())
            tcf_admin_perform_client_action(params, response)
            if params['action'] == 'deleteBtn':
                assert(response['result'] == False)
            else:
                assert(response['result'] == True)
    # Validation of Deactivated User by checking can user Sign In
        elif self.key == "pm_key_can_user_login":
            obj_common_utils = common_utils(driver)
            try:
                obj_common_utils.signout(params, response)
            except:
                assert True
            else:
                assert False
    # Validation of activated User by checking can user Sign Out
        elif self.key == "pm_key_can_user_logout":
            obj_common_utils = common_utils(driver)
            try:
                obj_common_utils.signout(params, response)
            except:
                assert False
            else:
                assert True
# admin client dashboard
    #  navigate admin client dashboard
        elif self.key == "pm_key_navigate_admin_client_dashboard":
            tcf_navigate_admin_client_dashboard(params, response)
    # add notes
        elif self.key == "pm_key_admin_client_notes":
            params.update(self.obj.get_data_notes_and_todotask())
            tcf_navigate_n_add_client_notes(params, response)
    # add todo
        elif self.key == "pm_key_admin_client_todo_task":
            params.update(self.obj.get_data_notes_and_todotask())
            tcf_add_client_todo_task(params, response)
    # complete todo task
        elif self.key == "pm_key_admin_client_todo_complt":
            params.update(self.obj.get_todo_checkbox_data())
            tcf_complete_admin_client_todo_task(params, response)
    # check active eng
        elif self.key == "pm_key_admin_client_active_eng":
            params.update(self.obj.get_data_active_engage())
            tcf_navigate_to_client_dashboard_active_engage(params, response)
    # actions on client doc files
        elif self.key == "pm_key_actions_on_admin_client_doc":
            params.update(self.obj.get_data())
            tcf_actions_on_client_doc(params, response)
        # check client checkboxes
        elif self.key == "pm_key_check_admin_client_checkboxes":
            params['checkbox_name'] = "AP-checkbox"
            params.update(self.obj.get_data())
            tcf_navigate_admin_client_doc_tabs(params, response)
            tcf_checking_admin_client_doc_checkboxes(params, response)
        # view file
        elif self.key == "pm_key_view_client_file":
            params.update(self.obj.get_data())
            tcf_view_admin_client_doc_file(params, response)
        # download file
        elif self.key == "pm_key_download_client_file":
            params.update(self.obj.get_data())
            tcf_download_admin_client_doc_file(params, response)
        # delete file
        elif self.key == "pm_key_delete_client_file":
            params.update(self.obj.get_data())
            tcf_delete_admin_client_doc_file(params, response)

    # upload files
        elif self.key == "pm_key_admin_client_upload_files":
            params.update(self.obj.get_data())
            tcf_client_upload_files(params, response)
    # add business
        elif self.key == "pm_key_admin_client_add_bns":
            params['l_bns_info'] = []
            for bns in self.obj.get_bns_data():
                params['l_bns_info'].append(bns)
            tcf_navigate_n_add_client_business(params, response)
    # update status
        elif self.key == "pm_key_admin_client_update_status":
            params.update(self.obj.get_data())
            tcf_update_client_status(params, response)
            assert(response['result'] == True)
    # update price est
        elif self.key == "pm_key_admin_client_update_price_est":
            params.update(self.obj.get_data())
            tcf_update_client_price_est(params, response)
            assert(response['result'] == True)
    # client invoice
        elif self.key == "pm_key_admin_client_invoice":
            params.update(self.obj.get_data())
            tcf_add_n_actions_on_client_invoice(params, response)
            assert(response['result'] == True)
        # edit invoice details
        elif self.key == "pm_key_edit_admin_client_invoice_details":
            params.update(self.obj.get_data())
            tcf_edit_admin_client_invoice_details(params, response)
        # paid date details
        elif self.key == "pm_key_admin_client_invoice_paid":
            params.update(self.obj.get_data())
            tcf_admin_client_invoice_paid(params, response)

# emp client dashboard doc
        elif self.key == "pm_key_actions_on_emp_doc":
            params.update(self.obj.get_data())
            tcf_actions_on_emp_login_doc(params, response)
        # check client checkboxes
        elif self.key == "pm_key_check_emp_doc_checkboxes":
            params['checkbox_name'] = "EP-checkbox"
            params.update(self.obj.get_data())
            tcf_navigate_admin_client_doc_tabs(params, response)
            tcf_checking_admin_client_doc_checkboxes(params, response)
# mgr client dashboard doc
        elif self.key == "pm_key_actions_on_mgr_doc":
            params.update(self.obj.get_data())
            tcf_actions_on_mgr_login_doc(params, response)
        # check client checkboxes
        elif self.key == "pm_key_check_mgr_doc_checkboxes":
            params['checkbox_name'] = "MP-checkbox"
            params.update(self.obj.get_data())
            tcf_navigate_admin_client_doc_tabs(params, response)
            tcf_checking_admin_client_doc_checkboxes(params, response)

# client login dashboard
    # check todo checkboxes
        elif self.key == "pm_key_client_dashboard_check_todo":
            params.update(self.obj.get_todo_checkbox_data())
            tcf_client_dashboard_check_todo_checkbox(params, response)
    # uncheck todo checkboxes
        elif self.key == "pm_key_client_dashboard_uncheck_todo":
            params.update(self.obj.get_todo_checkbox_data())
            tcf_client_dashboard_uncheck_todo_checkbox(params, response)
    # client doc actions
        elif self.key == "pm_key_client_dashboard_doc_actions":
            params.update(self.obj.get_data())
            tcf_navigate_n_actions_on_client_doc(params, response)
    # client invoice
        elif self.key == "pm_key_client_dashboard_invoice":
            params.update(self.obj.get_data())
            tcf_navigate_n_actions_on_client_invoice(params, response)
            assert(response['result'] == True)

# recep login dashboard
    # nav to client dashboard
        elif self.key == "pm_key_nav_from_recep_to_client_dashboard":
            params.update(self.obj.get_client_link())
            tcf_navigate_from_client_list_to_recep_dashboard(params, response)

# admin Insights
    # Practice
        elif self.key == "pm_key_insight_practice":
            params.update(self.obj.get_data())
            tcf_insight_practice(params, response)
            assert(response['result'] == True)

    # Client
        elif self.key == "pm_key_insight_client":
            params.update(self.obj.get_data())
            tcf_insight_client(params, response)
            assert(response['result'] == True)

    # Growth
        elif self.key == "pm_key_insight_growth":
            params.update(self.obj.get_data())
            tcf_insight_growth(params, response)
            assert(response['result'] == True)

# admin profile settings
    # navigate to admin profile  and change due date settings
        elif self.key == "pm_key_navigate_to_admin_profile":
            tcf_navigate_admin_profile_settings_page(params, response)
        elif self.key == "pm_key_admin_profile_due_date":
            params.update(self.obj.get_due_date_data())
            tcf_edit_admin_profile_global_due_settings(params, response)
    # check access settings
        elif self.key == "pm_key_admin_profile_check_access_settings":
            params.update(self.obj.get_access_settings_data())
            tcf_check_admin_profile_access_settings(params, response)
    # uncheck access settings
        elif self.key == "pm_key_admin_profile_uncheck_access_settings":
            params.update(self.obj.get_access_settings_data())
            tcf_uncheck_admin_profile_access_settings(params, response)
    # change price calculation
        elif self.key == "pm_key_admin_profile_price_cal":
            params.update(self.obj.get_price_cal_data())
            tcf_update_admin_profile_price_calculation(params, response)
    # change email trigger settings
        elif self.key == "pm_key_admin_profile_email_tr":
            params.update(self.obj.get_email_tr_data())
            tcf_edit_admin_profile_email_trigger_settings(params, response)
    # add template
        elif self.key == "pm_key_admin_profile_add_template":
            params.update(self.obj.get_template_data())
            tcf_uploading_admin_profile_templates(params, response)

# notifications
    # check notification count
        elif self.key == "pm_key_check_notification_count":
            params.update(self.obj.get_notifi_data())
            tcf_check_notification_counts(params, response)
            assert(response['result'] == True)
    # check notification messages count
        elif self.key == "pm_key_check_notification_msgs_count":
            params.update(self.obj.get_notifi_data())
            tcf_check_notification_msgs_count(params, response)
            assert(response['result'] == True)

# e2e tests for admin profile settings(access settings)
        elif self.key == "pm_key_validate_id":
            params.update(self.obj.get_id())
            tcf_validate_ids(params, response)
            assert(response['result'] == True)

        elif self.key == "pm_key_appointment":
            params.update(self.obj.get_data())
            tcf_add_appointment(params, response)
            assert(response['result'] == params['assert_result'])

        elif self.key == "pm_key_update_client_profile":
            params.update(self.obj.get_data())
            tcf_update_client_profile(params, response)

# Run this OS command to generate the Auto To Do
        elif self.key == "pm_key_auto_todo":
            os.system("python ~/django_cpa_pm/cpa_pm/manage.py auto_todo")

        elif self.key == "pm_key_change_password":
            params.update(self.obj.get_data())
            tcf_reset_password(params, response)
        else:
            raise Exception("Not a valid keyword transaction")

def execute_transactions(l_transactions, driver):
    for transaction in l_transactions:
        transaction.execute(driver)
        #sl_time_sleep()
