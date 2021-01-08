
from pm.test.test_data.test_data_class.test_data_admin_client_dashboard import *
from pm.test.test_data.test_data_class.test_data_client import *
from pm.test.test_data.test_data_class.test_data_admin import *
from pm.test.test_data.test_data_class.test_data_emp import *
from pm.test.test_data.test_transactions import *
from pm.test.test_cases.tc_base import *
from pm.test.test_case_func.admin.tcf_client_actions import *
from pm.test.test_case_func.admin.tcf_admin_client_dashboard import *
import random

l_transactions = []
l_d_users = []


num_bns = 2 # per client
num_files = 2 # +1 per client (personal) and per business


d_users = {
    'l_d_admin': [],
    'l_d_doc' : [],
    'l_d_bns' : [],
    'l_d_upload' :[],
    'l_d_client_msgs' : [],
    'd_emp_links' : [],
    'd_client_links' : [],
    'l_d_status' : [],
    'l_d_price_est' : [],
    'l_invoice' : [],
    'l_d_client_doc_actions' : [],
    'l_d_active_engage' : [],
    'l_d_notes_todotask' : [],
    'l_d_clients' : [],
}

def data_add_business():
    for bns_num in range(1, num_bns + 1, 1):
        bns_name = "furniture" + str(bns_num)
        bns_type = "LLP"
        bns_inc_state = "CA"
        bns_inc_date = "01012020"
        bk_frequency = "Monthly"
        pr_frequency = "Bi-Monthly"
        st_frequency = "Quarterly"
        tp_checkbox = True
        tp_frequency = "Yearly"
        bns_obj = test_data_business(bns_name, bns_type, bns_inc_state, bns_inc_date,
                                        bk_frequency, pr_frequency, st_frequency, tp_checkbox, tp_frequency)
        d_users['l_d_bns'].append(bns_obj)


def data_admin():
    admin_data_obj = test_data_admin(email = "sarah.walker@cpa.com", password = "123",)
    d_users['l_d_admin'].append(admin_data_obj)

def data_nav_client():
    #1
    client_obj1 = test_data_client(email = '0_client_8.last@client.com')	#0_client_9.last@client.com
    d_users['d_client_links'].append(client_obj1)

# upload files
def data_upload_files():
    file_1 = test_data_file(file_name='per_w2_1.pdf', file_type='Tax Return')
    file_2 = test_data_file(file_name='per_w2_2.pdf', file_type='Tax Return')
    file_3 = test_data_file(file_name='per_w2_3.pdf', file_type='Tax Return')
    file_obj1 = test_data_upload_files(tab_name="personalTab", sub_tab="fromClient", client_login_access= False,
                                tax_year="2018", document_source = "Received From Client", bns_name = None,
                                l_files = [file_1,file_2, file_3])
    d_users['l_d_upload'].append(file_obj1)

    file_4 = test_data_file(file_name='01bns_w2_1.pdf', file_type='Tax Return')
    file_5 = test_data_file(file_name='01bns_w2_2.pdf', file_type='Tax Return')
    file_obj2 = test_data_upload_files(tab_name="businessTab", sub_tab="fromClient", client_login_access = False,
                                tax_year= "2020", bns_name = "bns1", document_source="Received From Client",
                                l_files = [file_4, file_5])
    d_users['l_d_upload'].append(file_obj2)

def data_messages():
    msg_obj1 = test_data_msgs(client_msg = ['client Message 1', 'client Message 2'])
    d_users['l_d_client_msgs'].append(msg_obj1)
    msg_obj2 = test_data_msgs(team_msg= ['team Message 1', 'team Message 2'])
    d_users['l_d_client_msgs'].append(msg_obj2)

def data_status():
    st_val1 = test_data_status_values(emp_status_access = False, manager_dropdown='mgr-42', manager_names='m1 lname',
                            employee_dropdown='emp-42', employee_names='e1 lname', status_name='In Progress',)

    # st_val2 = test_data_status_values(emp_status_access = False, manager_dropdown='mgr-55', manager_names='Sarah Walker', employee_dropdown='emp-14', employee_names='John Casey',
    #                                     status_dropdown='2017-status', status_name='In Progress',)
    #
    # st_val3 = test_data_status_values(emp_status_access = False, manager_dropdown='mgr-15', manager_names='John Casey', employee_dropdown='emp-15', employee_names='Kevin Durant',
    #                                     status_dropdown='2018-status', status_name='In Progress',)

    status_obj1 = test_data_status(tab_name='personalTab', l_mgr_names= ['m1 lname',],
                                    l_emp_names=['e1 lname'], l_years=[2019],
                                    l_d_status= [st_val1])
    d_users['l_d_status'].append(status_obj1)

    st_val4 = test_data_status_values(emp_status_access = False, manager_dropdown='mgr-43', manager_names='m1 lname',
                                    employee_dropdown='emp-43', employee_names='e2 lname', status_name='In Progress',)

    status_obj2 = test_data_status(tab_name='businessTab', l_mgr_names= ['m1 lname'], l_business=['furniture2'],
                                    l_emp_names=['e2 lname'], l_years=[2019],
                                    l_d_status= [st_val4])
    d_users['l_d_status'].append(status_obj2)

def data_price_est():
    price_obj1 = test_data_price_est(tab_name= 'personalTab', year='2019', estimated_pr=0,)
    d_users['l_d_price_est'].append(price_obj1)

    price_obj2 = test_data_price_est(tab_name= 'businessTab', year='2019', bns_name='furniture2', estimated_pr=0)
    d_users['l_d_price_est'].append(price_obj2)

def data_invoice():
    # add invoice
    invoice_obj1 = test_data_invoice(l_descs=['desc 1', 'desc 2', 'desc 3'],l_qtys=['1', '1', '1'], l_prices=['1', '2', '3'],)
    d_users['l_invoice'].append(invoice_obj1)
    # edit details
    invoice_obj2 = test_data_invoice(l_details=["26"], l_descs=['desc 1', 'desc 2',  'desc 3'],
                                    l_qtys=['1', '2', '3'], l_prices=['10', '10', '10'],)
    d_users['l_invoice'].append(invoice_obj2)
    # paid date
    invoice_obj3 = test_data_invoice(l_paid_dates= ['26'])
    d_users['l_invoice'].append(invoice_obj3)

def data_doc_actions():

    doc_obj1=test_data_doc_actions(tab_name = "personalTab",
                                    sub_tab = "fromClient",
                                    tax_year = "2019",
                                    l_file_names = ["file_1.pdf", "file_2.pdf"],
                                    )
    d_users['l_d_client_doc_actions'].append(doc_obj1)

    doc_obj2=test_data_doc_actions(tab_name = "businessTab",
                                    sub_tab = "fromClient",
                                    tax_year = "2019",
                                    l_file_names = ["file_1.pdf", "file_2.pdf"],
                                    )
    d_users['l_d_client_doc_actions'].append(doc_obj2)

def data_active_eng():
    active_eng_obj = test_data_admin_client_dashboard(
                                                        tab_name = "personalTab",
                                                        l_manager_names = ['Morgan Grimes'],
                                                        l_employee_names = ['Kyrie Irving']
                                                        )
    d_users['l_d_active_engage'].append(active_eng_obj)

def data_add_todo_task():
    todo_task_obj = test_data_admin_client_dashboard(
                                                        notes = "Some Notes Here..",
                                                        todoDueDate = "08012020",
                                                        todoTask = "task1",
                                                        )
    d_users['l_d_notes_todotask'].append(todo_task_obj)

    todo_task_obj2 = test_data_admin_client_dashboard(l_todo_task_names = ['task1'])
    d_users['l_d_notes_todotask'].append(todo_task_obj2)


def data_admin_client():
    data_status()
    data_price_est()
    data_invoice()
    data_doc_actions()
    data_active_eng()
    data_add_todo_task()
    data_admin()
    data_messages()
    data_add_business()
    data_upload_files()
    data_nav_client()

@pytest.mark.test_all
@pytest.mark.test_admin_client_dashboard
class Test_admin_client_dashboard(base_test_case):
    def test_1_setup(self):
        super(Test_admin_client_dashboard, self).get_driver()
        data_admin_client()
        driver = self.driver
    # admin3 sign in
        obj_transaction = test_transaction('pm_key_signin', d_users['l_d_admin'][0])
        l_transactions.append(obj_transaction)

    # navigate to admin client dashboard
        obj_transaction = test_transaction('pm_key_navigation_to_admin_client', d_users['d_client_links'][0])
        l_transactions.append(obj_transaction)

    # # add notes
    #     obj_transaction = test_transaction('pm_key_admin_client_notes', d_users['l_d_notes_todotask'][0])
    #     l_transactions.append(obj_transaction)
    #
    # # open todo tasks
    #     obj_transaction = test_transaction('pm_key_open_todo_task', None)
    #     l_transactions.append(obj_transaction)
    #
    # # add  todo tasks
    #     obj_transaction = test_transaction('pm_key_admin_client_todo_task', d_users['l_d_notes_todotask'][0])
    #     l_transactions.append(obj_transaction)
    # # hide todo tasks
    #     obj_transaction = test_transaction('pm_key_hide_todo_task', None)
    #     l_transactions.append(obj_transaction)
    #
    # # send client msg
    #     obj_transaction = test_transaction('pm_key_send_client_msg', d_users['l_d_client_msgs'][0])
    #     l_transactions.append(obj_transaction)
    #
    # # send team msg
    #     obj_transaction = test_transaction('pm_key_send_team_msg', d_users['l_d_client_msgs'][1])
    #     l_transactions.append(obj_transaction)

    # # add bns
    #     for bns in d_users['l_d_bns']:
    #         obj_transaction = test_transaction('pm_key_admin_client_add_bns', bns)
    #         l_transactions.append(obj_transaction)

    #
    # # doc actions personal tab
    #     obj_transaction = test_transaction('pm_key_actions_on_admin_client_doc', d_users['l_d_client_doc_actions'][0])
    #     l_transactions.append(obj_transaction)

    # # doc actions business tab
    #     obj_transaction = test_transaction('pm_key_actions_on_admin_client_doc', d_users['l_d_client_doc_actions'][1])
    #     l_transactions.append(obj_transaction)

    # # upload personal files
    #     obj_transaction = test_transaction('pm_key_admin_client_upload_files', d_users['l_d_upload'][0])
    #     l_transactions.append(obj_transaction)
    # upload business files
        obj_transaction = test_transaction('pm_key_admin_client_upload_files', d_users['l_d_upload'][1])
        l_transactions.append(obj_transaction)



    # # # update personal status
    # #     obj_transaction = test_transaction('pm_key_admin_client_update_status', d_users['l_d_status'][0])
    # #     l_transactions.append(obj_transaction)
    # # # update business status
    # #     obj_transaction = test_transaction('pm_key_admin_client_update_status', d_users['l_d_status'][1])
    # #     l_transactions.append(obj_transaction)
    #

    # # update personal price est
    #     obj_transaction = test_transaction('pm_key_admin_client_update_price_est', d_users['l_d_price_est'][0])
    #     l_transactions.append(obj_transaction)
    # # update business price est
    #     obj_transaction = test_transaction('pm_key_admin_client_update_price_est', d_users['l_d_price_est'][1])
    #     l_transactions.append(obj_transaction)
    #
    # # invoice
    #     obj_transaction = test_transaction('pm_key_admin_client_invoice', d_users['l_invoice'][0])
    #     l_transactions.append(obj_transaction)
    #
    #     obj_transaction = test_transaction('pm_key_edit_admin_client_invoice_details', d_users['l_invoice'][1])
    #     l_transactions.append(obj_transaction)
    #
    #     obj_transaction = test_transaction('pm_key_admin_client_invoice_paid', d_users['l_invoice'][2])
    #     l_transactions.append(obj_transaction)

    # execute transactions
        execute_transactions(l_transactions, driver)

    def test_2_destroy_instance(self):
        super(Test_admin_client_dashboard, self).destroy_driver()
        tc_post_process()

# @pytest.mark.test_all
# @pytest.mark.test_admin_client_dashboard
# class Test_admin_client_dashboard(base_test_case):
#     def test_1_setup(self):
#         super(Test_admin_client_dashboard, self).get_driver()
#         obj_common_utils = common_utils(self.driver)
#         params = dict()
#         response = dict()
#         params['user_name'] = "sarah.walker@cpa.com"
#         params['password'] = "123"
#         obj_common_utils.signin(params, response)
#         tc_post_process()
#
#     def test_2_navigate_admin_client_page(self):
#         super(Test_admin_client_dashboard, self).get_driver()
#         params = dict()
#         response = dict()
#         params['driver'] = self.driver
#         params['tab_name'] = "activeTab"
#         tcf_navigate_admin_client_page(params, response)
#         tc_post_process()
#         assert True
#
#     def test_3_navigate_admin_to_client_dashboard(self):
#         super(Test_admin_client_dashboard, self).get_driver()
#         params = dict()
#         response = dict()
#         params['driver'] = self.driver
#         client_email_id1 = "percy.jackson@client.com"
#         client_email_id2= "annabeth.chase@client.com"
#         client_email_id3 = "hazel.levesque@client.com"
#         params['client_link'] = client_email_id3
#         tcf_navigate_admin_to_client_dashboard(params, response)
#         tc_post_process()

    # def test_4_navigate_n_add_client_notes_n_todo_task(self):
    #     super(Test_admin_client_dashboard, self).get_driver()
    #     tc_pre_process()
    #     params = dict()
    #     response = dict()
    #     params['driver'] = self.driver
    #     params['notes'] = "Some Notes Here.."
    #     params['todoDueDate'] = "08012020"
    #     params['todoTask'] = "Add New Task Here.."
    #     tcf_navigate_n_add_client_notes_n_todo_task(params, response)
    #     tc_post_process()
    #     assert True
    #
    # def test_5_view_n_send_team_n_client_msgs(self):
    #     super(Test_admin_client_dashboard, self).get_driver()
    #     tc_pre_process()
    #     params = dict()
    #     response = dict()
    #     params['driver'] = self.driver
    #     params['client_msg'] = ['client Message 1', 'client Message 2']
    #     params['team_msg'] = ['team Message 1', 'team Message 2']
    #     tcf_view_n_send_team_n_client_msgs(params, response)
    #     tc_post_process()
    #     assert True
    #
    # def test_6_navigate_to_client_dashboard_active_engage(self):
    #     super(Test_admin_client_dashboard, self).get_driver()
    #     tc_pre_process()
    #     params = dict()
    #     response = dict()
    #     params['driver'] = self.driver
    #     params['tab_name'] = "personalTab"
    #     params['manager_names'] = ['Morgan Grimes', 'Sarah Walker', 'John Casey']
    #     params['employee_names'] = ['Kyrie Irving', 'John Casey', 'Kevin Durant']
    #     tcf_navigate_to_client_dashboard_active_engage(params, response)
    #     tc_post_process()
    #     assert True
    #
    # def test_9_client_upload_personal_files(self):
    #     super(Test_admin_client_dashboard, self).get_driver()
    #     params = dict()
    #     response = dict()
    #     params['driver'] = self.driver
    #     params['tab_name'] = "personalTab"
    #     params['sub_tab'] = "fromClient"
    #     params['client_login_access'] = False
    #     params['tax_year'] = "2019"
    #     params['document_source'] = "Received from Client"
    #
    #     path = '/home/gangah/Downloads/'
    #     l_files = ["file_1.pdf", "file_2.pdf", "file_3.pdf"]
    #     params['file_details'] = list()
    #
    #     for file_name in l_files:
    #         params1 = dict()
    #         params1['file_name'] = file_name
    #         params1['full_file_name'] = str(path + file_name)
    #         # params1['file_year'] = params['tax_year']
    #         params1['file_type'] = "Tax Return"
    #         params['file_details'].append(params1)
    #
    #     tcf_client_upload_files(params, response)
    #     assert(response['result'] == True)
    #
    # def test_10_client_upload_business_files(self):
    #     super(Test_admin_client_dashboard, self).get_driver()
    #     params = dict()
    #     response = dict()
    #     params['driver'] = self.driver
    #     params['tab_name'] = "businessTab"
    #     params['sub_tab'] = "fromClient"
    #     params['client_login_access'] = False
    #     params['tax_year'] = "2019"
    #     params['document_source'] = "Received from Client"
    #     params['bns_name'] = "furniture2"
    #
    #     path = '/home/gangah/Downloads/'
    #     l_files = ["file_1.pdf", "file_2.pdf", "file_3.pdf"]
    #     params['file_details'] = list()
    #
    #     for file_name in l_files:
    #         params1 = dict()
    #         params1['file_name'] = file_name
    #         params1['full_file_name'] = str(path + file_name)
    #         # params1['file_year'] = params['tax_year']
    #         params1['file_type'] = "Tax Return"
    #         params['file_details'].append(params1)
    #
    #     tcf_client_upload_files(params, response)
    #     assert(response['result'] == True)
    #
    # def test_7_actions_on_client_doc_personal_files(self):
    #     super(Test_admin_client_dashboard, self).get_driver()
    #     params = dict()
    #     response = dict()
    #     params['driver'] = self.driver
    #     params['tab_name'] = "personalTab"
    #     params['sub_tab'] = "fromClient"
    #     params['tax_year'] = "2019"
    #     params['l_file_names'] = ["file_1.pdf", "file_2.pdf"]
    #     tcf_actions_on_client_doc(params, response)
    #     tc_post_process()
    #     assert True
    #
    # def test_7_actions_on_client_doc_business_files(self):
    #     super(Test_admin_client_dashboard, self).get_driver()
    #     params = dict()
    #     response = dict()
    #     params['driver'] = self.driver
    #     params['l_l_ids'] = list()
    #     params['tab_name'] = "businessTab"
    #     params['sub_tab'] = "fromClient"
    #     params['tax_year'] = "2019"
    #     params['l_file_names'] = ["file_1.pdf", "file_2.pdf"]
    #     tcf_actions_on_client_doc(params, response)
    #     tc_post_process()
    #     assert True

    # def test_11_update_client_personal_status(self):
    #     super(Test_admin_client_dashboard, self).get_driver()
    #     params = dict()
    #     response = dict()
    #     params['driver'] = self.driver
    #     params['l_l_status_values'] = list()
    #     params['tab_name'] = "personalTab"
    #
    #     params['l_mgr_names'] = ['Morgan Grimes', 'Sarah Walker', 'John Casey']
    #     params['l_emp_names'] = ['Kyrie Irving', 'John Casey', 'Kevin Durant']
    #     params['l_years'] = [2016, 2017, 2018]
    #
    #     for st_num, st_yr, mgr_name, emp_name in zip(range(13, 17), range(6, 10), params['l_mgr_names'], params['l_emp_names']):
    #         params1 = dict()
    #         params1['emp_status_access'] = False
    #         params1['manager_dropdown'] = str("mgr-" + str(st_num))
    #         params1['manager_names'] = mgr_name
    #         params1['employee_dropdown'] = str("emp-" +str(st_num))
    #         params1['employee_names'] = emp_name
    #         params1['status_dropdown'] = str("201" + str(st_yr) + "-status")
    #         params1['status_name'] = "In Progress"
    #         # params1[''] = str("201" + str(st_yr) + "-uploadCmp-checkbox")
    #         # params1['extension_checkbox'] = str("201" + str(st_yr) + "-onExt-checkbox")
    #         params['l_l_status_values'].append(params1)
    #
    #     tcf_update_client_status(params, response)
    #     tc_post_process()
    #     assert(response['result'] == True)

    # def test_12_update_client_business_status(self):
    #     super(Test_admin_client_dashboard, self).get_driver()
    #     params = dict()
    #     response = dict()
    #     params['driver'] = self.driver
    #     params['l_l_status_values'] = list()
    #     params['tab_name'] = "businessTab"
    #
    #     params['l_mgr_names'] = ['Morgan Grimes', 'Sarah Walker']
    #     params['l_emp_names'] = ['Kyrie Irving', 'John Casey']
    #     params['l_years'] = [2019, 2019]
    #     params['l_business'] = ['furniture2', 'furniture1']
    #
    #     for st_num, bns_num, mgr_name, emp_name in zip(range(41, 43), range(1, 3), params['l_mgr_names'], params['l_emp_names']):
    #         params1 = dict()
    #         params1['emp_status_access'] = False
    #         params1['manager_dropdown'] = str("mgr-" + str(st_num))
    #         params1['manager_names'] = mgr_name
    #         params1['employee_dropdown'] = str("emp-" +str(st_num))
    #         params1['employee_names'] = emp_name
    #         params1['status_dropdown'] = str("2019" + "-furniture"  + str(bns_num) + "-status")
    #         params1['status_name'] = "In Progress"
    #         params['l_l_status_values'].append(params1)
    #
    #     tcf_update_client_status(params, response)
    #     tc_post_process()
    #     assert(response['result'] == True)

    # def test_13_check_client_status_history(self):
    #     super(Test_admin_client_dashboard, self).get_driver()
    #     params = dict()
    #     response = dict()
    #     params['driver'] = self.driver
    #     params['l_l_values'] = list()
    #
    #     for hist_num in range(6, 10, 1):
    #         params1 = dict()
    #         params1['history_button'] = str("201" + str(hist_num) + "-historyBtn")
    #         params['l_l_values'].append(params1)
    #     tcf_check_client_status_history(params, response)
    #     tc_post_process()
    #     assert True
    #
    # def test_14_client_add_business(self):
    #     super(Test_admin_client_dashboard, self).get_driver()
    #     tc_pre_process()
    #     params = dict()
    #     response = dict()
    #     params['driver'] = self.driver
    #     params['l_bns_info'] = list()
    #
    #     l_bns_type = ['LLP', 'Sole-Prop']
    #
    #     for business, bns_type  in zip(range(1, 3), l_bns_type):
    #         params1 = dict()
    #         params1['business_name'] = str("furniture" + str(business))
    #         params1['business_type'] = bns_type
    #         params1['bns_inc_state'] = "AR"
    #         params1['bns_inc_date'] = "08012020"
    #         params1['bk_checkbox'] = False
    #         params1['pr_checkbox'] = False
    #         params1['st_checkbox'] = False
    #         params1['tp_checkbox'] = True
    #         params1['bk_frequency'] = "Monthly"
    #         params1['pr_frequency'] = "Quarterly"
    #         params1['st_frequency'] = "Yearly"
    #         params['l_bns_info'].append(params1)
    #
    #     tcf_navigate_n_add_client_business(params, response)
    #     tc_post_process()
    #     assert(response['result'] == True)
    #
    #
    # def test_16_client_edit_business(self):
    #     super(Test_admin_client_dashboard, self).get_driver()
    #     params = dict()
    #     response = dict()
    #     params['driver'] = self.driver
    #     params['l_bns_val'] = list()
    #
    #     for val in range(1, 2):
    #         params1 = dict()
    #         params1['bk_frequency'] = "bkDropdown"
    #         params1['bk_frequency_value'] = "Monthly"
    #         params1['pr_frequency'] = "prDropdown"
    #         params1['pr_frequency_value'] = "Yearly"
    #         params1['st_frequency'] = "stDropdown"
    #         params1['st_frequency_value'] = "Quarterly"
    #         params1['tp_frequency'] = "tpDropdown"
    #         params1['tp_frequency_value'] = "Yearly"
    #         params['l_bns_val'].append(params1)
    #
    #     tcf_client_edit_business(params, response)
    #     tc_post_process()
    #     assert True

    # def test_17_updating_client_personal_price_adj(self):
    #     super(Test_admin_client_dashboard, self).get_driver()
    #     params = dict()
    #     response = dict()
    #     params['driver'] = self.driver
    #     params['tab_name'] = "personalTab"
    #     params['l_years'] = ['2016', '2017', '2018', '2019']
    #     tcf_update_client_price_est(params, response)
    #     tc_post_process()
    #     assert(response['result'] == True)
    #
    # def test_18_updating_client_business_price_adj(self):
    #     super(Test_admin_client_dashboard, self).get_driver()
    #     params = dict()
    #     response = dict()
    #     params['driver'] = self.driver
    #     params['tab_name'] = "businessTab"
    #     params['l_years'] = ['2019', '2019']
    #     params['l_bns_names'] = ['furniture1', 'furniture2']
    #     tcf_update_client_price_est(params, response)
    #     tc_post_process()
    #     assert(response['result'] == True)
    #
    # def test_19_add_n_actions_on_client_invoice(self):
    #     super(Test_admin_client_dashboard, self).get_driver()
    #     params = dict()
    #     response = dict()
    #     params['driver'] = self.driver
    #     params['l_descs'] = ["desc 1",]
    #     params['l_qtys'] = ['1', ]
    #     params['l_prices'] = ['2',]
    #     tcf_add_n_actions_on_client_invoice(params, response)
    #     tc_post_process()
    #     assert(response['result'] == False)

    # def test_20_edit_admin_client_invoice_details(self):
    #     super(Test_admin_client_dashboard, self).get_driver()
    #     params = dict()
    #     response = dict()
    #     params['driver'] = self.driver
    #     params['l_details'] = ["32",]
    #     params['l_descs'] = ["desc 1", "desc 2"]
    #     params['l_qtys'] = ['1', "2"]
    #     params['l_prices'] = ['10', '10',]
    #     tcf_edit_admin_client_invoice_details(params, response)
    #     tc_post_process()
    #     assert True

    # def test_20_admin_client_invoice_paid(self):
    #     super(Test_admin_client_dashboard, self).get_driver()
    #     params = dict()
    #     response = dict()
    #     params['driver'] = self.driver
    #     params['l_paid_dates'] = ['11', '16']
    #     tcf_admin_client_invoice_paid(params, response)
    #     tc_post_process()
    #     assert True
    #
    # def test_20_destroy_instance(self):
    #     super(Test_admin_client_dashboard, self).destroy_driver()
    #     tc_post_process()
