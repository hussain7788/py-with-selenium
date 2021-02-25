from pm.test.pages.admin.pg_client_actions import *
from pm.test.test_case_func.common.tcf_client_dashboard import *
from pm.test.pages.common.pg_client_dashboard import *
from pm.test.locators.lc_admin import *
from pm.test.locators.lc_client import *
from pm.test.locators.lc_common import *
from pm.test.selenium_utility.sl_functions import *


# dashboard functions
def tcf_navigate_n_add_client_notes(params, response):
    obj = tcf_admin_client_dashboard()
    obj.navigate_n_add_client_notes(params, response)

def tcf_add_client_todo_task(params, response):
    obj = tcf_admin_client_dashboard()
    obj.add_client_todo_task(params, response)

def tcf_complete_admin_client_todo_task(params, response):
    obj = tcf_admin_client_dashboard()
    obj.complete_admin_client_todo_task(params, response)

def tcf_view_n_send_team_n_client_msgs(params, response):
    obj = tcf_admin_client_dashboard()
    obj.view_n_send_team_n_client_msgs(params, response)

def tcf_navigate_to_client_dashboard_active_engage(params, response):
    obj = tcf_admin_client_dashboard()
    obj.navigate_to_client_dashboard_active_engage(params, response)

# document functions
def tcf_actions_on_client_doc(params, response):
    obj = tcf_admin_client_dashboard()
    obj.actions_on_client_doc(params, response)

# upload functions
def tcf_client_upload_files(params, response):
    obj = tcf_admin_client_dashboard()
    obj.client_upload_files(params, response)

# status functions

def tcf_update_client_status(params, response):
    obj = tcf_admin_client_dashboard()
    obj.update_client_status(params, response)

def tcf_check_client_status_history(params, response):
    obj = tcf_admin_client_dashboard()
    obj.check_client_status_history(params, response)

# business functions
def tcf_navigate_n_add_client_business(params, response):
    obj = tcf_admin_client_dashboard()
    obj.navigate_n_add_client_business(params, response)

def tcf_edit_client_business(params, response):
    obj = tcf_admin_client_dashboard()
    obj.edit_client_business(params, response)

# price est functions
def tcf_update_client_price_est(params, response):
    obj = tcf_admin_client_dashboard()
    obj.update_client_price_est(params, response)

# invoice func
def tcf_add_n_actions_on_client_invoice(params, response):
    obj_invoice = tcf_admin_client_dashboard()
    obj_invoice.add_n_actions_on_client_invoice(params, response)

def tcf_edit_admin_client_invoice_details(params, response):
    obj = tcf_admin_client_dashboard()
    obj.edit_admin_client_invoice_details(params, response)

def tcf_admin_client_invoice_paid(params, response):
    obj = tcf_admin_client_dashboard()
    obj.admin_client_invoice_paid(params, response)

class tcf_admin_client_dashboard(tcf_client_dashboard):

# dashboard test case function
    def navigate_n_add_client_notes(self, params, response):
        super(tcf_admin_client_dashboard, self).navigate_admin_client_dashboard(params, response)
        super(tcf_admin_client_dashboard, self).add_client_notes(params, response)

    def add_client_todo_task(self, params, response):
        super(tcf_admin_client_dashboard, self).add_client_todo_task(params, response)

    def complete_admin_client_todo_task(self, params, response):
        super(tcf_admin_client_dashboard, self).open_todo_task(params, response)
        super(tcf_admin_client_dashboard, self).complete_client_todo_task(params, response)
        super(tcf_admin_client_dashboard, self).hide_todo_task(params, response)

    def view_n_send_team_n_client_msgs(self, params, response):
        super(tcf_admin_client_dashboard, self).view_n_send_client_msg(params, response)
        super(tcf_admin_client_dashboard, self).view_n_send_team_msg(params, response)

    def navigate_to_client_dashboard_active_engage(self, params, response):
        super(tcf_admin_client_dashboard, self).navigate_to_client_active_engage(params, response)

# document test case functions

    def actions_on_client_doc(self, params, response):
        super(tcf_admin_client_dashboard, self).navigate_to_admin_client_doc_tabs(params, response)
        # params['checkbox_name'] = 'AP-checkbox'
        # super(tcf_admin_client_dashboard, self).checking_admin_client_doc_checkboxes(params, response)
        # super(tcf_admin_client_dashboard, self).view_admin_client_doc_file(params, response)
        # super(tcf_admin_client_dashboard, self).download_admin_client_doc_file(params, response)
        # super(tcf_admin_client_dashboard, self).delete_admin_client_doc_file(params, response)

#uplolad functions
    def client_upload_files(self, params, response):
        super(tcf_admin_client_dashboard, self).client_file_upload(params, response)

# status test case functionsutt
    def update_client_status(self, params, response):
        super(tcf_admin_client_dashboard, self).update_admin_client_status(params, response)

    def check_client_status_history(self, params, response):
        super(tcf_admin_client_dashboard, self).check_admin_client_history_status(params, response)

# business test case functions
    def navigate_n_add_client_business(self, params, response):
        super(tcf_admin_client_dashboard, self).admin_client_add_business(params, response)

    def edit_client_business(self, params, response):
        super(tcf_admin_client_dashboard, self).client_edit_business(params, response)

# price est test case functions

    def update_client_price_est(self, params, response):
        super(tcf_admin_client_dashboard, self).update_admin_client_price_est(params, response)

# invoice test cases functions
    def add_n_actions_on_client_invoice(self, params, response):
        super(tcf_admin_client_dashboard, self).add_admin_client_invoice(params, response)

    def edit_admin_client_invoice_details(self, params, response):
        super(tcf_admin_client_dashboard, self).edit_client_invoice_details(params, response)

    def admin_client_invoice_paid(self, params, response):
        super(tcf_admin_client_dashboard, self).client_invoice_paid(params, response)
