from pm.src.utils.utils_logger import *
from pm.log.common.lg_lookup import *


def create_client_add_bns_log(params, response):
    log_context = params['log_context']
    bns_name = params['bns_name']
    bns_type = get_bns_type(params['bns_type'])
    bns_inc_state = params['bns_incorp_state']
    bns_inc_date = params['bns_incorp_date']
    if params['is_bk'] == True:
        bk_checkbox = True
        bk_frequency = get_bns_frequency(params['bk_sched'])
    else:
        bk_checkbox = False
        bk_frequency = 0
    if params['is_pr'] == True:
        pr_checkbox = True
        pr_frequency = get_bns_frequency(params['pr_sched'])
    else:
        pr_checkbox = False
        pr_frequency = 0
    if params['is_st'] == True:
        st_checkbox = True
        st_frequency = get_bns_frequency(params['st_sched'])
    else:
        st_checkbox = False
        st_frequency = 0
    if params['is_tp'] == True:
        tp_checkbox = True
        tp_frequency = get_bns_frequency(params['tp_sched'])
    else:
        tp_checkbox = False
        tp_frequency = 0
    log_message = str("\"{'pm_key_client_add_bns':{" + f"'bns_name':{bns_name},'bns_type':'{bns_type}','bns_inc_state':{bns_inc_state},'bns_inc_date':{bns_inc_date},'bk_checkbox':{bk_checkbox},'bk_frequency':{bk_frequency},'pr_checkbox':'{pr_checkbox}','pr_frequency':{pr_frequency},'st_checkbox':'{st_checkbox}','st_frequency':{st_frequency},'tp_checkbox':{tp_checkbox},'tp_frequency':{tp_frequency}" + "}}\"")
    priority = True
    write_log(params['context'], log_context, log_message, priority)


def write_log(context, log_context, log_message, priority):
    if context == "admin":
        pmAdminLogInfo(log_context, log_message, prio=priority)
    elif context == "emp":
        pmEmpLogInfo(log_context, log_message, prio=priority)
    elif context == "client":
        pmClientLogInfo(log_context, log_message, prio=priority)


def create_client_edit_bns_log(params, response):
    log_context = params['log_context']
    bns_name = params['bns_name']
    business_type = get_bns_type(params['bns_type'])
    business_inco_date = params['bns_incorp_date']
    bns_inc_state = params['bns_incorp_state']
    bk_frequency_value = get_bns_frequency(params['bk_sched'])
    pr_frequency_value = get_bns_frequency(params['pr_sched'])
    st_frequency_value = get_bns_frequency(params['st_sched'])
    tp_frequency_value = get_bns_frequency(params['tp_sched'])
    m_states_value = params['extra_states_raw']

    log_message = str("\"{'pm_key_c_edit_bns':{"+f"'bns_name':{bns_name},'business_type':'{business_type}','bns_inc_state':{bns_inc_state},'business_inco_date':{business_inco_date},'bk_frequency_value':'{bk_frequency_value}','pr_frequency_value':{pr_frequency_value},'st_frequency_value':{st_frequency_value},'tp_frequency_value':{tp_frequency_value},'m_states_value':{m_states_value}" + "}}\"")
    priority = True
    write_log(params['context'], log_context, log_message, priority)


def create_client_upload_files_log(params, response):
    log_context = params['log_context']
    if params['cat'] == 1:
        tab_name = "personalTab"
        sub_tab = params['sub_tab']
        bns_name = None
    else:
        tab_name = "businessTab"
        sub_tab = params['sub_tab']
        bns_name = params['bns_name']
    client_login_access = params['is_user']
    document_source = get_upload_doc_source(int(params['access']))
    tax_year = params['year']
    l_files = list()
    for file in params['l_files']:
        l_files.append(
            {"file_name": file[0],  "file_type": get_upload_file_type(int(file[1]))})

        try:
            response['fail']
        except KeyError:
            log_message = str("\"{'pm_key_client_add_doc':{" + f"'tab_name':{tab_name},'sub_tab':'{sub_tab}','client_login_access':{client_login_access},'bns_name':{bns_name},'document_source':'{document_source}','tax_year':'{tax_year}','l_files':{l_files}" + "}}\"")
        else:
            log_message = str(
                "\"{'pm_key_client_add_doc':{" + f"'tab_name':{tab_name},'sub_tab':'{sub_tab}','client_login_access':{client_login_access},'bns_name':{bns_name},'document_source':'{document_source}','tax_year':'{tax_year}','l_files':{l_files},'warning':'{response['fail']}'" + "}}\"")
        priority = True
        write_log(params['context'], log_context, log_message, priority)


def create_client_msgs_log(params, response):
    log_context = params['log_context']
    client_msg = params['message']
    log_message = str(
        "\"{'pm_key_send_client_msg':{" + f"'client_msg':'{client_msg}'" + "}}\"")
    priority = True
    write_log(params['context'], log_context, log_message, priority)


def create_team_msgs_log(params, response):
    log_context = params['log_context']
    team_msg = params['message']
    log_message = str(
        "\"{'pm_key_send_team_msg':{" + f"'team_msg':'{team_msg}'" + "}}\"")
    priority = True
    write_log(params['context'], log_context, log_message, priority)


def create_client_todo_task_log(params, response):
    log_context = params['log_context']
    todoDueDate = params['duedate']
    todoTask = params['task']
    log_message = str("\"{'pm_key_client_add_todo_task':{" +
                      f"'todoDueDate':'{todoDueDate}','todoTask':'{todoTask}'" + "}}\"")
    priority = True
    write_log(params['context'], log_context, log_message, priority)


def create_client_todo_check_log(params, response):
    log_context = params['log_context']
    l_todo_task_names = params['l_todo_task_names']
    log_message = str("\"{'pm_key_client_complete_todo_task':{" +
                      f"'l_todo_task_names':'{l_todo_task_names}'" + "}}\"")
    priority = True
    write_log(params['context'], log_context, log_message, priority)


def create_client_todo_process_log(params, response):
    log_context = params['log_context']
    l_todo_task_names = params['l_todo_task_names']
    log_message = str("\"{'pm_key_client_process_todo_task':{" +
                      f"'l_todo_task_names':'{l_todo_task_names}'" + "}}\"")
    priority = True
    write_log(params['context'], log_context, log_message, priority)


def create_client_doc_log(params, response):
    log_context = params['log_context']
    if params['cat'] == 1:
        tab_name = "personalTab"
    else:
        tab_name = "businessTab"
    sub_tab = "fromClient"
    tax_year = params['tax_year']
    l_file_names = params['l_file_names']
    if params['context'] == "admin":
        log_message = str("\"{'pm_key_select_client_doc_checkboxes':{" +
                          f"'tab_name':'{tab_name}','sub_tab':'{sub_tab}','tax_year':'{tax_year}','l_file_names':'{l_file_names}'" + "}}\"")
    elif params['context'] == "emp":
        if params['key'] == "pm_key_select_client_doc_checkboxes":
            log_message = str("\"{'pm_key_select_client_doc_checkboxes':{" +
                              f"'tab_name':'{tab_name}','sub_tab':'{sub_tab}','tax_year':'{tax_year}','l_file_names':'{l_file_names}'" + "}}\"")
        elif params['key'] == "pm_key_select_client_doc_checkboxes":
            log_message = str("\"{'pm_key_select_client_doc_checkboxes':{" +
                              f"'tab_name':'{tab_name}','sub_tab':'{sub_tab}','tax_year':'{tax_year}','l_file_names':'{l_file_names}'" + "}}\"")

    log_message = str("\"{'pm_key_select_client_doc_checkboxes':{" +
                      f"'tab_name':'{tab_name}','sub_tab':'{sub_tab}','tax_year':'{tax_year}','l_file_names':'{l_file_names}'" + "}}\"")

    priority = True
    write_log(params['context'], log_context, log_message, priority)


def create_client_price_est_log(params, response):
    log_context = params['log_context']
    if params['cat'] == 1:
        tab_name = "PersonalTab"
        bns_name = None
    else:
        tab_name = "BusinessTab"
        bns_name = params['bns_name']
    year = params['year']
    estimated_pr = None
    log_message = str("\"{'pm_key_admin_client_update_price_est':{" +
                      f"'tab_name':'{tab_name}','year':'{year}','bns_name':'{bns_name}','estimated_pr':'{estimated_pr}'" + "}}\"")
    priority = True
    write_log(params['context'], log_context, log_message, priority)


def create_client_status_log(params, response):
    log_context = params['log_context']
    try:
        params['cat_id']
    except KeyError:
        pass
    else:
        if params['cat_id'] == 1:
            tab_name = "personalTab"
            l_bns_names = None
        else:
            tab_name = "businessTab"
            l_bns_names = params['l_bns_names']

        emp_status_access = params['emp_status_access']
        mgr_status_access = params['mgr_status_access']
        l_mgr_names = params['l_mgr_names']
        l_emp_names = params['l_emp_names']
        l_years = params['l_years']
        # l_status_names = get_filter_status(int(params['l_status_names']))
        l_status_names = params['l_status_names']

        log_message = str("\"{'pm_key_update_client_status':{" + f"'tab_name':'{tab_name}','emp_status_access':'{emp_status_access}','mgr_status_access':'{mgr_status_access}','l_mgr_names':'{l_mgr_names}','l_emp_names':'{l_emp_names}','l_years':'{l_years}','l_status_names':'{l_status_names}','l_bns_names':'{l_bns_names}'" + "}}\"")
        priority = True
        write_log(params['context'], log_context, log_message, priority)


def create_client_dashboard_notes_process_log(params, response):
    log_context = params['log_context']
    notes = params['notes']

    log_message = str(
        "\"{'pm_key_admin_client_notes':{" + f"'notes':'{notes}'" + "}}\"")
    priority = True
    write_log(params['context'], log_context, log_message, priority)


def create_delete_file_log(params, response):
    log_context = params['log_context']
    c_name = params['cat']
    f_name = params["file_name"]
    f_year = params['tax_year']
    t_name = params['t_name']
    sub_name = params['st_name']
    log_message = str("\"{'pm_key_client_add_doc_file_actions':{" +
                      f"'file name':{f_name},'file year':{f_year},'file category name ':'{c_name}','tap_name ':'{t_name}','sub_tap_name ':'{sub_name}'" + "}}\"")
    pmAdminLogInfo(log_context, log_message, prio=False)


def create_client_add_invoice_log(params, response):
    log_context = params['log_context']
    invoice_date = params['invoice_date']
    due_date = params["due_date"]
    description = params['description']
    quantity = params['quantity']
    price = params['price']
    sales_tax = params['sales_tax']
    notes = params['notes']
    payment_memo = params['payment_memo']
    log_message = str("\"{'pm_key_client_add_invoice':{" + f"'invoice_date':{invoice_date},'due_date':{due_date},'description':'{description}','quantity':'{quantity}','price':'{price}','sales_tax':'{sales_tax}','notes':'{notes}','payment_memo':'{payment_memo}'" + "}}\"")
    pmAdminLogInfo(log_context, log_message, prio=False)


def create_client_add_project_log(params, response):
    log_context = params['log_context']
    project_name = params['project_name']
    project_type = params["project_type"]
    try:
        bns_name = params['bns_name']
        emp_name = params['emp_name']
    except KeyError:
        bns_name = False
        emp_name = False

    service_name = params['service_name']
    if service_name != False:
        frequency = False
    else:
        frequency = params['frequency']

    if params['month'] != False:
        month = get_filter_project_month(int(params['month']))
    else:
        month = params['month']
    day = params['day']
    try:
        response['fail']
    except KeyError:
        log_message = str("\"{'pm_key_admin_client_add_project':{" +
                          f"'project_name':{project_name},'project_type':{project_type},'bns_name':'{bns_name}','emp_name':'{emp_name}','service_name':'{service_name}','frequency':'{frequency}','month':'{month}','day':'{day}'" + "}}\"")
    else:
        log_message = str("\"{'pm_key_admin_client_add_project':{" +
                          f"'project_name':{project_name},'project_type':{project_type},'bns_name':'{bns_name}','emp_name':'{emp_name}','service_name':'{service_name}','frequency':'{frequency}','month':'{month}','day':'{day}','warning':'{response['fail']}'" + "}}\"")
    pmAdminLogInfo(log_context, log_message, prio=False)


def create_client_edit_project_log(params, response):
    log_context = params['log_context']
    project_type = params['project_type']
    project_name = params['project_name']
    bns_name = params['bns_name']
    status_name = params['status_name']
    due_date = params['due_date']
    try:
        emp_name = params['emp_name']
    except KeyError:
        emp_name = False
    frequency = False
    day = False
    month = False

    try:
        emp_name = params['emp_name']
    except KeyError:
        emp_name = False

    if project_type == "project":
        log_message = str(
            "\"{'pm_key_edit_project':{" + f"'project_type':{project_type},'project_name':{project_name},'bns_name':'{bns_name}','emp_name':'{emp_name}','status_name':'{status_name}','due_date':'{due_date}'" + "}}\"")
    elif project_type == "project_templates":
        log_message = str("\"{'pm_key_edit_project':{" + f"'project_type':{project_type},'project_name':{project_name},'bns_name':'{bns_name}','emp_name':'{emp_name}', 'frequency':'{frequency}','month':'{month}','day':'{day}'" + "}}\"")
    priority = False
    write_log(params['context'], log_context, log_message, priority)


def create_client_project_add_task_log(params, response):
    log_context = params['log_context']
    task_name = params['task_name']
    try:
        emp_name = params['emp_name']
    except KeyError:
        emp_name = False

    log_message = str("\"{'pm_key_project_add_task':{" +
                      f"'task_name':{task_name},'emp_name':'{emp_name}'" + "}}\"")
    priority = False
    write_log(params['context'], log_context, log_message, priority)


def create_client_project_edit_task_log(params, response):
    log_context = params['log_context']
    task_name = params['task_name']
    status_name = params['status_name']
    percent = params['percent']
    try:
        emp_name = params['emp_name']
    except KeyError:
        emp_name = False
    notes = params['notes']

    log_message = str("\"{'pm_key_project_edit_task':{" +
                      f"'task_name':'{task_name}','emp_name':'{emp_name}','status_name':'{status_name}','percent':'{percent}', 'notes':'{notes}'" + "}}\"")
    priority = False
    write_log(params['context'], log_context, log_message, priority)


def create_client_project_add_docs(params, response):
    log_context = params['log_context']
    document_source = params['document_source']
    l_files = params['l_files']

    log_message = str("\"{'pm_key_project_add_doc':{" +
                      f"'document_source':'{document_source}','l_files':'{l_files}'" + "}}\"")
    priority = False
    write_log(params['context'], log_context, log_message, priority)


def create_client_project_select_doc_checkbox(params, response):
    log_context = params['log_context']
    file_name = params['file_name']

    log_message = str(
        "\"{'pm_key_project_select_doc_checkboxes':{" + f"'file_name':'{file_name}'" + "}}\"")
    priority = False
    write_log(params['context'], log_context, log_message, priority)
