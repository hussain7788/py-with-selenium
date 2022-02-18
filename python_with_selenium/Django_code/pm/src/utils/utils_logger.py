import logging
import pdb
import inspect

pmLogger = logging.getLogger("pmLogger")
pmPrioLogger = logging.getLogger("pmPrioLogger")


def pmLoggerLog(context, extra_dict, level, msg, *args, **kwargs):
    if args != list():
        for item in args:
            msg += str(item)
    try:
        prio = kwargs['prio']
    except KeyError:
        prio = False

    callerFrameRecord = inspect.stack()[3]
    frame = callerFrameRecord[0]
    info = inspect.getframeinfo(frame)
    fname = info.filename.split("pm")
    extra_dict['fname'] = fname[1]
    extra_dict['linenum'] = info.lineno

    if 'admin_obj' in context:
        extra_dict['adminName'] = context['admin_obj'].admin_full_name
    else:
        extra_dict['adminName'] = ""

    if 'emp_obj' in context:
        extra_dict['empName'] = context['emp_obj'].emp_full_name
    else:
        extra_dict['empName'] = ""

    if 'user_obj' in context:
        extra_dict['clientName'] = context['user_obj'].user_full_name
    else:
        extra_dict['clientName'] = ""

    if level == 1:
        pmLogger.critical(msg, extra=extra_dict)
        if prio == True:
            pmPrioLogger.critical(msg, extra=extra_dict)
    elif level == 2:
        pmLogger.warning(msg, extra=extra_dict)
        if prio == True:
            pmPrioLogger.warning(msg, extra=extra_dict)
    elif level == 3:
        pmLogger.error(msg, extra=extra_dict)
        if prio == True:
            pmPrioLogger.error(msg, extra=extra_dict)
    elif level == 4:
        pmLogger.info(msg, extra=extra_dict)
        if prio == True:
            pmPrioLogger.info(msg, extra=extra_dict)
    elif level == 5:
        pmLogger.debug(msg, extra=extra_dict)
        if prio == True:
            pmPrioLogger.debug(msg, extra=extra_dict)


def pmGenericLog(level, msg, *args, **kwargs):
    context = dict()
    extra_dict = dict()
    extra_dict['tag'] = "Generic"
    pmLoggerLog(context, extra_dict, level, msg, *args, **kwargs)


def pmGenericLogCritical(msg, *args, **kwargs):
    pmGenericLog(1, msg, *args, **kwargs)


def pmGenericLogWarning(msg, *args, **kwargs):
    pmGenericLog(2, msg, *args, **kwargs)


def pmGenericLogError(msg, *args, **kwargs):
    pmGenericLog(3, msg, *args, **kwargs)


def pmGenericLogInfo(msg, *args, **kwargs):
    pmGenericLog(4, msg, *args, **kwargs)


def pmGenericLogDebug(msg, *args, **kwargs):
    pmGenericLog(5, msg, *args, **kwargs)


def pmAdminLog(context, level, msg, *args, **kwargs):
    extra_dict = dict()
    extra_dict['tag'] = "Admin"
    pmLoggerLog(context, extra_dict, level, msg, *args, **kwargs)


def pmAdminLogCritical(context, msg, *args, **kwargs):
    pmAdminLog(context, 1, msg, *args, **kwargs)


def pmAdminLogWarning(context, msg, *args, **kwargs):
    pmAdminLog(context, 2, msg, *args, **kwargs)


def pmAdminLogError(context, msg, *args, **kwargs):
    pmAdminLog(context, 3, msg, *args, **kwargs)


def pmAdminLogInfo(context, msg, *args, **kwargs):
    pmAdminLog(context, 4, msg, *args, **kwargs)


def pmAdminLogDebug(context, msg, *args, **kwargs):
    pmAdminLog(context, 5, msg, *args, **kwargs)


def pmEmpLog(context, level, msg, *args, **kwargs):
    extra_dict = dict()
    extra_dict['tag'] = "Emp"
    pmLoggerLog(context, extra_dict, level, msg, *args, **kwargs)


def pmEmpLogCritical(context, msg, *args, **kwargs):
    pmEmpLog(context, 1, msg, *args, **kwargs)


def pmEmpLogWarning(context, msg, *args, **kwargs):
    pmEmpLog(context, 2, msg, *args, **kwargs)


def pmEmpLogError(context, msg, *args, **kwargs):
    pmEmpLog(context, 3, msg, *args, **kwargs)


def pmEmpLogInfo(context, msg, *args, **kwargs):
    pmEmpLog(context, 4, msg, *args, **kwargs)


def pmEmpLogDebug(context, msg, *args, **kwargs):
    pmEmpLog(context, 5, msg, *args, **kwargs)


def pmClientLog(context, level, msg, *args, **kwargs):
    extra_dict = dict()
    extra_dict['tag'] = "Client"
    pmLoggerLog(context, extra_dict, level, msg, *args, **kwargs)


def pmClientLogCritical(context, msg, *args, **kwargs):
    pmClientLog(context, 1, msg, *args, **kwargs)


def pmClientLogWarning(context, msg, *args, **kwargs):
    pmClientLog(context, 2, msg, *args, **kwargs)


def pmClientLogError(context, msg, *args, **kwargs):
    pmClientLog(context, 3, msg, *args, **kwargs)


def pmClientLogInfo(context, msg, *args, **kwargs):
    pmClientLog(context, 4, msg, *args, **kwargs)


def pmClientLogDebug(context, msg, *args, **kwargs):
    pmClientLog(context, 5, msg, *args, **kwargs)
