from pm.test.test_data.test_data_class.test_data_tasks import *
from pm.test.test_data.test_data_class.test_data_admin import *
from pm.test.test_data.test_data_class.test_data_emp import *
from pm.test.test_data.test_data_class.test_data_client import *
from pm.test.selenium_utility.sl_functions import *
import random

l_d_users = []

num_admins = 1
num_clients = 2 # per admin
num_bns = 2 # per client
num_files = 2 # +1 per client (personal) and per business
num_mgrs = 2 # per admin
num_emps = 2 # per mgr

def data_users():

    for admin_num in range(1, num_admins + 1, 1):
        d_users = {
            'd_admin': {},
            'l_d_clients': [],
            'l_d_mgrs': [],
            'l_d_emps': [],
            'l_d_doc': [],
            'l_d_msgs': [],
            'l_d_unassigned_tasks': [],
            'l_d_assigned_tasks': [],
            'l_d_mgr_review_tasks': [],
            'l_d_admin_review_tasks': [],
            'l_d_client_review_tasks': [],
            'l_d_efile_auth_tasks': [],
            'l_d_efiled_tasks': [],
            'l_d_closed_tasks': [],
        }
        create_admin_data(d_users, admin_num)

        for client_num in range(1, num_clients + 1, 1):
            create_client_data(d_users, admin_num, client_num)

        for mgr_num in range(1, num_mgrs + 1, 1):
            create_mgr_data(d_users, admin_num, mgr_num)
            create_unassigned_task_data(d_users, admin_num, mgr_num)
            create_assigned_task_data(d_users, admin_num, mgr_num)

            create_emp_doc_actions(d_users, admin_num, mgr_num)
            create_mgr_review_task_data(d_users, admin_num, mgr_num)

            create_admin_review_task_data(d_users, admin_num, mgr_num)
        
        create_client_review_task_data(d_users, admin_num)
        create_data_messages(d_users)
        create_efile_auth_task_data(d_users, admin_num)
        create_efiled_task_data(d_users, admin_num)
        create_closed_task_data(d_users, admin_num)
        l_d_users.append(d_users)

def create_admin_data(d_users, admin_num):
    first_name = str("admin" + str(admin_num).zfill(2))
    last_name = "lname"
    company_name = str("CPA Sage " + str(admin_num).zfill(2))
    email = str(first_name + "." + last_name + "@cpa.com")
    phone = "123-456-7890"
    password = "123"
    admin_obj = test_data_admin(first_name, last_name, company_name, email, phone, password)
    d_users['d_admin'] = admin_obj

def create_client_data(d_users, admin_num, client_num):
    first_name = str(str(admin_num).zfill(2) + "_client" + str(client_num).zfill(2))
    last_name = "lname"
    email = str(first_name + "." + last_name + "@client.com")
    phone = "123-456-7890"
    password = "123"
    l_bns = []
    l_file_dtls = []

    for bns_num in range(1, num_bns + 1, 1):
        business_name = str(str(admin_num).zfill(2) + "_" + str(client_num).zfill(2) + "_business" + str(bns_num).zfill(2))
        create_c_bns_data(l_bns, business_name)
        create_c_bns_files(l_file_dtls, business_name, bns_num)

    create_c_per_files(l_file_dtls)

    client_obj = test_data_client(first_name, last_name, email, phone, password, l_bns, l_file_dtls)
    d_users['l_d_clients'].append(client_obj)

def create_c_bns_data(l_bns, business_name):
    business_type = "LLP"
    bns_inc_state = "CA"
    business_inco_date = "01012020"
    bk_frequency = "Monthly"
    pr_frequency = "Bi-Monthly"
    st_frequency = "Quarterly"
    tp_checkbox = True
    bns_obj = test_data_business(business_name, business_type, bns_inc_state, business_inco_date, 
                                    bk_frequency, pr_frequency, st_frequency, tp_checkbox)
    l_bns.append(bns_obj)

def create_c_bns_files(l_file_dtls, business_name, bns_num):
        l_files = []
        for file_num in range(1, num_files + 1, 1):
            file_name = str(str(bns_num).zfill(2) + "bns_w2_" + str(file_num) + ".pdf")
            # file_year = '2019'
            file_type = 'W-2'
            file_obj = test_data_file(file_name, file_type)
            l_files.append(file_obj)
        
        tab_name = "BusinessTab"
        sub_tab = "fromClient"
        client_login_access = True
        tax_year = "2019"
        bns_name = business_name
        document_source = "Received from Client"
        file_dtl_obj = test_data_upload_files(tab_name, sub_tab, client_login_access, tax_year, document_source, bns_name, l_files)
        l_file_dtls.append(file_dtl_obj)

def create_c_per_files(l_file_dtls):
    l_files = []
    for file_num in range(1, num_files + 2, 1):
        file_name = str("per_w2_" + str(file_num) + ".pdf")
        # file_year = '2019'
        file_type = 'W-2'
        file_obj = test_data_file(file_name, file_type)
        l_files.append(file_obj)
    
    tab_name = "PersonalTab"
    sub_tab = "fromClient"
    client_login_access = True
    tax_year = "2019"
    bns_name = None
    document_source = "Received from Client"
    file_dtl_obj = test_data_upload_files(tab_name, sub_tab, client_login_access, tax_year, document_source, bns_name, l_files)
    l_file_dtls.append(file_dtl_obj)

def create_mgr_data(d_users, admin_num, mgr_num):
    mgr_first_name = str(str(admin_num).zfill(2) + "_mgr" + str(mgr_num).zfill(2))
    mgr_last_name = "lname"
    email = str(mgr_first_name + "." + mgr_last_name + "@mgr.com")
    phone = "123-456-7890"
    password = "123"
    emp_type = "Team Manager"
    emp_obj = test_data_emp(mgr_first_name, mgr_last_name, email, phone, password, emp_type, None)
    d_users['l_d_mgrs'].append(emp_obj)

    for emp_num in range(1, num_emps + 1, 1):
        create_emp_data(d_users, admin_num, mgr_num, emp_num, mgr_first_name, mgr_last_name)


def create_emp_data(d_users, admin_num, mgr_num, emp_num, mgr_first_name, mgr_last_name):
    first_name = str(str(admin_num).zfill(2) + "_" + str(mgr_num).zfill(2) + "_emp" + str(emp_num).zfill(2))
    last_name = "lname"
    email = str(first_name + "." + last_name + "@emp.com")
    phone = "123-456-7890"
    password = "123"
    emp_type = "Team Member"
    manager = str(mgr_first_name + " " + mgr_last_name)
    emp_obj = test_data_emp(first_name, last_name, email, phone, password, emp_type, manager)
    d_users['l_d_emps'].append(emp_obj)

def create_emp_doc_actions(d_users, admin_num, mgr_num):
    client_name = d_users['l_d_clients'][mgr_num - 1].get_client_full_name()
    bns_name = None
    tab_name = "PersonalTab"
    sub_tab = "fromClient"
    tax_year = "2019"
    year = "2019"
    file_names = []
    for file_num in range(1, num_files + 2, 1):
        file_name = str("per_w2_" + str(file_num) + ".pdf")
        file_names.append(file_name)
    doc_obj = test_data_doc_actions(client_name, bns_name, tab_name, sub_tab, tax_year, file_names, year)
    d_users['l_d_doc'].append(doc_obj)

    for bns_num in range (1, num_bns + 1, 1): 
        bns_name = str(str(admin_num).zfill(2) + "_" + str(mgr_num).zfill(2) + "_business" + str(bns_num).zfill(2))
        tab_name = "BusinessTab"
        file_names = []
        for file_num in range(1, num_files + 1, 1):
            file_name = str(str(bns_num).zfill(2) + "bns_w2_" + str(file_num) + ".pdf")
            file_names.append(file_name)
        doc_obj = test_data_doc_actions(client_name, bns_name, tab_name, sub_tab, tax_year, file_names, year)
        d_users['l_d_doc'].append(doc_obj)

def create_unassigned_task_data(d_users, admin_num, mgr_num):
    sub_menu_option = 'unassignedTaskList'
    filter_year = 'All'
    tab_name = None
    filter_status = None
    action = 'assign'
    client_team_member = d_users['l_d_mgrs'][mgr_num - 1].get_full_name()
    l_client_name = []
    l_year = []
    l_client_bns = None
    assert_result = True

    #Unassigned Personal Task 
    tab_name = 'personalTab'
    l_client_name.append(d_users['l_d_clients'][mgr_num - 1].get_client_full_name())
    l_year.append('2019')
    admin_task_obj = test_data_task(sub_menu_option, filter_year, tab_name, filter_status, action,
                                    client_team_member, l_client_name, l_year, l_client_bns, assert_result)
    d_users['l_d_unassigned_tasks'].append(admin_task_obj)

    #Unassigned Business Task
    tab_name = 'businessTab'
    l_client_name = []
    l_year = []
    l_client_bns = []
    for bns_num in range (1, num_bns + 1, 1): 
        # filter_status = None,
        l_client_name.append(d_users['l_d_clients'][mgr_num - 1].get_client_full_name())
        l_year.append('2019')
        l_client_bns = d_users['l_d_clients'][mgr_num - 1].get_c_bns_names()

    admin_task_obj = test_data_task(sub_menu_option, filter_year, tab_name, filter_status, action,
                                     client_team_member, l_client_name, l_year, l_client_bns, assert_result)

    d_users['l_d_unassigned_tasks'].append(admin_task_obj)

def create_assigned_task_data(d_users, admin_num, mgr_num):
    sub_menu_option = 'teamTaskList'
    filter_year = 'All'
    tab_name = None
    filter_status = "Assigned"
    action = 'assign'
    client_team_member = None
    l_client_name = []
    l_year = []
    l_client_bns = None
    assert_result = True

    #assigned Personal Task 
    tab_name = 'personalTab'
    client_team_member = d_users['l_d_emps'][2*(mgr_num - 1)].get_full_name()
    l_client_name.append(d_users['l_d_clients'][mgr_num - 1].get_client_full_name())
    l_year.append('2019')
    admin_task_obj = test_data_task(sub_menu_option, filter_year, tab_name, filter_status, action,
                                    client_team_member, l_client_name, l_year, l_client_bns, assert_result)
    d_users['l_d_assigned_tasks'].append(admin_task_obj)

    #assigned Business Task
    tab_name = 'businessTab'
    client_team_member = d_users['l_d_emps'][2*(mgr_num - 1) + 1].get_full_name()
    l_client_name = []
    l_year = []
    l_client_bns = []
    for bns_num in range (1, num_bns + 1, 1): 
        # filter_status = None,
        l_client_name.append(d_users['l_d_clients'][mgr_num - 1].get_client_full_name())
        l_year.append('2019')
        l_client_bns = d_users['l_d_clients'][mgr_num - 1].get_c_bns_names()

    admin_task_obj = test_data_task(sub_menu_option, filter_year, tab_name, filter_status, action,
                                     client_team_member, l_client_name, l_year, l_client_bns, assert_result)

    d_users['l_d_assigned_tasks'].append(admin_task_obj)

def create_mgr_review_task_data(d_users, admin_num, mgr_num):
    sub_menu_option = 'teamTaskList'
    filter_year = 'All'
    tab_name = None
    filter_status = "In Progress"
    action = 'managerReview'
    client_team_member = None
    l_client_name = []
    l_year = []
    l_client_bns = None
    assert_result = False

    #assigned Personal Task 
    tab_name = 'personalTab'
    l_client_name.append(d_users['l_d_clients'][mgr_num - 1].get_client_full_name())
    l_year.append('2019')
    admin_task_obj = test_data_task(sub_menu_option, filter_year, tab_name, filter_status, action,
                                    client_team_member, l_client_name, l_year, l_client_bns, assert_result)
    d_users['l_d_mgr_review_tasks'].append(admin_task_obj)

    #assigned Business Task
    tab_name = 'businessTab'
    l_client_name = []
    l_year = []
    l_client_bns = []
    for bns_num in range (1, num_bns + 1, 1): 
        # filter_status = None,
        l_client_name.append(d_users['l_d_clients'][mgr_num - 1].get_client_full_name())
        l_year.append('2019')
        l_client_bns = d_users['l_d_clients'][mgr_num - 1].get_c_bns_names()

    admin_task_obj = test_data_task(sub_menu_option, filter_year, tab_name, filter_status, action,
                                     client_team_member, l_client_name, l_year, l_client_bns, assert_result)
    d_users['l_d_mgr_review_tasks'].append(admin_task_obj)

def create_admin_review_task_data(d_users, admin_num, mgr_num):
    sub_menu_option = 'reviewTaskList'
    filter_year = 'All'
    tab_name = None
    filter_status = "In Progress"
    action = 'adminReview'
    client_team_member = None
    l_client_name = []
    l_year = []
    l_client_bns = None
    assert_result = False

    #assigned Personal Task 
    tab_name = 'personalTab'
    l_client_name.append(d_users['l_d_clients'][mgr_num - 1].get_client_full_name())
    l_year.append('2019')
    admin_task_obj = test_data_task(sub_menu_option, filter_year, tab_name, filter_status, action,
                                    client_team_member, l_client_name, l_year, l_client_bns, assert_result)
    d_users['l_d_admin_review_tasks'].append(admin_task_obj)

    #assigned Business Task
    tab_name = 'businessTab'
    l_client_name = []
    l_year = []
    l_client_bns = []
    for bns_num in range (1, num_bns + 1, 1): 
        # filter_status = None,
        l_client_name.append(d_users['l_d_clients'][mgr_num - 1].get_client_full_name())
        l_year.append('2019')
        l_client_bns = d_users['l_d_clients'][mgr_num - 1].get_c_bns_names()

    admin_task_obj = test_data_task(sub_menu_option, filter_year, tab_name, filter_status, action,
                                     client_team_member, l_client_name, l_year, l_client_bns, assert_result)
    d_users['l_d_admin_review_tasks'].append(admin_task_obj)

def create_client_review_task_data(d_users, admin_num):
    sub_menu_option = 'reviewTaskList'
    filter_year = 'All'
    tab_name = None
    filter_status = None
    action = 'clientReview'
    client_team_member = None
    l_client_name = []
    l_year = []
    l_client_bns = None
    assert_result = True

    #assigned Personal Task 
    tab_name = 'personalTab'
    for client_num in range(1, num_clients + 1, 1):
        l_client_name.append(d_users['l_d_clients'][client_num - 1].get_client_full_name())
        l_year.append('2019')
    admin_task_obj = test_data_task(sub_menu_option, filter_year, tab_name, filter_status, action,
                                    client_team_member, l_client_name, l_year, l_client_bns, assert_result)
    d_users['l_d_client_review_tasks'].append(admin_task_obj)

    #assigned Business Task
    tab_name = 'businessTab'
    for client_num in range(1, num_clients + 1, 1):
        l_client_name = []
        l_year = []
        l_client_bns = []
        # filter_status = None,
        l_client_name.append(d_users['l_d_clients'][client_num - 1].get_client_full_name())
        l_year.append('2019')
        l_client_name.append(d_users['l_d_clients'][client_num - 1].get_client_full_name())
        l_year.append('2019')
        l_client_bns = d_users['l_d_clients'][client_num - 1].get_c_bns_names()
        admin_task_obj = test_data_task(sub_menu_option, filter_year, tab_name, filter_status, action,
                                        client_team_member, l_client_name, l_year, l_client_bns, assert_result)
        d_users['l_d_client_review_tasks'].append(admin_task_obj)

def create_efile_auth_task_data(d_users, admin_num):
    sub_menu_option = 'clientTaskList'
    filter_year = 'All'
    tab_name = None
    filter_status = 'Client Review'
    action = 'efileAuth'
    client_team_member = None
    l_client_name = []
    l_year = []
    l_client_bns = None
    assert_result = True

    #assigned Personal Task 
    tab_name = 'personalTab'
    for client_num in range(1, num_clients + 1, 1):
        l_client_name.append(d_users['l_d_clients'][client_num - 1].get_client_full_name())
        l_year.append('2019')
    admin_task_obj = test_data_task(sub_menu_option, filter_year, tab_name, filter_status, action,
                                    client_team_member, l_client_name, l_year, l_client_bns, assert_result)
    d_users['l_d_efile_auth_tasks'].append(admin_task_obj)

    #assigned Business Task
    tab_name = 'businessTab'
    for client_num in range(1, num_clients + 1, 1):
        l_client_name = []
        l_year = []
        l_client_bns = []
        # filter_status = None,
        l_client_name.append(d_users['l_d_clients'][client_num - 1].get_client_full_name())
        l_year.append('2019')
        l_client_name.append(d_users['l_d_clients'][client_num - 1].get_client_full_name())
        l_year.append('2019')
        l_client_bns = d_users['l_d_clients'][client_num - 1].get_c_bns_names()
        admin_task_obj = test_data_task(sub_menu_option, filter_year, tab_name, filter_status, action,
                                        client_team_member, l_client_name, l_year, l_client_bns, assert_result)
        d_users['l_d_efile_auth_tasks'].append(admin_task_obj)

def create_efiled_task_data(d_users, admin_num):
    sub_menu_option = 'clientTaskList'
    filter_year = 'All'
    tab_name = None
    filter_status = 'Efile Auth'
    action = 'efiled'
    client_team_member = None
    l_client_name = []
    l_year = []
    l_client_bns = None
    assert_result = True

    #assigned Personal Task 
    tab_name = 'personalTab'
    for client_num in range(1, num_clients + 1, 1):
        l_client_name.append(d_users['l_d_clients'][client_num - 1].get_client_full_name())
        l_year.append('2019')
    admin_task_obj = test_data_task(sub_menu_option, filter_year, tab_name, filter_status, action,
                                    client_team_member, l_client_name, l_year, l_client_bns, assert_result)
    d_users['l_d_efiled_tasks'].append(admin_task_obj)

    #assigned Business Task
    tab_name = 'businessTab'
    for client_num in range(1, num_clients + 1, 1):
        l_client_name = []
        l_year = []
        l_client_bns = []
        # filter_status = None,
        l_client_name.append(d_users['l_d_clients'][client_num - 1].get_client_full_name())
        l_year.append('2019')
        l_client_name.append(d_users['l_d_clients'][client_num - 1].get_client_full_name())
        l_year.append('2019')
        l_client_bns = d_users['l_d_clients'][client_num - 1].get_c_bns_names()
        admin_task_obj = test_data_task(sub_menu_option, filter_year, tab_name, filter_status, action,
                                        client_team_member, l_client_name, l_year, l_client_bns, assert_result)
        d_users['l_d_efiled_tasks'].append(admin_task_obj)

def create_closed_task_data(d_users, admin_num):
    sub_menu_option = 'closureTaskList'
    filter_year = 'All'
    tab_name = None
    filter_status = 'Efiled'
    action = 'close'
    client_team_member = None
    l_client_name = []
    l_year = []
    l_client_bns = None
    assert_result = True

    #assigned Personal Task 
    tab_name = 'personalTab'
    for client_num in range(1, num_clients + 1, 1):
        l_client_name.append(d_users['l_d_clients'][client_num - 1].get_client_full_name())
        l_year.append('2019')
    admin_task_obj = test_data_task(sub_menu_option, filter_year, tab_name, filter_status, action,
                                    client_team_member, l_client_name, l_year, l_client_bns, assert_result)
    d_users['l_d_closed_tasks'].append(admin_task_obj)

    #assigned Business Task
    tab_name = 'businessTab'
    for client_num in range(1, num_clients + 1, 1):
        l_client_name = []
        l_year = []
        l_client_bns = []
        # filter_status = None,
        l_client_name.append(d_users['l_d_clients'][client_num - 1].get_client_full_name())
        l_year.append('2019')
        l_client_name.append(d_users['l_d_clients'][client_num - 1].get_client_full_name())
        l_year.append('2019')
        l_client_bns = d_users['l_d_clients'][client_num - 1].get_c_bns_names()
        admin_task_obj = test_data_task(sub_menu_option, filter_year, tab_name, filter_status, action,
                                        client_team_member, l_client_name, l_year, l_client_bns, assert_result)
        d_users['l_d_closed_tasks'].append(admin_task_obj)

def create_data_messages(d_users):
    #1
    msg_obj1 = test_data_msgs(client_msg = ["I have reviewed. Please e-file"], team_msg= None)

    d_users['l_d_msgs'].append(msg_obj1)
    #2
    msg_obj2 = test_data_msgs(client_msg = ["Sent for Efile authorization"], team_msg= None)

    d_users['l_d_msgs'].append(msg_obj2)
    #3
    msg_obj3 = test_data_msgs(client_msg = ["Authorized for efiling"], team_msg= None)

    d_users['l_d_msgs'].append(msg_obj3)

