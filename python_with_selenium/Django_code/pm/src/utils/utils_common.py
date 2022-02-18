from .utils_logger import *
from pm.models import *
from rest_framework import status as rest_status

from django.core.exceptions import ValidationError
from django.core.validators import validate_email

import calendar


################################################################################
# Common Functions - Begin
################################################################################
def is_string_empty(string):
    return not (string and string.strip())

def is_email_invalid(email):
    try:
        validate_email(email)
    except ValidationError:
        return True
    else:
        return False

def get_tax_year():
    """
    curr_date = timezone.now()
    if curr_date.month < 12:
        return (curr_date.year - 1)
    else:
        return (curr_date.year)
    """
    return timezone.now().year - 1

def get_all_years():
    curr_year = get_tax_year()
    years = list()
    years.append(curr_year)
    for i in range(1, 4, 1):
        curr_year = curr_year - 1
        years.append(curr_year)
    return years

def get_rest_status(status):
    if status == 200:
        return rest_status.HTTP_200_OK
    elif status == 412:
        return rest_status.HTTP_412_PRECONDITION_FAILED
    elif status == 500:
        return rest_status.HTTP_500_INTERNAL_SERVER_ERROR
    elif status == 401:
        return rest_status.HTTP_401_UNAUTHORIZED
    #return error code 500 for unknown status code
    return rest_status.HTTP_500_INTERNAL_SERVER_ERROR

def password_validate(password):
    is_valid = True
    valid_message = list()
    l_spec_char = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
    if len(password) not in range(8, 20):
        is_valid = False
        if len(password) < 8:
            valid_message.append("Your password is too short")
        else:
            valid_message.append("Your password is too long")
    if not any(x.isupper() for x in password):
        is_valid = False
        valid_message.append("Your password must have atleast one uppercase letter")
    if not any(x.isdigit() for x in password):
        is_valid = False 
        valid_message.append("Your password must have atleast one number")
    if not any(x in l_spec_char for x in password):
        is_valid = False
        valid_message.append("Your password must have atleast one special character")
    return is_valid, valid_message 

def check_user_exist(email, response={}):
    email = email.lower()
    try:
        Admin.objects.get(admin_email=email)
    except Admin.DoesNotExist:
        pass
    else:
        return True

    try:
        emp_obj = Employee.objects.get(emp_email=email)
    except Employee.DoesNotExist:
        pass
    else:
        response['mgr_name'] = emp_obj.emp_mgr_name
        return True

    try:
        User.objects.get(user_email=email)
    except User.DoesNotExist:
        pass
    else:
        return True

    return False

def get_active_clients(admin_id):
    users = User.objects.all().annotate(d_flag=F('flag').bitand(2)).filter(user_admin_id=admin_id, d_flag=2)
    user_list = [item.id for item in users]
    return user_list

def get_emp_list(admin_id, emp_id, **kwargs):
    q_emp = Employee.objects.all().filter(emp_admin_id=admin_id, id=emp_id) | \
        Employee.objects.all().filter(emp_admin_id=admin_id, emp_mgr=emp_id)

    all_emp_for_admin = kwargs.get('all_emp_for_admin', 0)
    if all_emp_for_admin == 1:
        q_emp = Employee.objects.all().annotate(d_flag=F('flag').bitand(32)).exclude(d_flag=32) \
            .filter(emp_admin_id=admin_id).order_by('emp_full_name')

    admin_all_emp = kwargs.get('admin_all_emp', 0)
    if admin_all_emp == 1:
        q_emp = Employee.objects.all().annotate(d_flag=F('flag').bitand(32)).exclude(d_flag=32) \
            .filter(emp_admin_id=admin_id, emp_mgr=0).order_by('emp_full_name')

    admin_direct_emp = kwargs.get('admin_direct_emp', 0)
    if admin_direct_emp == 1:
        q_emp = Employee.objects.all().annotate(d_flag=F('flag').bitand(32)).exclude(d_flag=32) \
            .filter(emp_admin_id=admin_id, emp_mgr=0) \
            .annotate(d_flag=F('flag').bitand(16)).exclude(d_flag=16).order_by('emp_full_name')

    admin_mgr_emp = kwargs.get('admin_mgr_emp', 0)
    if admin_mgr_emp == 1:
        q_emp = Employee.objects.all().annotate(d_flag=F('flag').bitand(32)).exclude(d_flag=32) \
            .filter(emp_admin_id=admin_id, emp_mgr=0) \
            .annotate(d_flag=F('flag').bitand(16)).filter(d_flag=16).order_by('emp_full_name')

    active_emp = kwargs.get('active_emp', 0)
    if active_emp == 1:
        q_emp = q_emp.annotate(d_flag=F('flag').bitand(2))

    queryset = kwargs.get("queryset", 0)
    if queryset == 1:
        return q_emp
    return q_emp.values_list("id", flat=True)

def get_admin_info(context, admin_id):
    context['admin_obj'] = Admin.objects.get(id=admin_id)

def get_emp_info(context, admin_id, emp_id):
    get_admin_info(context, admin_id)
    context['emp_obj'] = Employee.objects.get(emp_admin_id=admin_id, id=emp_id)

def get_client_info(context, admin_id, user_id):
    get_admin_info(context, admin_id)
    context['user_obj'] = User.objects.get(user_admin_id=admin_id, id=user_id)

################################################################################
# Common Functions - End
################################################################################

def get_url_redirect(params, response):
    url = params['url']
    value = params['value']
    if value == True:
        url += "?success=" + str(response['success'])
    else:
        url += "?fail=" + str(response['fail'])
    return url

def get_response_context_fill(params, context):
    success = params['success']
    fail = params['fail']

    if success != False:
        context['success'] = success
    else:
        context['fail'] = fail

def set_admin_config(adminConfig):
    adminConfig.set_default_config() 
    adminConfig.save()

def get_business_day_due_date(from_date, add_days):
    business_days_to_add = add_days
    current_date = from_date
    while business_days_to_add > 0:
        current_date += dt.timedelta(days=1)
        weekday = current_date.weekday()
        if weekday >= 5: # sunday = 6
            continue
        business_days_to_add -= 1
    return current_date

def get_date_range(params, response):
    range_text = params['range_text']
    try:
        prev_only = params['prev_only']
    except KeyError:
        prev_only = False
    
    try:
        post_only = params['post_only']
    except KeyError:
        post_only = False

    try:
        prev_post = params['prev_post']
    except KeyError:
        prev_post = False

    try:
        today_date = params['today_date']
    except KeyError:
        today_date = timezone.now()
    
    #local_today_date = timezone.now().astimezone(get_current_timezone())
    local_today_date = today_date.astimezone(get_current_timezone())

    response['filter_info'] = list()
    response['l_labels'] = list()

    if prev_only == True or prev_post == True:
        if range_text == "1week":
            start_date = local_today_date - dt.timedelta(days=6)
            local_start_date = local_today_date - dt.timedelta(days=6)
            for i in range(7):
                year = start_date.year
                month = start_date.month
                day = start_date.day
                date_append = date(year, month, day)
                response['filter_info'].append(date_append)
                if prev_post == True and date_append == local_today_date.date():
                    response['l_labels'].append("Today")
                elif prev_post == True:
                    response['l_labels'].append("Prev " + local_start_date.strftime('%a'))
                else:
                    response['l_labels'].append(local_start_date.strftime('%a'))
                start_date = start_date + dt.timedelta(days=1)
                local_start_date = local_start_date + dt.timedelta(days=1)
        elif range_text == "1month":
            start_date = local_today_date - dt.timedelta(days=27)
            local_start_date = local_today_date - dt.timedelta(days=27)
            for i in range(4):
                year = list()
                month = list()
                day = list()
                local_year = list()
                local_month = list()
                local_day = list()
                for j in range(7):
                    year.append(start_date.year)
                    month.append(start_date.month)
                    day.append(start_date.day)
                    local_year.append(local_start_date.year)
                    local_month.append(local_start_date.month)
                    local_day.append(local_start_date.day)
                    start_date = start_date + dt.timedelta(days=1)
                    local_start_date = local_start_date + dt.timedelta(days=1)
                response['filter_info'].append([date(year[0], month[0], day[0]), date(year[-1], month[-1], day[-1])])
                response['l_labels'].append(str(local_month[0]) + "/" + str(local_day[0]) + "-" + str(local_month[-1]) + "/" + str(local_day[-1]))
        elif range_text == "3month":
            month = local_today_date.month
            year = local_today_date.year
            local_month = local_today_date.month
            local_year = local_today_date.year
            if month >= 3:
                start_month = month - 2
                start_year = year
            elif month == 2:
                start_month = 12
                start_year = year - 1
            elif month == 1:
                start_month = 11
                start_year = year - 1

            if local_month >= 3:
                local_start_month = local_month - 2
                local_start_year = local_year
            elif local_month == 2:
                local_start_month = 12
                local_start_year = local_year - 1
            elif local_month == 1:
                local_start_month = 11
                local_start_year = local_year - 1

            for i in range(2):
                response['filter_info'].append([[start_year], [start_month]])
                response['l_labels'].append(calendar.month_abbr[local_start_month])
                start_year = start_year + int(start_month/12)
                start_month = (start_month % 12) + 1
                local_start_year = local_start_year + int(local_start_month/12)
                local_start_month = (local_start_month % 12) + 1
            response['filter_info'].append([[local_today_date.year], [local_today_date.month]])
            response['l_labels'].append(calendar.month_abbr[local_today_date.month])
    if post_only == True or prev_post == True:
        if range_text == "1week":
            if prev_post == True:
                start_date = local_today_date + dt.timedelta(days=1)
                local_start_date = local_today_date + dt.timedelta(days=1)
            else:
                start_date = local_today_date
                local_start_date = local_today_date
            for i in range(7):
                year = start_date.year
                month = start_date.month
                day = start_date.day
                date_append = date(year, month, day)
                response['filter_info'].append(date_append)
                if prev_post == True:
                    response['l_labels'].append("Post " + local_start_date.strftime('%a'))
                else:
                    response['l_labels'].append(local_start_date.strftime('%a'))
                start_date = start_date + dt.timedelta(days=1)
                local_start_date = local_start_date + dt.timedelta(days=1)
        elif range_text == "1month":
            if prev_post == True:
                start_date = local_today_date + dt.timedelta(days=1)
                local_start_date = local_today_date + dt.timedelta(days=1)
            else:
                start_date = local_today_date
                local_start_date = local_today_date
            for i in range(4):
                year = list()
                month = list()
                day = list()
                local_year = list()
                local_month = list()
                local_day = list()
                for j in range(7):
                    year.append(start_date.year)
                    month.append(start_date.month)
                    day.append(start_date.day)
                    local_year.append(local_start_date.year)
                    local_month.append(local_start_date.month)
                    local_day.append(local_start_date.day)
                    start_date = start_date + dt.timedelta(days=1)
                    local_start_date = local_start_date + dt.timedelta(days=1)
                response['filter_info'].append([date(year[0], month[0], day[0]), date(year[-1], month[-1], day[-1])])
                response['l_labels'].append(str(local_month[0]) + "/" + str(local_day[0]) + "-" + str(local_month[-1]) + "/" + str(local_day[-1]))
        elif range_text == "3month":
            start_month = local_today_date.month
            start_year = local_today_date.year
            local_start_month = local_today_date.month
            local_start_year = local_today_date.year
            if prev_post == False:
                response['filter_info'].append([[start_year], [start_month]])
                response['l_labels'].append(calendar.month_abbr[local_today_date.month])
            for i in range(2):
                start_year = start_year + int(start_month/12)
                start_month = (start_month % 12) + 1
                local_start_year = local_start_year + int(local_start_month/12)
                local_start_month = (local_start_month % 12) + 1
                response['filter_info'].append([[start_year], [start_month]])
                response['l_labels'].append(calendar.month_abbr[local_start_month])