from pm.models import (
    Admin, AdminConfig, UserTracking, Messages, Notifications,
    TodoList, User, get_status_obj_from_internal_name,
    TaskTracking, Alert
)

from pm.src.api.api_client_dashboard.api_client_dashboard_utils.serializers import (
    UserTrackingPersonalSerializer, UserTrackingBusinessSerializer, MessagesSerializer,
    TodoSerializer, TaskTrackingSerializer, AlertSerializer
)

from pm.src.api.api_global_config.channels import update_notification_channel
from pm.src.utils.utils_common import check_user_exist, is_string_empty, is_email_invalid
from pm.src.utils.utils_email import send_client_referral_email

from intelws_core.messages.messages import message_create, message_fetch
from intelws_core.todo.todo import todo_create, todo_fetch
from intelws_core.alerts.alerts import fetch_alerts

from django.db.models import F
from django.utils import timezone
from django.utils.timezone import make_aware, get_current_timezone, get_default_timezone

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from pm.log.lg_create import create_log

from datetime import datetime

import pdb


def _client_dashboard_client_referral(request):
    if request.session['role'] == "user":
        admin_id = request.session['admin_id']
        user_id = request.session['user_id']
        email = request.POST.get("email", False)
        d_error = dict()
        is_error = False
        if email == False:
            d_error['email'] = "Email is a required field"
            is_error = True
        if is_error:
            return 412, {"query_response": {"fail_response": d_error}}
        if is_string_empty(email):
            d_error['email'] = "Email is a required field"
            is_error = True
        if is_error:
            return 412, {"query_response": {"fail_response": d_error}}
        if is_email_invalid(email):
            d_error['email'] = "Please enter a valid email address"
            is_error = True
        if is_error:
            return 412, {"query_response": {"fail_response": d_error}}
        if check_user_exist(email):
            d_error['email'] = "This email is already registered"
            is_error = True
        if is_error:
            return 412, {"query_response": {"fail_response": d_error}}
        admin_obj = Admin.objects.get(id=admin_id)
        try:
            user_obj = User.objects.get(user_admin_id=admin_id, id=user_id)
        except User.DoesNotExist:
            pass
        else:
            params = dict()
            response = dict()
            params['admin_obj'] = admin_obj
            params['user_obj'] = user_obj
            params['email'] = email
            send_client_referral_email(params, response)
            return 200, {"query_response": {"success": ["Referall sent!"]}}
    return 401, {}

# Client Info


def _client_dashboard_client_info(request):
    admin_id = request.session['admin_id']
    if request.session['role'] == "user":
        user_id = request.session['user_id']
    else:
        user_id = request.query_params['user_id']
    user_obj = User.objects.get(user_admin_id=admin_id, id=user_id)
    return {"name": user_obj.user_full_name, "email": user_obj.user_email,
            "phone_num": str(user_obj.user_phone_num)}

# Active Engagements


def _client_dashboard_active_engagements(request):
    admin_id = request.session['admin_id']
    if request.session['role'] == "user":
        user_id = request.session['user_id']
    else:

        user_id = request.query_params['user_id']
    cat = int(request.query_params['cat'])
    closed_state_id = get_status_obj_from_internal_name(admin_id, "closed")[
        "id"]
    if cat == 0 or cat == 1:
        user_tracking = UserTracking.objects.order_by('-ut_year').filter(
            ut_admin_id=admin_id, ut_user_id=user_id).exclude(ut_current_status=closed_state_id)
    else:
        task_tracking = TaskTracking.objects.filter(tt_admin_id=admin_id, tt_user_id=user_id).annotate(
            d_flag=F('flag').bitand(2)).exclude(d_flag=2).exclude(tt_current_status=closed_state_id)
    if cat == 0:
        return {"data": UserTrackingPersonalSerializer(user_tracking.filter(ut_bns_id=0), many=True, context={"role": request.session['role']}).data,
                "is_user": request.session['role'] == "user"}
    elif cat == 1:
        return {"data": UserTrackingBusinessSerializer(user_tracking.exclude(ut_bns_id=0), many=True, context={"role": request.session['role']}).data,
                "is_user": request.session['role'] == "user"}
    elif cat == 2:
        return {"data": TaskTrackingSerializer(task_tracking, many=True, context={"role": request.session['role']}).data,
                "is_user": request.session['role'] == "user"}
    else:
        return {}


def _client_dashboard_alerts(request):
    admin_id = request.session['admin_id']
    if request.session['role'] == "user":
        user_id = request.session['user_id']
    else:
        user_id = request.query_params['user_id']
    alert_type = request.query_params['alert_type']
    is_user_visible = request.session['role'] == "user"
    emp_id = -1
    if request.session['role'] == "manager" or request.session['role'] == "employee" or request.session['role'] == "direct_employee":
        emp_id = request.session['emp_id']

    def _alert_post_process(**kwargs):
        return True, kwargs['q_alerts']

    tab_config = None
    q_alerts = None
    if alert_type == "-":
        q_user_tracking_alerts = fetch_alerts(Alert=Alert, admin_id=admin_id, user_id=user_id, alert_type="user_tracking", emp_id=emp_id,
                                              is_user_visible=is_user_visible, post_process=_alert_post_process)[1]
        q_task_tracking_alerts = fetch_alerts(Alert=Alert, admin_id=admin_id, user_id=user_id, alert_type="task_tracking", emp_id=emp_id,
                                              is_user_visible=is_user_visible, post_process=_alert_post_process)[1]
        q_alerts = q_user_tracking_alerts
        user_tracking_notif_num = q_user_tracking_alerts.count()
        task_tracking_notif_num = q_task_tracking_alerts.count()
        tab_config = [
            {"target": "user_tracking", "active": True, "display": "Tax Filings"},
            {"target": "task_tracking", "active": False, "display": "Projects"}
        ]
        if user_tracking_notif_num > 0:
            tab_config[0]["notif"] = {"notifNumber": user_tracking_notif_num}
        if task_tracking_notif_num > 0:
            tab_config[1]["notif"] = {"notifNumber": task_tracking_notif_num}
    else:
        q_alerts = fetch_alerts(Alert=Alert, admin_id=admin_id, user_id=user_id, alert_type=alert_type, emp_id=emp_id,
                                is_user_visible=is_user_visible, post_process=_alert_post_process)[1]
    """
    q_alerts = fetch_alerts(Alert=Alert, admin_id=admin_id, user_id=user_id, alert_type="", emp_id=emp_id, is_user_visible=is_user_visible,
        post_process=_alert_post_process)[1]
    """
    return {"data": AlertSerializer(q_alerts, many=True).data, "tab_config": tab_config}


# Mark upload complete
def _client_dashboard_upload_complete_process(request):
    admin_id = request.session['admin_id']
    if request.session['role'] == "user":
        user_id = request.session['user_id']
    else:
        user_id = request.query_params['user_id']
    tracking_id = request.POST['tracking_id']

    ut_record = UserTracking.objects.get(
        ut_admin_id=admin_id, ut_user_id=user_id, id=tracking_id)
    ut_record.set_upload_complete()
    ut_record.save()

    return 200, {"query_response": {"success": ["Upload Complete Successful"]}}

# Mark Extension


def _client_dashboard_extension_process(request):
    admin_id = request.session['admin_id']
    if request.session['role'] == "user":
        user_id = request.session['user_id']
    else:
        user_id = request.query_params['user_id']
    tracking_id = request.POST['tracking_id']

    ut_record = UserTracking.objects.get(
        ut_admin_id=admin_id, ut_user_id=user_id, id=tracking_id)
    ut_record.set_extension()
    ut_record.save()

    return 200, {"query_response": {"success": ["Extension Successful"]}}

# Notes


def _client_dashboard_notes(request):
    admin_id = request.session['admin_id']
    if request.session['role'] == "user":
        user_id = request.session['user_id']
    else:
        user_id = request.query_params['user_id']
    user_obj = User.objects.get(user_admin_id=admin_id, id=user_id)
    notes = str()
    if request.session['role'] == "admin":
        notes = user_obj.user_admin_notes
    elif request.session['role'] == "manager":
        notes = user_obj.user_manager_notes
    elif request.session['role'] == "employee" or request.session['role'] == "direct_employee":
        notes = user_obj.user_employee_notes
    return {"notes": notes}


def _client_dashboard_notes_process(request):
    params = {}
    response = {}

    admin_id = request.session['admin_id']
    if request.session['role'] == "user":
        user_id = request.session['user_id']
        params['context'] = "client"
        params['user_id'] = user_id
    else:
        user_id = request.query_params['user_id']
        params['user_id'] = user_id

    user_obj = User.objects.get(user_admin_id=admin_id, id=user_id)
    new_note = request.POST['new_note']
    if request.session['role'] == "admin":
        params['context'] = "admin"
        user_obj.user_admin_notes = new_note
    elif request.session['role'] == "manager":
        params['emp_id'] = request.session['emp_id']
        params['context'] = "emp"
        user_obj.user_manager_notes = new_note
    elif request.session['role'] == "employee" or request.session['role'] == "direct_employee" or request.session['role'] == "recep":
        params['emp_id'] = request.session['emp_id']
        params['context'] = "emp"
        user_obj.user_employee_notes = new_note

    user_obj.save()
    params['notes'] = new_note
    params['key'] = "pm_key_admin_client_notes"
    params['admin_id'] = admin_id
    params['user_id'] = user_id
    create_log(params, response)
    return 200, {"query_response": {"success": ["Notes successfully updated"]}}

# Todo List


def _client_dashboard_todo(request):
    admin_id = request.session['admin_id']
    if request.session['role'] == "user":
        user_id = request.session['user_id']
    else:
        user_id = request.query_params['user_id']
    is_client_view = request.session['role'] == "user"

    def _todo_post_process(**kwargs):
        if kwargs['is_success']:
            return True, TodoSerializer(kwargs['q_todo'], many=True).data
        return False, False
    is_success, return_response = todo_fetch(TodoList=TodoList, admin_id=admin_id, user_id=user_id, is_client_view=is_client_view,
                                             post_process=_todo_post_process)
    return return_response


def _client_dashboard_todo_process(request):
    def _todo_pre_process_check(**kwargs):
        duedate = kwargs['duedate']
        if duedate == '':
            return False, (412, {"query_response": {"fail": ["Please Select Date"]}})
        try:
            user_obj = User.objects.get(
                user_admin_id=kwargs['admin_id'], id=kwargs['user_id'])
        except User.DoesNotExist:
            return False, (412, {"query_response": {"fail": ["Invalid User"]}})
        duedate = duedate + " 23:59"
        duedate = datetime.strptime(duedate, "%Y-%m-%d %H:%M")
        duedate = make_aware(duedate, timezone=get_current_timezone()).astimezone(
            get_default_timezone())
        return True, {"duedate": duedate, "user_full_name": user_obj.user_full_name}

    def _todo_create_log(**kwargs):
        log_params = dict()
        log_response = dict()
        log_params['admin_id'] = kwargs['admin_id']
        log_params['user_id'] = kwargs['user_id']
        log_params['key'] = "pm_key_client_add_todo_task"
        log_params['task'] = kwargs['task']
        log_params['duedate'] = kwargs['duedate']
        role = kwargs['role']
        if role == "admin":
            log_params['context'] = "admin"
        elif role == "user":
            log_params['context'] = "client"
        elif role == "employee" or role == "manager" or role == "recep" or role == "direct_employee":
            log_params['emp_id'] = kwargs['emp_id']
            log_params['context'] = "emp"
        create_log(log_params, log_response)

    def _todo_post_process(**kwargs):
        _todo_create_log(**kwargs)
        return True, (200, {"query_response": {"success": ["TodoList successfully added"]}, "data": TodoSerializer(kwargs['todo_obj']).data})

    admin_id = request.session['admin_id']
    if request.session['role'] == "user":
        user_id = request.session['user_id']
    else:
        user_id = request.query_params['user_id']
    role = request.session['role']
    emp_id = -1
    d_context = {"role": role}
    if role == "employee" or role == "manager" or role == "recep" or role == "direct_employee":
        emp_id = request.session['emp_id']
        d_context['emp_id'] = emp_id
    task = request.POST['task']
    duedate = request.POST['duedate']
    is_success, return_response = todo_create(TodoList=TodoList, Notifications=Notifications, admin_id=admin_id,
                                              user_id=user_id, duedate=duedate, task=task, sent_name=request.session[
                                                  'name'], context=d_context,
                                              pre_process=_todo_pre_process_check, post_process=_todo_post_process)

    return return_response


def _client_dashboard_todo_switch_state(request):
    params = dict()
    response = dict()
    admin_id = request.session['admin_id']
    if request.session['role'] == "user":
        user_id = request.session['user_id']
    else:
        user_id = request.query_params['user_id']
    role = request.session['role']
    if role == "employee" or role == "manager" or role == "recep" or role == "direct_employee":
        emp_id = request.session['emp_id']
        params['emp_id'] = emp_id
    todoID = int(request.POST['todo_id'])
    mark = int(request.POST['todo_movement_mark'])
    is_processed = False
    params['admin_id'] = admin_id
    params['user_id'] = user_id
    if role == "admin":
        params['context'] = "admin"
    elif role == "user":
        params['context'] = "client"
    elif role == "employee" or role == "manager" or role == "recep" or role == "direct_employee":
        params['context'] = "emp"

    """
    0: Down
    ex: Completed -> Pending
    1: Up
    ex: Pending -> Completed
    """
    todoOBJ = TodoList.objects.get(id=todoID)
    try:
        notif = Notifications.objects.get(
            ntfy_admin_id=admin_id, ntfy_user_id=user_id)
    except Notifications.DoesNotExist:
        return 412, {"query_response": {"fail": ["Invalid request"]}}
    l_todo_task_names = list()
    response_message = str()
    if todoOBJ.check_completed():
        if mark == 0:
            if todoOBJ.check_processed():
                todoOBJ.reset_processed()
            todoOBJ.reset_completed()
            response_message = "TodoList moved to Pending"
            notif.increment_client_todo(1, todoOBJ.check_auto())
            notif.set_client_todo_update_time(todoOBJ.check_auto())
            notif.set_team_todo_update_time(todoOBJ.check_auto())
            l_todo_task_names.append(todoOBJ.td_task)
            params['key'] = "pm_key_client_complete_todo_task"
            params['l_todo_task_names'] = l_todo_task_names
        else:
            todoOBJ.td_processed_date = timezone.now()
            todoOBJ.set_processed()
            todoOBJ.reset_completed()
            response_message = "TodoList marked as Processed"
            is_processed = True

            notif.decrement_team_todo(1, todoOBJ.check_auto())
            notif.set_team_todo_update_time(todoOBJ.check_auto())
            l_todo_task_names.append(todoOBJ.td_task)
            params['key'] = "pm_key_client_process_todo_task"
            params['l_todo_task_names'] = l_todo_task_names
    else:
        todoOBJ.td_completed_date = timezone.now()
        todoOBJ.set_completed()
        response_message = "TodoList moved to Completed"
        notif.decrement_client_todo(1, todoOBJ.check_auto())
        notif.set_client_todo_update_time(todoOBJ.check_auto())
        notif.set_team_todo_update_time(todoOBJ.check_auto())
        l_todo_task_names.append(todoOBJ.td_task)
        params['key'] = "pm_key_client_complete_todo_task"
        params['l_todo_task_names'] = l_todo_task_names
    notif.save()
    todoOBJ.save()
    create_log(params, response)
    if is_processed:
        return 200, {"data": {"message": "Remove element"}, "query_response": {"success": [response_message]}}
    return 200, {"data": TodoSerializer(todoOBJ).data, "query_response": {"success": [response_message]}}


# Messages

def _client_dashboard_messages(request):
    admin_id = request.session['admin_id']
    role = request.session['role']
    if request.session['role'] == "user":
        user_id = request.session['user_id']
    else:
        user_id = request.query_params['user_id']
    emp_id = -1
    if role == "manager" or role == "employee" or role == "direct_employee":
        emp_id = request.session['emp_id']

    def _messages_fetch_post_process(**kwargs):
        update_notification_channel([request.session], kwargs['message_type'])
        if kwargs['is_success']:
            return True, {"data": MessagesSerializer(kwargs['q_messages'], many=True, context={'email': request.session['email']}).data}
        return False, False

    is_success, return_response = message_fetch(Messages=Messages, Notifications=Notifications, admin_id=admin_id, user_id=user_id,
                                                emp_id=emp_id, message_type=request.query_params['type'], role=request.session['role'], post_process=_messages_fetch_post_process)
    return return_response


def _client_dashboard_messages_process(request):
    def message_post_process(**kwargs):
        notif_cxt = kwargs['notif_cxt']
        message_type = kwargs['message_type']
        sent_email = kwargs['sent_email']
        l_channels_notif_update = list()
        admin_config_obj = AdminConfig.objects.get(
            ac_admin_id=request.session['admin_id'])
        if notif_cxt == "admin":
            # Adding the user records to notif channel
            if message_type == "client":
                l_channels_notif_update.append(
                    {"role": "user", "admin_id": admin_id, "user_id": user_id})
            # Adding the employee records to notif channel
            for key, value in kwargs['notif_obj'].ntfy_emp_id.items():
                l_channels_notif_update.append({"role": value, "admin_id": admin_id, "emp_id": int(
                    key, 16), "d_auth": admin_config_obj.ac_access_settings[value]})
        elif notif_cxt == "manager" or notif_cxt == "employee" or notif_cxt == "direct_employee" or notif_cxt == "recep":
            # Adding the user records to notif channel
            l_channels_notif_update.append(
                {"role": "admin", "admin_id": admin_id})
            # Adding the admin records to notif channel
            if request.query_params['type'] == "client":
                l_channels_notif_update.append(
                    {"role": "user", "admin_id": admin_id, "user_id": user_id})
            # Adding the employee records to notif channel
            for key, value in kwargs['notif_obj'].ntfy_emp_id.items():
                emp_id = int(key, 16)
                if emp_id != request.session['emp_id']:
                    l_channels_notif_update.append(
                        {"role": value, "admin_id": admin_id, "emp_id": emp_id, "d_auth": admin_config_obj.ac_access_settings[value]})
        elif notif_cxt == "user":
            # Adding the admin records to notif channel
            l_channels_notif_update.append(
                {"role": "admin", "admin_id": admin_id})
            # Adding the employee records to notif channel
            for key, value in kwargs['notif_obj'].ntfy_emp_id.items():
                emp_id = int(key, 16)
                l_channels_notif_update.append(
                    {"role": value, "admin_id": admin_id, "emp_id": emp_id, "d_auth": admin_config_obj.ac_access_settings[value]})

        update_notification_channel(
            l_channels_notif_update, request.query_params['type'])

        log_params = dict()
        log_response = dict()
        log_params['admin_id'] = kwargs['admin_id']
        log_params['user_id'] = kwargs['user_id']
        log_params['message'] = kwargs['message']
        if notif_cxt == "employee" or notif_cxt == "manager" or notif_cxt == "recep" or notif_cxt == "direct_employee":
            log_params['emp_id'] = kwargs['emp_id']
        if message_type == "client":
            log_params['key'] = "pm_key_send_client_msg"
        elif message_type == "team":
            log_params['key'] = "pm_key_send_team_msg"
        if notif_cxt == "admin":
            log_params['context'] = "admin"
        elif notif_cxt == "manager" or notif_cxt == "employee" or notif_cxt == "direct_employee" or notif_cxt == "recep":
            log_params['context'] = "emp"
        elif notif_cxt == "user":
            log_params['context'] = "client"
        create_log(log_params, log_response)

        s_msg = MessagesSerializer(kwargs['message_obj'], context={
                                   'email': sent_email}).data
        return True, (200, {"query_response": {"success": ["Message Sent"]}, "data": s_msg})

    """
    Configuring the function with right parameters based on session
    """
    admin_id = request.session['admin_id']
    if request.session['role'] == "user":
        user_id = request.session['user_id']
    else:
        user_id = request.query_params['user_id']
    notif_cxt = request.session['role']
    sent_name = request.session['name']
    sent_email = request.session['email']
    message_form = request.POST['msg']
    emp_id = -1
    if notif_cxt == "employee" or notif_cxt == "manager" or notif_cxt == "recep" or notif_cxt == "direct_employee":
        emp_id = request.session['emp_id']

    is_success, return_response = message_create(Messages=Messages, Notifications=Notifications, admin_id=admin_id,
                                                 user_id=user_id, message=message_form, sent_name=sent_name, sent_email=sent_email, notif_cxt=notif_cxt,
                                                 message_type=request.query_params['type'], emp_id=emp_id, post_process=message_post_process)

    return return_response
