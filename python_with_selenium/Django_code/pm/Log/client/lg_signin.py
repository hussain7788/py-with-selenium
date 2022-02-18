
from pm.src.utils.utils_logger import *
from pm.log.common.lg_lookup import *


def write_log(context, log_context, log_message, priority):
    if context == "admin":
        pmAdminLogInfo(log_context, log_message, prio=priority)
    elif context == "super_admin":
        pmAdminLogInfo(log_context, log_message, prio=priority)
    elif context == "super_admin_emp":
        pmEmpLogInfo(log_context, log_message, prio=priority)
    elif context == "emp":
        pmEmpLogInfo(log_context, log_message, prio=priority)
    elif context == "client":
        pmClientLogInfo(log_context, log_message, prio=priority)


def create_signin_log(params, response):
    log_context = params['context']
    email = params['email_id']
    name = params['name']
    log_message = str(
        "\"{"+f"{params['key']}" + ":{" + f"'name':{name},'email':'{email}'" + "}}\"")
    priority = True
    write_log(params['context'], log_context, log_message, priority)


def create_signout_log(params, response):
    log_context = params['context']
    email = params['email_id']
    name = params['name']
    log_message = str(
        "\"{"+f"{params['key']}" + ":{" + f"'name':{name},'email':'{email}'" + "}}\"")
    priority = True
    write_log(params['context'], log_context, log_message, priority)
