from pm.test.test_data.test_transactions import *
from pm.test.regression.rg_test_data_gen import *
import pdb

def execute_task_transitions(driver, obj, admin_num):
    l_transactions = []
    admin_obj = obj.get_admin_data(admin_num)
    # appointment
    special_admin_obj = obj.get_special_admin_data(admin_num)
    special_mgr_obj = obj.get_special_mgr_data(admin_num)
    special_client_obj = obj.get_special_client_data(admin_num)
    l_d_special_rcp = obj.get_all_special_rcp_data(admin_num)
    l_d_appointments = obj.get_all_admin_appointment_test_data(admin_num)

    super_admin_obj = obj.get_super_admin_data(admin_num)
    super_admin_emp_obj = obj.get_super_admin_emp_data(admin_num)
    l_d_clients = obj.get_all_client_data(admin_num)
    l_d_update_client_profile = obj.get_all_client_update_profile_data(admin_num)
    l_d_rcp = obj.get_all_rcp_data(admin_num)
    l_d_mgrs = obj.get_all_mgrs_data(admin_num)
    l_d_emps = obj.get_all_emps_data(admin_num)
    l_d_unassigned_tasks = obj.get_all_unassigned_tasks_data(admin_num)
    l_d_assigned_tasks = obj.get_all_assigned_tasks_data(admin_num)
    l_d_due_date_tasks = obj.get_all_due_date_tasks_data(admin_num)
    l_d_mgr_review_tasks = obj.get_all_mgr_review_tasks_data(admin_num)
    l_d_admin_review_tasks = obj.get_all_admin_review_tasks_data(admin_num)
    l_d_client_review_tasks = obj.get_all_client_review_tasks_data(admin_num)
    l_d_efile_auth_sendReminder_tasks = obj.get_all_efile_auth_sendReminder_tasks_data(admin_num)
    l_d_efile_auth_tasks = obj.get_all_efile_auth_tasks_data(admin_num)
    l_d_efiled_tasks = obj.get_all_efiled_tasks_data(admin_num)
    l_d_closed_tasks = obj.get_all_closed_tasks_data(admin_num)
    l_d_doc = obj.get_all_doc_data(admin_num)
    l_d_msgs = obj.get_all_msgs_data(admin_num)
    # team and client actions
    l_d_clients_delete = obj.get_all_client_delete_data(admin_num)
    l_d_mgrs_delete = obj.get_all_mgrs_delete_data(admin_num)
    l_d_team_actions = obj.get_all_admin_team_action_data(admin_num)
    l_d_client_actions = obj.get_all_admin_client_action_data(admin_num)
    # ticket objects
    l_d_ticket = obj.get_all_admin_ticket_action_data(admin_num)
    l_d_insight_practice = obj.get_all_admin_insights_practice_data(admin_num)
    l_d_insight_client = obj.get_all_admin_insights_client_data(admin_num)
    l_d_insight_growth = obj.get_all_admin_insights_growth_data(admin_num)

    d_price_cal = obj.get_price_cal_data(admin_num)
    l_d_price_est = obj.get_price_est_data(admin_num)
    l_todo_tasks = obj.get_todo_task_data(admin_num)
    l_invoice = obj.get_add_invoice_data(admin_num)
    l_invoice_verify = obj.get_verify_invoice_data(admin_num)
    l_access_settings = obj.get_access_settings_data(admin_num)
    l_verify_access_settings = obj.get_verify_access_settings_data(admin_num)
    l_notifi_count = obj.get_notifi_count_data(admin_num)
    l_notifi_msg_count = obj.get_notifi_msg_count_data(admin_num)
    l_auto_todo = obj.get_auto_todo_data(admin_num)
    d_reset_password_obj = obj.get_reset_password_data(admin_num)

# CPA Register
    obj_transaction = test_transaction('pm_key_add_admin', admin_obj)
    l_transactions.append(obj_transaction)

# CPA signin
    obj_transaction = test_transaction('pm_key_signin', admin_obj)
    l_transactions.append(obj_transaction)

# navigate to admin profile settings
    obj_transaction = test_transaction('pm_key_navigate_to_admin_profile', None)
    l_transactions.append(obj_transaction)

# change price for tax return
    obj_transaction = test_transaction('pm_key_admin_profile_price_cal', d_price_cal)
    l_transactions.append(obj_transaction)

# add client
    obj_transaction = test_transaction('pm_key_add_client', l_d_clients)
    l_transactions.append(obj_transaction)

# add client to be deleted
    obj_transaction = test_transaction('pm_key_add_client', l_d_clients_delete)
    l_transactions.append(obj_transaction)

# add receptionist
    obj_transaction = test_transaction('pm_key_add_emp', l_d_rcp)
    l_transactions.append(obj_transaction)
# add managers
    obj_transaction = test_transaction('pm_key_add_emp', l_d_mgrs)
    l_transactions.append(obj_transaction)
# add employees
    obj_transaction = test_transaction('pm_key_add_emp', l_d_emps)
    l_transactions.append(obj_transaction)

# add manager to be deleted
    obj_transaction = test_transaction('pm_key_add_emp', l_d_mgrs_delete)
    l_transactions.append(obj_transaction)

# CPA signout
    obj_transaction = test_transaction('pm_key_signout', None)
    l_transactions.append(obj_transaction)

    if obj.appointment_test == 'yes':
        # CPA Signin
        obj_transaction = test_transaction('pm_key_signin', special_admin_obj)
        l_transactions.append(obj_transaction)

    # add receptionist
        obj_transaction = test_transaction('pm_key_add_emp', l_d_special_rcp)
        l_transactions.append(obj_transaction)

        obj_transaction = test_transaction('pm_key_appointment', l_d_appointments[0])
        l_transactions.append(obj_transaction)

        obj_transaction = test_transaction('pm_key_appointment', l_d_appointments[1])
        l_transactions.append(obj_transaction)

    # CPA Signout
        obj_transaction = test_transaction('pm_key_signout', None)
        l_transactions.append(obj_transaction)

# log in as john
        obj_transaction = test_transaction('pm_key_signin', special_mgr_obj)
        l_transactions.append(obj_transaction)
    # perform action yes
        obj_transaction = test_transaction('pm_key_appointment', l_d_appointments[2])
        l_transactions.append(obj_transaction)
    # log out john
        obj_transaction = test_transaction('pm_key_signout', None)
        l_transactions.append(obj_transaction)

    # log in as client
        obj_transaction = test_transaction('pm_key_signin', special_client_obj)
        l_transactions.append(obj_transaction)
    # perform action yes
    # join meeting
        obj_transaction = test_transaction('pm_key_appointment', l_d_appointments[3])
        l_transactions.append(obj_transaction)
    # client log out
        obj_transaction = test_transaction('pm_key_signout', special_client_obj)
        l_transactions.append(obj_transaction)

    # login receptionist
        obj_transaction = test_transaction('pm_key_signin', l_d_special_rcp[0])
        l_transactions.append(obj_transaction)
        obj_transaction = test_transaction('pm_key_appointment', l_d_appointments[4])
        l_transactions.append(obj_transaction)

    # receptionist log out
        obj_transaction = test_transaction('pm_key_signout', l_d_special_rcp[0])
        l_transactions.append(obj_transaction)


    for count, d_team_action in enumerate(l_d_team_actions):
        # CPA Signin
        obj_transaction = test_transaction('pm_key_signin', admin_obj)
        l_transactions.append(obj_transaction)

        obj_transaction = test_transaction('pm_key_admin_team_actions', d_team_action)
        l_transactions.append(obj_transaction)

        obj_transaction = test_transaction('pm_key_signout', None)
        l_transactions.append(obj_transaction)

        for emp_count, d_emp in enumerate(l_d_emps[-1:]):
            obj_transaction = test_transaction('pm_key_signin', d_emp)
            l_transactions.append(obj_transaction)
            if count == 4:
                if emp_count != len(l_d_emps):
                    obj_transaction = test_transaction('pm_key_can_user_logout', d_emp)
                    l_transactions.append(obj_transaction)
                else:
                    obj_transaction = test_transaction('pm_key_can_user_login', d_emp)
                    l_transactions.append(obj_transaction)
            else:
                obj_transaction = test_transaction('pm_key_can_user_login', d_emp)
                l_transactions.append(obj_transaction)


    for count, d_client_action in enumerate(l_d_client_actions):
        # CPA Signin
        obj_transaction = test_transaction('pm_key_signin', admin_obj)
        l_transactions.append(obj_transaction)

        obj_transaction = test_transaction('pm_key_admin_client_actions', d_client_action)
        l_transactions.append(obj_transaction)

        obj_transaction = test_transaction('pm_key_signout', None)
        l_transactions.append(obj_transaction)

        for client_count, d_client in enumerate(l_d_clients[-1:]):
        # client signin
            obj_transaction = test_transaction('pm_key_signin', d_client)
            l_transactions.append(obj_transaction)
            if count == 4:
                if client_count != len(l_d_clients):
                    obj_transaction = test_transaction('pm_key_can_user_logout', d_client)
                    l_transactions.append(obj_transaction)
                else:
                    obj_transaction = test_transaction('pm_key_can_user_login', d_client)
                    l_transactions.append(obj_transaction)
            else:
            # client signin
                obj_transaction = test_transaction('pm_key_can_user_login', d_client)
                l_transactions.append(obj_transaction)

    if obj.ticket_test == 'yes':
    # CPA Signin
        obj_transaction = test_transaction('pm_key_signin', admin_obj)
        l_transactions.append(obj_transaction)
        # Add new Ticket
        obj_transaction = test_transaction('pm_key_add_ticket', l_d_ticket[0])
        l_transactions.append(obj_transaction)
        # CPA signout
        obj_transaction = test_transaction('pm_key_signout', admin_obj)
        l_transactions.append(obj_transaction)

        # super Signin
        obj_transaction = test_transaction('pm_key_signin', super_admin_obj)
        l_transactions.append(obj_transaction)
        # reply to Ticket
        obj_transaction = test_transaction('pm_key_super_admin_ticket_reply', l_d_ticket[1])
        l_transactions.append(obj_transaction)
        # super_admin signout
        obj_transaction = test_transaction('pm_key_signout', super_admin_obj)
        l_transactions.append(obj_transaction)

        # super_admin_emp Signin
        obj_transaction = test_transaction('pm_key_signin', super_admin_emp_obj)
        l_transactions.append(obj_transaction)
        # reply to Ticket
        obj_transaction = test_transaction('pm_key_super_admin_ticket_reply', l_d_ticket[2])
        l_transactions.append(obj_transaction)
        # super_admin signout
        obj_transaction = test_transaction('pm_key_signout', super_admin_emp_obj)
        l_transactions.append(obj_transaction)

        # CPA Signin
        obj_transaction = test_transaction('pm_key_signin', admin_obj)
        l_transactions.append(obj_transaction)
        # Add new Ticket
        obj_transaction = test_transaction('pm_key_admin_ticket_reply', l_d_ticket[3])
        l_transactions.append(obj_transaction)

        obj_transaction = test_transaction('pm_key_close_ticket', l_d_ticket[4])
        l_transactions.append(obj_transaction)
        # CPA signout
        obj_transaction = test_transaction('pm_key_signout', admin_obj)
        l_transactions.append(obj_transaction)

        # super Signin
        obj_transaction = test_transaction('pm_key_signin', super_admin_obj)
        l_transactions.append(obj_transaction)
        # reply to Ticket
        obj_transaction = test_transaction('pm_key_super_admin_close_ticket_validation', l_d_ticket[5])
        l_transactions.append(obj_transaction)
        # super_admin signout
        obj_transaction = test_transaction('pm_key_signout', super_admin_obj)
        l_transactions.append(obj_transaction)

    for count, d_client in enumerate(l_d_clients):
    # client signin
        obj_transaction = test_transaction('pm_key_signin', d_client)
        l_transactions.append(obj_transaction)
    # Update Profile
        obj_transaction = test_transaction('pm_key_update_client_profile', l_d_update_client_profile[count])
        l_transactions.append(obj_transaction)
    # add new business
        obj_transaction = test_transaction('pm_key_c_add_bns', d_client)
        l_transactions.append(obj_transaction)
    # uploading client personal and business files
        obj_transaction = test_transaction('pm_key_c_upload_files', d_client)
        l_transactions.append(obj_transaction)
    # client signout
        obj_transaction = test_transaction('pm_key_signout', None)
        l_transactions.append(obj_transaction)

# Generate auto todo
    obj_transaction = test_transaction('pm_key_auto_todo', None)
    l_transactions.append(obj_transaction)

# CPA signin
    obj_transaction = test_transaction('pm_key_signin', admin_obj)
    l_transactions.append(obj_transaction)

# check auto todo notifications count
    obj_transaction = test_transaction('pm_key_check_notification_count', l_notifi_count[3])
    l_transactions.append(obj_transaction)
# check auto todo notification msgs count
    obj_transaction = test_transaction('pm_key_check_notification_msgs_count', l_notifi_msg_count[4])
    l_transactions.append(obj_transaction)

# price est validation
    price_est_idx = 0
    todo_task_idx = 0
    auto_todo_indx = 0
    process_auto_todo_indx = 0
    for d_client in l_d_clients:
    # navigate to admin client dashboard
        obj_transaction = test_transaction('pm_key_navigation_to_admin_client', d_client)
        l_transactions.append(obj_transaction)

    #check auto todo checkboxes
        obj_transaction = test_transaction('pm_key_client_dashboard_check_todo', l_auto_todo[auto_todo_indx])
        l_transactions.append(obj_transaction)
        obj_transaction = test_transaction('pm_key_client_dashboard_check_todo', l_auto_todo[auto_todo_indx + 1])
        l_transactions.append(obj_transaction)
        auto_todo_indx += 2

    #process auto todo tasks
        obj_transaction = test_transaction('pm_key_admin_client_todo_complt', l_auto_todo[process_auto_todo_indx])
        l_transactions.append(obj_transaction)
        obj_transaction = test_transaction('pm_key_admin_client_todo_complt', l_auto_todo[process_auto_todo_indx + 1])
        l_transactions.append(obj_transaction)
        process_auto_todo_indx += 2

    # add  todo tasks
        obj_transaction = test_transaction('pm_key_admin_client_todo_task', l_todo_tasks[todo_task_idx])
        l_transactions.append(obj_transaction)
        todo_task_idx += 1

    # invoice add
        for index, values in enumerate(l_invoice):
            obj_transaction = test_transaction('pm_key_admin_client_invoice', l_invoice[index])
            l_transactions.append(obj_transaction)

    # validate price es1
        obj_transaction = test_transaction('pm_key_admin_client_update_price_est', l_d_price_est[price_est_idx])
        l_transactions.append(obj_transaction)

        obj_transaction = test_transaction('pm_key_admin_client_update_price_est', l_d_price_est[price_est_idx + 1])
        l_transactions.append(obj_transaction)
        price_est_idx += 2

    # check todo notification count
        obj_transaction = test_transaction('pm_key_check_notification_count', l_notifi_count[2])
        l_transactions.append(obj_transaction)

    # check todo notification msgs count
        obj_transaction = test_transaction('pm_key_check_notification_msgs_count', l_notifi_msg_count[3])
        l_transactions.append(obj_transaction)

    # admin signout
    obj_transaction = test_transaction('pm_key_signout', None)
    l_transactions.append(obj_transaction)

    todo_task_idx = 0
    invoice_verify_inx = 0
    for d_client in l_d_clients:
    # client  login
        obj_transaction = test_transaction('pm_key_signin', d_client)
        l_transactions.append(obj_transaction)

    # check todo checkbox
        obj_transaction = test_transaction('pm_key_client_dashboard_check_todo', l_todo_tasks[todo_task_idx])
        l_transactions.append(obj_transaction)
        todo_task_idx += 1
    # invoice verify
        for invoice in l_invoice_verify:
            obj_transaction = test_transaction('pm_key_client_dashboard_invoice', invoice)
            l_transactions.append(obj_transaction)

    # client signout
        obj_transaction = test_transaction('pm_key_signout', None)
        l_transactions.append(obj_transaction)

    # CPA signin
    obj_transaction = test_transaction('pm_key_signin', admin_obj)
    l_transactions.append(obj_transaction)

    todo_task_idx = 0
    for d_client in l_d_clients:
    # navigate to admin client dashboard
        obj_transaction = test_transaction('pm_key_navigation_to_admin_client', d_client)
        l_transactions.append(obj_transaction)

    # complete todo checkbox
        obj_transaction = test_transaction('pm_key_admin_client_todo_complt', l_todo_tasks[todo_task_idx])
        l_transactions.append(obj_transaction)
        todo_task_idx += 1

    # admin practice insights
    for practiceInsights in l_d_insight_practice[0:2]:
        obj_transaction = test_transaction('pm_key_insight_practice', practiceInsights)
        l_transactions.append(obj_transaction)

    # CPA signout
    obj_transaction = test_transaction('pm_key_signout', None)
    l_transactions.append(obj_transaction)

    i = 0
    j = 0
    client_link_indx = 0
    for d_mgr in l_d_mgrs:
    # CPA signin
        obj_transaction = test_transaction('pm_key_signin', admin_obj)
        l_transactions.append(obj_transaction)
    # individual tab client assign to a m1
        obj_transaction = test_transaction('pm_key_task_action', l_d_unassigned_tasks[i])
        l_transactions.append(obj_transaction)
    # business tab client assign to a m1
        obj_transaction = test_transaction('pm_key_task_action', l_d_unassigned_tasks[i+1])
        l_transactions.append(obj_transaction)

    # navigate to admin client dashboard
        obj_transaction = test_transaction('pm_key_navigation_to_admin_client', l_d_clients[client_link_indx])
        l_transactions.append(obj_transaction)
        client_link_indx += 1

    # send team1 msg
        obj_transaction = test_transaction('pm_key_send_team_msg', l_d_msgs[3])
        l_transactions.append(obj_transaction)

    # CPA signout
        obj_transaction = test_transaction('pm_key_signout', None)
        l_transactions.append(obj_transaction)

        i = i + len(l_d_mgrs)

    # Manager signin
        obj_transaction = test_transaction('pm_key_signin', d_mgr)
        l_transactions.append(obj_transaction)
    # individual tab client assign to a e1
        obj_transaction = test_transaction('pm_key_task_action', l_d_assigned_tasks[j])
        l_transactions.append(obj_transaction)
    # business tab client assign to a e2
        obj_transaction = test_transaction('pm_key_task_action', l_d_assigned_tasks[j+1])
        l_transactions.append(obj_transaction)
    # Manager signout
        obj_transaction = test_transaction('pm_key_signout', None)
        l_transactions.append(obj_transaction)

        j = j + len(l_d_mgrs)


# profile settings e2e access settings
# admin sign in
    obj_transaction = test_transaction('pm_key_signin', admin_obj)
    l_transactions.append(obj_transaction)

# navigate to admin profile settings
    obj_transaction = test_transaction('pm_key_navigate_to_admin_profile', None)
    l_transactions.append(obj_transaction)

# uncheck access settings
    obj_transaction = test_transaction('pm_key_admin_profile_uncheck_access_settings', l_access_settings[0])
    l_transactions.append(obj_transaction)

#1
# mgr sign in
    obj_transaction = test_transaction('pm_key_signin', l_d_mgrs[0])
    l_transactions.append(obj_transaction)

#validate  tasks id
    obj_transaction = test_transaction('pm_key_validate_id', l_verify_access_settings[0])
    l_transactions.append(obj_transaction)

#nav to emp client dashboard
    obj_transaction = test_transaction('pm_key_nav_to_client_dashboard', l_access_settings[2])
    l_transactions.append(obj_transaction)

#validate bns, price est, invoice ids, client msgs
    obj_transaction = test_transaction('pm_key_validate_id', l_verify_access_settings[1])
    l_transactions.append(obj_transaction)
#mgr signout
    obj_transaction = test_transaction('pm_key_signout', None)
    l_transactions.append(obj_transaction)

#2
#  emp sign in
    obj_transaction = test_transaction('pm_key_signin', l_d_emps[0])
    l_transactions.append(obj_transaction)

#validate unassigned, client and closure and extension ids
    obj_transaction = test_transaction('pm_key_validate_id', l_verify_access_settings[0])
    l_transactions.append(obj_transaction)

#nav to emp client dashboard
    obj_transaction = test_transaction('pm_key_nav_to_client_dashboard', l_access_settings[2])
    l_transactions.append(obj_transaction)

#validate bns and price and invoice ids, team msgs
    obj_transaction = test_transaction('pm_key_validate_id', l_verify_access_settings[1])
    l_transactions.append(obj_transaction)

# emp logout
    obj_transaction = test_transaction('pm_key_signout', None)
    l_transactions.append(obj_transaction)

# checking all checkboxes agian
# admin sign in
    obj_transaction = test_transaction('pm_key_signin', admin_obj)
    l_transactions.append(obj_transaction)

# navigate to admin profile settings
    obj_transaction = test_transaction('pm_key_navigate_to_admin_profile', None)
    l_transactions.append(obj_transaction)

# check access settings
    obj_transaction = test_transaction('pm_key_admin_profile_check_access_settings', l_access_settings[1])
    l_transactions.append(obj_transaction)

###
    for due_date in l_d_due_date_tasks:
    # individual tab client due date change
        obj_transaction = test_transaction('pm_key_task_action', due_date)
        l_transactions.append(obj_transaction)
    # CPA signout
    obj_transaction = test_transaction('pm_key_signout', None)
    l_transactions.append(obj_transaction)


    k = 0
    l = 0
    for d_emp in l_d_emps:
    # Employee signin
        obj_transaction = test_transaction('pm_key_signin', d_emp)
        l_transactions.append(obj_transaction)
    # Process the client documents
        obj_transaction = test_transaction('pm_key_emp_process_client_docs', l_d_doc[k])
        l_transactions.append(obj_transaction)
        if (k==1 or k==4):
            k = k + 1
            obj_transaction = test_transaction('pm_key_emp_process_client_docs', l_d_doc[k])
            l_transactions.append(obj_transaction)

    # Send File for Manager Review
        obj_transaction = test_transaction('pm_key_task_action', l_d_mgr_review_tasks[l])
        l_transactions.append(obj_transaction)
        k = k + 1
        l = l + 1

    k = 0
    l = 0
    client_inx = 1
    for d_mgr in l_d_mgrs:
    # Manager signin
        obj_transaction = test_transaction('pm_key_signin', d_mgr)
        l_transactions.append(obj_transaction)
    # Process the client documents
        obj_transaction = test_transaction('pm_key_mgr_process_client_docs', l_d_doc[k])
        l_transactions.append(obj_transaction)
        if (k==0 or k==3):
            k = k + 1
            obj_transaction = test_transaction('pm_key_mgr_process_client_docs', l_d_doc[k])
            l_transactions.append(obj_transaction)
            k = k + 1
            obj_transaction = test_transaction('pm_key_mgr_process_client_docs', l_d_doc[k])
            l_transactions.append(obj_transaction)

    # send team1 msg
        obj_transaction = test_transaction('pm_key_send_team_msg', l_d_msgs[5])
        l_transactions.append(obj_transaction)

    # Send File for Admin Review
        obj_transaction = test_transaction('pm_key_task_action', l_d_admin_review_tasks[l])
        l_transactions.append(obj_transaction)
        obj_transaction = test_transaction('pm_key_task_action', l_d_admin_review_tasks[l+1])
        l_transactions.append(obj_transaction)
        k = k + 1
        l = l + len(l_d_mgrs)
    #team notifications
    # admin sign in
        obj_transaction = test_transaction('pm_key_signin', admin_obj)
        l_transactions.append(obj_transaction)

    # check notification count
        obj_transaction = test_transaction('pm_key_check_notification_count', l_notifi_count[1])
        l_transactions.append(obj_transaction)

    # check notification msgs count of team
        obj_transaction = test_transaction('pm_key_check_notification_msgs_count', l_notifi_msg_count[client_inx])
        l_transactions.append(obj_transaction)
        client_inx += 1

    # admin signout
        obj_transaction = test_transaction('pm_key_signout', None)
        l_transactions.append(obj_transaction)
    # Send team message - "Sending for CPA Review"

    # CPA signin
    obj_transaction = test_transaction('pm_key_signin', admin_obj)
    l_transactions.append(obj_transaction)

    # admin practice insights
    for practiceInsights in l_d_insight_practice[2:4]:
        obj_transaction = test_transaction('pm_key_insight_practice', practiceInsights)
        l_transactions.append(obj_transaction)

    # CPA signout
    obj_transaction = test_transaction('pm_key_signout', None)
    l_transactions.append(obj_transaction)

    l = 0
    # CPA signin
    obj_transaction = test_transaction('pm_key_signin', admin_obj)
    l_transactions.append(obj_transaction)
    # Process the client documents
    for i in range (0, len(l_d_doc), 1):
        obj_transaction = test_transaction('pm_key_admin_process_client_docs', l_d_doc[i])
        l_transactions.append(obj_transaction)
    # Send File for Client Review
    obj_transaction = test_transaction('pm_key_task_action', l_d_client_review_tasks[l])
    l_transactions.append(obj_transaction)
    obj_transaction = test_transaction('pm_key_task_action', l_d_client_review_tasks[l+1])
    l_transactions.append(obj_transaction)
    obj_transaction = test_transaction('pm_key_task_action', l_d_client_review_tasks[l+2])
    l_transactions.append(obj_transaction)

    # admin practice insights
    for practiceInsights in l_d_insight_practice[4:6]:
        obj_transaction = test_transaction('pm_key_insight_practice', practiceInsights)
        l_transactions.append(obj_transaction)

    # CPA signout
    obj_transaction = test_transaction('pm_key_signout', None)
    l_transactions.append(obj_transaction)

    for d_client in l_d_clients:
    # client signin
        obj_transaction = test_transaction('pm_key_signin', d_client)
        l_transactions.append(obj_transaction)
    # client send message
        obj_transaction = test_transaction('pm_key_send_client_msg', l_d_msgs[0])
        l_transactions.append(obj_transaction)
    # client signout
        obj_transaction = test_transaction('pm_key_signout', None)
        l_transactions.append(obj_transaction)

    l = 0
    # CPA signin
    obj_transaction = test_transaction('pm_key_signin', admin_obj)
    l_transactions.append(obj_transaction)
    # Send File for E-file Auth
    obj_transaction = test_transaction('pm_key_task_action', l_d_efile_auth_tasks[l])
    l_transactions.append(obj_transaction)
    obj_transaction = test_transaction('pm_key_task_action', l_d_efile_auth_tasks[l+1])
    l_transactions.append(obj_transaction)
    obj_transaction = test_transaction('pm_key_task_action', l_d_efile_auth_tasks[l+2])
    l_transactions.append(obj_transaction)

    # Change status to e-filed
    for sendReminder_obj in l_d_efile_auth_sendReminder_tasks:
        obj_transaction = test_transaction('pm_key_task_action', sendReminder_obj)
        l_transactions.append(obj_transaction)

    for d_client in l_d_clients:
    # navigate to client dashboard
        obj_transaction = test_transaction('pm_key_nav_to_client_dashboard', l_d_doc[l])
        l_transactions.append(obj_transaction)
        l = l + 3
    # client send message
        obj_transaction = test_transaction('pm_key_send_client_msg', l_d_msgs[1])
        l_transactions.append(obj_transaction)

    # admin practice insights
    for practiceInsights in l_d_insight_practice[6:8]:
        obj_transaction = test_transaction('pm_key_insight_practice', practiceInsights)
        l_transactions.append(obj_transaction)

    # CPA signout
    obj_transaction = test_transaction('pm_key_signout', None)
    l_transactions.append(obj_transaction)

    for d_client in l_d_clients:
    # client signin
        obj_transaction = test_transaction('pm_key_signin', d_client)
        l_transactions.append(obj_transaction)
    # client send message
        obj_transaction = test_transaction('pm_key_send_client_msg', l_d_msgs[2])
        l_transactions.append(obj_transaction)
    # client signout
        obj_transaction = test_transaction('pm_key_signout', None)
        l_transactions.append(obj_transaction)

# client notifications
#admin sign in
    obj_transaction = test_transaction('pm_key_signin', admin_obj)
    l_transactions.append(obj_transaction)

# check client notification count
    obj_transaction = test_transaction('pm_key_check_notification_count', l_notifi_count[0])
    l_transactions.append(obj_transaction)

# check client notification msgs count
    obj_transaction = test_transaction('pm_key_check_notification_msgs_count', l_notifi_msg_count[0])
    l_transactions.append(obj_transaction)

    l = 0
    # Change status to e-filed
    obj_transaction = test_transaction('pm_key_task_action', l_d_efiled_tasks[l])
    l_transactions.append(obj_transaction)
    obj_transaction = test_transaction('pm_key_task_action', l_d_efiled_tasks[l+1])
    l_transactions.append(obj_transaction)
    obj_transaction = test_transaction('pm_key_task_action', l_d_efiled_tasks[l+2])
    l_transactions.append(obj_transaction)

    # admin practice insights
    for practiceInsights in l_d_insight_practice[8:10]:
        obj_transaction = test_transaction('pm_key_insight_practice', practiceInsights)
        l_transactions.append(obj_transaction)


    # Change status to closed
    obj_transaction = test_transaction('pm_key_task_action', l_d_closed_tasks[l])
    l_transactions.append(obj_transaction)
    obj_transaction = test_transaction('pm_key_task_action', l_d_closed_tasks[l+1])
    l_transactions.append(obj_transaction)
    obj_transaction = test_transaction('pm_key_task_action', l_d_closed_tasks[l+2])
    l_transactions.append(obj_transaction)

    # admin practice insights
    for practiceInsights in l_d_insight_practice[10:]:
        obj_transaction = test_transaction('pm_key_insight_practice', practiceInsights)
        l_transactions.append(obj_transaction)

    # admin client insights
    for clientInsights in l_d_insight_client:
        obj_transaction = test_transaction('pm_key_insight_client', clientInsights)
        l_transactions.append(obj_transaction)

    # admin growth insights
    for obj_growthInsights in l_d_insight_growth:
        obj_transaction = test_transaction('pm_key_insight_growth', obj_growthInsights)
        l_transactions.append(obj_transaction)

    # CPA signout
    obj_transaction = test_transaction('pm_key_signout', None)
    l_transactions.append(obj_transaction)

    # # reset password
    for client in l_d_clients:
        # client login
        obj_transaction = test_transaction('pm_key_signin', client)
        l_transactions.append(obj_transaction)

        obj_transaction = test_transaction('pm_key_change_password', d_reset_password_obj)
        l_transactions.append(obj_transaction)

#############################################################################


# execute transactions
    execute_transactions(l_transactions, driver)
