from pm.log.admin.lg_admin_add import *
from pm.log.admin.lg_admin_client import *
from pm.log.common.lg_client import *
from pm.log.emp.lg_emp import *

# from pm.log.common.signout import *

# from pm.log.common.signout import *

from pm.log.common.lg_signin import *


def create_log(params, response):
    getattr(c_log, "create_" + params['context'] + "_log")(params, response)


class c_log():
    @staticmethod
    def create_super_admin_log(params, response):
        admin_id = params['super_admin_id']
        log_context = {}
        get_admin_info(log_context, admin_id)
        params['log_context'] = log_context
        if params['key'] == "pm_key_super_admin_ticket_reply":
            create_super_admin_ticket_reply_log(params, response)
        elif params['key']=="pm_key_sadmin_signin":
            create_signin_log(params,response)
        elif params['key']=="pm_key_signout":
            create_signout_log(params,response)

    @staticmethod
    def create_super_admin_emp_log(params, response):
        admin_id = params['super_admin_id']
        emp_id = params['super_admin_emp_id']
        log_context = {}
        get_emp_info(log_context, admin_id, emp_id)
        params['log_context'] = log_context
        if params['key'] == "pm_key_super_admin_ticket_reply":
            create_super_admin_emp_ticket_reply_log(params, response)
        elif params['key']=="pm_key_signin":
            create_signin_log(params,response)
        elif params['key']=="pm_key_signout":
            create_signout_log(params,response)



    @staticmethod
    def create_admin_log(params, response):
        admin_id = params['admin_id']
        log_context = {}
        get_admin_info(log_context, admin_id)
        params['log_context'] = log_context
        if params['key'] == "pm_key_add_client":
            create_add_client_log(params, response)
        elif params['key'] == "pm_key_add_emp":
            create_add_emp_log(params, response)
        elif params['key'] == "pm_key_add_inv":
            create_add_inv_log(params, response)
        elif params['key'] == "pm_key_workflow_action":
            create_admin_task_transition_log(params, response)
        elif params['key'] == "pm_key_client_add_bns":
            user_id = params['user_id']
            get_client_info(log_context, admin_id, user_id)
            create_client_add_bns_log(params, response)
        elif params['key'] == "pm_key_c_edit_bns":
            user_id = params['user_id']
            get_client_info(log_context, admin_id, user_id)
            create_client_edit_bns_log(params, response)
        elif params['key'] == "pm_key_client_add_doc":
            user_id = params['user_id']
            get_client_info(log_context, admin_id, user_id)
            create_client_upload_files_log(params, response)
        elif params['key'] == "pm_key_update_client_status":
            user_id = params['user_id']
            get_client_info(log_context, admin_id, user_id)
            create_client_status_log(params, response)

        elif params['key'] == "pm_key_client_add_invoice":
            user_id = params['user_id']
            get_client_info(log_context, admin_id, user_id)
            create_client_add_invoice_log(params, response)

        elif params['key'] == "pm_key_admin_client_add_project":
            user_id = params['user_id']
            get_client_info(log_context, admin_id, user_id)
            create_client_add_project_log(params, response)
        
        elif params['key'] == "pm_key_edit_project":
            user_id = params['user_id']
            get_client_info(log_context, admin_id, user_id)
            create_client_edit_project_log(params, response)
        
        elif params['key'] == "pm_key_project_add_task":
            user_id = params['user_id']
            get_client_info(log_context, admin_id, user_id)
            create_client_project_add_task_log(params, response)
            
        elif params['key'] == "pm_key_project_edit_task":
            user_id = params['user_id']
            get_client_info(log_context, admin_id, user_id)
            create_client_project_edit_task_log(params, response)
        
        elif params['key'] == "pm_key_project_add_doc":
            user_id = params['user_id']
            get_client_info(log_context, admin_id, user_id)
            create_client_project_add_docs(params, response)
        
        elif params['key'] == "pm_key_project_select_doc_checkboxes":
            user_id = params['user_id']
            get_client_info(log_context, admin_id, user_id)
            create_client_project_select_doc_checkbox(params, response)

        elif params['key'] == "pm_key_client_add_todo_task":
            user_id = params['user_id']
            get_client_info(log_context, admin_id, user_id)
            create_client_todo_task_log(params, response)
        elif params['key'] == "pm_key_client_complete_todo_task":
            user_id = params['user_id']
            get_client_info(log_context, admin_id, user_id)
            create_client_todo_check_log(params, response)
        elif params['key'] == "pm_key_client_process_todo_task":
            user_id = params['user_id']
            get_client_info(log_context, admin_id, user_id)
            create_client_todo_process_log(params, response)
        elif params['key'] == "pm_key_send_client_msg":
            user_id = params['user_id']
            get_client_info(log_context, admin_id, user_id)
            create_client_msgs_log(params, response)
        elif params['key'] == "pm_key_send_team_msg":
            user_id = params['user_id']
            get_client_info(log_context, admin_id, user_id)
            create_team_msgs_log(params, response)
        elif params['key'] == "pm_key_select_client_doc_checkboxes":
            user_id = params['user_id']
            get_client_info(log_context, admin_id, user_id)
            create_client_doc_log(params, response)
        elif params['key'] == "pm_key_admin_team_actions":
            create_admin_team_action_log(params, response)
        elif params['key'] == "pm_key_admin_client_actions":
            create_admin_client_action_log(params, response)
        elif params['key'] == "pm_key_admin_access_settings":
            create_admin_profile_check_access_settings_log(params, response)
        # elif params['key'] == "pm_key_admin_profile_uncheck_access_settings":
        #     create_admin_profile_uncheck_access_settings_log(params, response)
        elif params['key'] == "pm_key_admin_add_templates":
            create_admin_profile_templates_log(params, response)
        elif params['key']=="pm_key_signin":
            create_signin_log(params,response)
        elif params['key']=="pm_key_signout":
            create_signout_log(params,response)
        elif params['key'] == "pm_key_admin_client_notes":
            user_id = params['user_id']
            get_client_info(log_context, admin_id, user_id)
            create_client_dashboard_notes_process_log(params,response)

        elif params['key']=="pm_key_client_add_doc_file_actions":
            user_id = params['user_id']
            get_client_info(log_context, admin_id, user_id)
            create_delete_file_log(params,response)

        elif params['key'] == 'pm_key_add_ticket':
            create_add_ticket_log(params, response)

        elif params['key'] == 'pm_key_admin_ticket_reply':
            create_admin_ticket_reply_log(params, response)

        elif params['key'] == 'pm_key_close_ticket':
            create_admin_ticket_close_log(params, response)



    @staticmethod
    def create_emp_log(params, response):
        admin_id = params['admin_id']
        emp_id = params['emp_id']
        log_context = {}
        get_emp_info(log_context, admin_id, emp_id)

        params['log_context'] = log_context
        if params['key'] == "pm_key_workflow_action":
            create_emp_task_transition_log(params, response)
        elif params['key'] == "pm_key_client_add_bns":
            user_id = params['user_id']
            get_client_info(log_context, admin_id, user_id)
            create_client_add_bns_log(params, response)
        elif params['key'] == "pm_key_c_edit_bns":
            user_id = params['user_id']
            get_client_info(log_context, admin_id, user_id)
            create_client_edit_bns_log(params, response)
        elif params['key'] == "pm_key_client_add_doc":
            user_id = params['user_id']
            get_client_info(log_context, admin_id, user_id)
            create_client_upload_files_log(params, response)
        elif params['key'] == "pm_key_update_client_status":
            user_id = params['user_id']
            get_client_info(log_context, admin_id, user_id)
            create_client_status_log(params, response)
        elif params['key'] == "pm_key_send_client_msg":
            user_id = params['user_id']
            get_client_info(log_context, admin_id, user_id)
            create_client_msgs_log(params, response)
        elif params['key'] == "pm_key_send_team_msg":
            user_id = params['user_id']
            get_client_info(log_context, admin_id, user_id)
            create_team_msgs_log(params, response)
        elif params['key'] == "pm_key_client_add_todo_task":
            user_id = params['user_id']
            get_client_info(log_context, admin_id, user_id)
            create_client_todo_task_log(params, response)
        elif params['key'] == "pm_key_client_complete_todo_task":
            user_id = params['user_id']
            get_client_info(log_context, admin_id, user_id)
            create_client_todo_check_log(params, response)
        elif params['key'] == "pm_key_client_process_todo_task":
            user_id = params['user_id']
            get_client_info(log_context, admin_id, user_id)
            create_client_todo_process_log(params, response)
        elif params['key'] == "pm_key_select_client_doc_checkboxes":
            user_id = params['user_id']
            get_client_info(log_context, admin_id, user_id)
            create_client_doc_log(params, response)
        elif params['key']=="pm_key_signin":
            create_signin_log(params,response)
        elif params['key']=="pm_key_signout":
            create_signout_log(params,response)
        elif params['key'] == "pm_key_admin_client_notes":
            user_id = params['emp_id']
            get_client_info(log_context, admin_id, user_id)
            create_client_dashboard_notes_process_log(params,response)

        elif params['key'] == "pm_key_edit_project":
            user_id = params['user_id']
            get_client_info(log_context, admin_id, user_id)
            create_client_edit_project_log(params, response)
        
        elif params['key'] == "pm_key_project_add_task":
            user_id = params['user_id']
            get_client_info(log_context, admin_id, user_id)
            create_client_project_add_task_log(params, response)
        
        elif params['key'] == "pm_key_project_edit_task":
            user_id = params['user_id']
            get_client_info(log_context, admin_id, user_id)
            create_client_project_edit_task_log(params, response)
        
        elif params['key'] == "pm_key_project_add_doc":
            user_id = params['user_id']
            get_client_info(log_context, admin_id, user_id)
            create_client_project_add_docs(params, response)
        
        elif params['key'] == "pm_key_project_select_doc_checkboxes":
            user_id = params['user_id']
            get_client_info(log_context, admin_id, user_id)
            create_client_project_select_doc_checkbox(params, response)
        

    @staticmethod
    def create_client_log(params, response):
        admin_id = params['admin_id']
        user_id = params['user_id']
        log_context = {}
        get_client_info(log_context, admin_id, user_id)
        params['log_context'] = log_context
        if params['key'] == "pm_key_client_add_bns":
            create_client_add_bns_log(params, response)
        elif params['key'] == "pm_key_c_edit_bns":
            create_client_edit_bns_log(params, response)
        elif params['key'] == "pm_key_client_add_doc":
            create_client_upload_files_log(params, response)
        elif params['key'] == "pm_key_send_client_msg":
            create_client_msgs_log(params, response)
        elif params['key'] == "pm_key_client_complete_todo_task":
            create_client_todo_check_log(params, response)
        elif params['key']=="pm_key_signin":
            create_signin_log(params,response)
        elif params['key']=="pm_key_signout":
            create_signout_log(params,response)
        elif params['key'] == "pm_key_admin_client_notes":
            create_client_dashboard_notes_process_log(params,response)
        
        elif params['key'] == "pm_key_project_add_doc":
            create_client_project_add_docs(params, response)


    def create_admin_signup_log(params, response):
        log_context = {}
        params['log_context'] = log_context
        if params['key'] == "pm_key_cpa_signup":
            create_add_admin_log(params, response)

