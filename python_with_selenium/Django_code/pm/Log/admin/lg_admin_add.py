from pm.src.utils.utils_logger import *
from pm.log.common.lg_lookup import *


def create_add_admin_log(params, response):
    log_context = params['log_context']
    first_name = params['f_name']
    last_name = params['l_name']
    company_name = params['company_name']
    email = params['username']
    try:
        response['fail']
    except KeyError:
        pmAdminLogInfo(log_context, "\"{'pm_key_cpa_signup':{" +
                       f"'first_name':{first_name},'last_name':'{last_name}','company_name':{company_name},'email':'{email}'" + "}}\"", prio=True)
    else:
        pmAdminLogWarning(
            log_context, "\"{pm_key_cpa_signup:{" + f"'first_name':{first_name},'last_name':'{last_name}','company_name':{company_name},'email':'{email}','warning':'{response['fail']}'" + "}}\"", prio=True)


def create_add_client_log(params, response):
    log_context = params['log_context']
    first_name = params['f_name']
    last_name = params['l_name']
    email = params['email']
    phone = params['phone']
    try:
        response['fail']
    except KeyError:
        pmAdminLogInfo(log_context, "\"{'pm_key_add_client':{" +
                       f"'first_name':{first_name},'last_name':'{last_name}','email':'{email}','phone':'{phone}'" + "}}\"", prio=True)
    else:
        pmAdminLogWarning(log_context, "\"{'pm_key_add_client':{" +
                          f"'first_name':{first_name},'last_name':'{last_name}','email':'{email}','phone':'{phone}','warning':'{response['fail']}'" + "}}\"", prio=False)


def create_add_emp_log(params, response):
    log_context = params['log_context']
    first_name = params['f_name']
    last_name = params['l_name']
    email = params['email']
    emp_type = get_emp_type(params['emp_type'])
    mgr_name = params['mgr_name']
    try:
        response['fail']
    except KeyError:
        pmAdminLogInfo(log_context, "\"{'pm_key_add_emp':{" +
                       f"'first_name':{first_name},'last_name':'{last_name}','email':'{email}','emp_type':'{emp_type}','mgr_name':'{mgr_name}'" + "}}\"", prio=True)
    else:
        pmAdminLogWarning(
            log_context, "\"{'pm_key_add_emp':{" + f"'first_name':{first_name},'last_name':'{last_name}','email':'{email}','emp_type':'{emp_type}','mgr_name':'{mgr_name}','warning':'{response['fail']}'" + "}}\"", prio=False)


def create_admin_team_action_log(params, response):
    log_context = params['log_context']
    l_emails = params['l_emails']
    action = params['action']
    try:
        response['fail']
    except KeyError:
        pmAdminLogInfo(log_context, "\"{'pm_key_admin_team_actions':{" +
                       f"'l_emails':{l_emails},'action':'{action}'" + "}}\"", prio=True)
    else:
        pmAdminLogWarning(log_context, "\"{pm_key_admin_team_actions:{" +
                          f"'l_emails':{l_emails},'action':'{action}','warning':'{response['fail']}'" + "}}\"", prio=True)


def create_admin_client_action_log(params, response):
    log_context = params['log_context']
    l_emails = params['l_emails']
    action = params['action']
    try:
        response['fail']
    except KeyError:
        pmAdminLogInfo(log_context, "\"{'pm_key_admin_client_actions':{" +
                       f"'l_emails':{l_emails},'action':'{action}'" + "}}\"", prio=True)
    else:
        pmAdminLogWarning(log_context, "\"{pm_key_admin_client_actions:{" +
                          f"'l_emails':{l_emails},'action':'{action}','warning':'{response['fail']}'" + "}}\"", prio=True)


def create_add_ticket_log(params, response):
    log_context = params['log_context']
    msg = params["message"]
    subject = params['subject']
    if params.get('l_files') != None:
        l_files = params['l_files']
        log_message = str(
            "\"{'pm_key_add_ticket':{" + f"'msg':{msg},'subject':'{subject}','l_files':{l_files}" + "}}\"")
    else:
        log_message = str(
            "\"{'pm_key_add_ticket':{" + f"'msg':{msg},'subject':'{subject}'" + "}}\"")

    pmAdminLogInfo(log_context, log_message, prio=False)


def create_admin_ticket_reply_log(params, response):
    log_context = params['log_context']
    ticket_num = params['ticket_num']
    msg = params["message"]
    if params.get('l_files') != None:
        l_files = params['l_files']
        log_message = str("\"{'pm_key_admin_ticket_reply':{" +
                          f"'msg':{msg},'ticket_num':'{ticket_num}','l_files':{l_files}" + "}}\"")
    else:
        log_message = str("\"{'pm_key_admin_ticket_reply':{" +
                          f"'msg':{msg},'ticket_num':'{ticket_num}'" + "}}\"")

    pmAdminLogInfo(log_context, log_message, prio=False)


def create_admin_ticket_close_log(params, response):
    log_context = params['log_context']
    ticket_num = params['ticket_num']
    log_message = str(
        "\"{'pm_key_close_ticket':{" + f"'ticket_num':'{ticket_num}'" + "}}\"")
    pmAdminLogInfo(log_context, log_message, prio=False)


def create_super_admin_ticket_reply_log(params, response):
    log_context = params['log_context']
    ticket_num = params['ticket_num']
    msg = params["message"]
    if params.get('l_files') != None:
        l_files = params['l_files']
        log_message = str("\"{'pm_key_super_admin_ticket_reply':{" +
                          f"'msg':{msg},'ticket_num':'{ticket_num}','l_files':{l_files}" + "}}\"")
    else:
        log_message = str("\"{'pm_key_super_admin_ticket_reply':{" +
                          f"'msg':{msg},'ticket_num':'{ticket_num}'" + "}}\"")

    pmAdminLogInfo(log_context, log_message, prio=False)


def create_super_admin_emp_ticket_reply_log(params, response):
    log_context = params['log_context']
    ticket_num = params['ticket_num']
    msg = params["message"]

    if params.get('l_files') != None:
        l_files = params['l_files']
        log_message = str("\"{'pm_key_super_admin_ticket_reply':{" +
                          f"'msg':{msg},'ticket_num':'{ticket_num}','l_files':{l_files}" + "}}\"")
    else:
        log_message = str("\"{'pm_key_super_admin_ticket_reply':{" +
                          f"'msg':{msg},'ticket_num':'{ticket_num}'" + "}}\"")

    pmAdminLogInfo(log_context, log_message, prio=False)
##################################################


def create_admin_profile_check_access_settings_log(params, response):
    log_context = params['log_context']
    l_cl_ids_check = params['l_cl_ids_check']

    log_message = str("\"{'pm_key_admin_access_settings':{" +
                      f"'l_cl_ids_check':{l_cl_ids_check}" + "}}\"")
    pmAdminLogInfo(log_context, log_message, prio=False)

# def create_admin_profile_uncheck_access_settings_log(params, response):
#     log_context = params['log_context']
#     l_cl_ids_uncheck = params['l_cl_ids_uncheck']

#     log_message = str("\"{'pm_key_admin_profile_uncheck_access_settings':{" + f"'l_cl_ids_uncheck':{l_cl_ids_uncheck}" + "}}\"")
#     pmAdminLogInfo(log_context, log_message, prio=False)


def create_admin_profile_templates_log(params, response):
    log_context = params['log_context']
    if params['cat'] == 1:
        category_name = "Individual"
        tab_name = "personalTab"
    else:
        category_name = "Business"
        tab_name = "businessTab"

    l_files = params['l_files']
    try:
        response['fail']
    except KeyError:
        log_message = str("\"{'pm_key_admin_add_templates':{" +
                          f"'category_name':{category_name},'tab_name':'{tab_name}','l_files':{l_files}" + "}}\"")
    else:
        log_message = str("\"{'pm_key_admin_add_templates':{" +
                          f"'category_name':{category_name},'tab_name':'{tab_name}','l_files':{l_files},'warning':'{response['fail']}'" + "}}\"")
    pmAdminLogInfo(log_context, log_message, prio=False)
