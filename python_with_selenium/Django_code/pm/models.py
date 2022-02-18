from django.db import models
from django.db.models import F, Sum, Value
from django.conf import settings
from django.core.files.storage import FileSystemStorage, default_storage
import os
from django.utils import timezone
from django.utils.timezone import make_aware, get_current_timezone, get_default_timezone
import pytz
from datetime import date, datetime
import datetime as dt
import pdb
import json
from random import randint
from django_calendar.calendar_api import *
from django_accounting.accounting_api import *

from intelws_core.models import (
    BaseUser, BaseNotifications, BaseAlert, BaseEmployee, BaseAdmin, BaseMessages, BaseAppointments,
    BaseLeadTracking, BaseCmtyQues, BaseTaskTracking, BaseInvoices, BaseTodoList,
    BaseTaskFiles, BaseApplicationLeads, BaseBulkMsg, _set_default_upload_time
)

from pm.src.api.common.url_map import *

def get_status_id_from_bucket(admin_id, internal_bucket_name):
    admin_config = AdminConfig.objects.get(ac_admin_id=admin_id)
    try:
        bucket_obj = admin_config.ac_bucket_get(internal_bucket_name=internal_bucket_name)
    except Exception:
        return None
    l_status_id = []
    for status_obj in bucket_obj["status_objs"]:
        l_status_id.append(status_obj["id"])
    return l_status_id

def get_status_name_from_bucket(admin_id, internal_bucket_name):
    admin_config = AdminConfig.objects.get(ac_admin_id=admin_id)
    try:
        bucket_obj = admin_config.ac_bucket_get(internal_bucket_name=internal_bucket_name)
    except Exception:
        return None
    l_status_name = []
    for status_obj in bucket_obj["status_objs"]:
        l_status_name.append(status_obj["display_name"])
    return l_status_name

def get_status_obj_from_bucket(admin_id, internal_bucket_name):
    admin_config = AdminConfig.objects.get(ac_admin_id=admin_id)
    try:
        bucket_obj = admin_config.ac_bucket_get(internal_bucket_name=internal_bucket_name)
    except Exception:
        return None
    return bucket_obj["status_objs"]

def get_status_obj_from_status_id(admin_id, status_id):
    admin_config = AdminConfig.objects.get(ac_admin_id=admin_id)
    try:
        status_obj = admin_config.ac_status_get(id=status_id)
    except Exception:
        return None
    return status_obj

def get_status_obj_from_internal_name(admin_id, internal_status_name):
    admin_config = AdminConfig.objects.get(ac_admin_id=admin_id)
    try:
        status_obj = admin_config.ac_status_get(internal_status_name=internal_status_name)
    except Exception:
        return None
    return status_obj
# Create your models here.
###########################################################################
# Packaging Models
###########################################################################
class Bitmap():
    #Methods
    def set_flag(self, bit):
        self.flag = (self.flag | (0x01 << bit))
        return self.flag

    def reset_flag(self, bit):
        self.flag &= ~(0x01 << bit)
        return self.flag

    def is_flag_valid(self, bit):
        flag = (self.flag & (0x01 << bit))
        if flag == 0:
            return False
        else:
            return True

class Packaging(models.Model):
    #Fields
    UPLOAD_DIR = models.CharField(max_length=1000)
    AUTH_DIR = models.CharField(max_length=1000)
    VERSION = models.IntegerField(default=0)

    #Methods
    def __str__(self):
        return str(self.pk)

    def get_dir(self):
        return self.UPLOAD_DIR

    def get_auth_dir(self):
        return self.AUTH_DIR

class Category(models.Model, Bitmap):
    #Fields
    cat_name = models.CharField(max_length=1000)
    external_cat_name = models.CharField(max_length=1000)
    flag = models.IntegerField(default=0)
    flag2 = models.IntegerField(default=0)

    #Methods
    def __str__(self):
        return str(str(self.pk) + "::" + self.cat_name)

class Bns_types(models.Model, Bitmap):
    #Fields
    bns_type_name = models.CharField(max_length=1000)
    flag = models.IntegerField(default=0)
    flag2 = models.IntegerField(default=0)

    #Methods
    def __str__(self):
        return str(str(self.pk) + "::" + self.bns_type_name)

class US_States(models.Model):
    state_abbr = models.CharField(max_length=10)

class File_types(models.Model, Bitmap):
    #Fields
    file_type_name = models.CharField(max_length=1000)
    flag = models.IntegerField(default=0)
    flag2 = models.IntegerField(default=0)

    #Methods
    def __str__(self):
        return str(str(self.pk) + "::" + self.file_type_name + "::" + str(self.flag))

    def set_personal(self):
        self.set_flag(1)

    def reset_personal(self):
        self.reset_flag(1)

    def is_personal(self):
        return self.is_flag_valid(1)

    def set_business(self):
        self.set_flag(2)

    def reset_business(self):
        self.reset_flag(2)

    def is_business(self):
        return self.is_flag_valid(2)

###########################################################################
# Core Modules
# Admin, Employee, User, Files, UserTracking, HistoryStatus
###########################################################################
def set_ac_template_raised_date_offset_default():
    return {
        "monthly": 10,
        "quarterly": 15,
        "yearly": 30
    }

def set_ac_payment_prices_default():
    return {
        "client": 0.01,
        "business": 0.01,
        "esign": 2
    }

def set_ac_access_settings_default():
    d_default_settings = {
        "client_interaction": True,
        "business": True,
        "unassigned": True,
        "invoice": True,
        "esign": True
    }
    return {
        "employee": d_default_settings,
        "manager": d_default_settings,
        "direct_employee": d_default_settings,
        "recep": d_default_settings
    }

class AdminConfig(models.Model, Bitmap):
    ac_admin_id = models.IntegerField()

    ac_due_date = models.IntegerField(default=5)
    ac_template_raised_date_offset = models.JSONField(default=set_ac_template_raised_date_offset_default)
    ac_access_settings = models.JSONField(default=set_ac_access_settings_default)
    flag = models.IntegerField(default=0)
    flag2 = models.IntegerField(default=0)

    # id, internal_status_name, display_name
    ac_status = models.JSONField(default=list)
    ac_next_status_id = models.IntegerField(default=1)

    # id, display_name, group_name, list of status objects
    ac_bucket_status = models.JSONField(default=list)
    ac_next_bucket_id = models.IntegerField(default=1)

    ac_payment_prices = models.JSONField(default=set_ac_payment_prices_default)
    ac_esign_raised = models.IntegerField(default=0)

    # key - role, value - list of bucket objects
    ac_bucket_status_role = models.JSONField(default=dict)

    # id, internal_status_name, display_name
    def ac_status_create(self, internal_status_name, display_name):
        try:
            self.ac_status_get(internal_status_name=internal_status_name)
        except Exception:
            pass
        else:
            raise Exception("Status already exists")

        status_obj = {
            "id": self.ac_next_status_id,
            "internal_status_name": internal_status_name,
            "display_name": display_name
        }
        self.ac_status.append(status_obj)
        self.ac_next_status_id += 1

    def ac_status_get(self, **kwargs):
        key = None
        value = None
        if "id" in kwargs:
            key = "id"
            value = kwargs["id"]
        elif "internal_status_name" in kwargs:
            key = "internal_status_name"
            value = kwargs["internal_status_name"]
        else:
            raise Exception("Invalid parameters used")

        for status_obj in self.ac_status:
            if status_obj[key] == value:
                return status_obj
        
        raise Exception("Invalid status info")

    def ac_status_set(self, display_name, **kwargs):
        key = None
        value = None
        if "id" in kwargs:
            key = "id"
            value = kwargs["id"]
        elif "internal_status_name" in kwargs:
            key = "internal_status_name"
            value = kwargs["internal_status_name"]
        else:
            raise Exception("Invalid parameters used")

        for status_obj in self.ac_status:
            if status_obj[key] == value:
                status_obj["display_name"] = display_name
                return True

        return False

    # id, internal_bucket_name, display_name, list of status objects
    def ac_bucket_create(self, internal_bucket_name, display_name, **kwargs):
        bucket_obj = {
            "id": self.ac_next_bucket_id,
            "internal_bucket_name": internal_bucket_name,
            "display_name": display_name,
            "status_objs": []
        }

        try:
            self.ac_bucket_get(internal_bucket_name=internal_bucket_name)
        except Exception:
            pass
        else:
            raise Exception("Bucket already exists")

        arg_name = None
        l_iter = None
        if "l_status_id" in kwargs:
            arg_name = "id"
            l_iter = kwargs["l_status_id"]
        elif "l_status_internal_name" in kwargs:
            arg_name = "internal_status_name"
            l_iter = kwargs["l_status_internal_name"]
        else:
            raise Exception("Invalid parameters used")

        for item in l_iter:
            d_args = {arg_name: item}
            status_obj = self.ac_status_get(**d_args)
            if status_obj != None:
                bucket_obj["status_objs"].append(status_obj)
            else:
                raise Exception("Please use a valid argument for status querying. Element in question {}".format(str(d_args)))
        self.ac_bucket_status.append(bucket_obj)
        self.ac_next_bucket_id += 1
    
    def ac_bucket_get(self, **kwargs):
        key = None
        value = None

        if "id" in kwargs:
            key = "id"
            value = kwargs["id"]
        elif "internal_bucket_name" in kwargs:
            key = "internal_bucket_name"
            value = kwargs["internal_bucket_name"]
        else:
            raise Exception("Invalid parameters used")

        for bucket_obj in self.ac_bucket_status:
            if bucket_obj[key] == value:
                return bucket_obj
    
        raise Exception("Invalid Bucket Info")
    
    def ac_bucket_status_set(self, **kwargs):
        bucket_obj = self.ac_bucket_get(**kwargs)
        arg_name = None
        l_iter = None
        if "l_status_id" in kwargs:
            arg_name = "id"
            l_iter = kwargs["l_status_id"]
        elif "l_status_internal_name" in kwargs:
            arg_name = "internal_status_name"
            l_iter = kwargs["l_status_internal_name"]
        else:
            raise Exception("Invalid parameters used")

        status_objs = []
        for item in l_iter:
            d_args = {arg_name: item}
            status_obj = self.ac_status_get(**d_args)
            if status_obj != None:
                status_objs.append(status_obj)
            else:
                raise Exception("Please use a valid argument for status querying. Element in question {}".format(str(d_args))) 
        bucket_obj["status_objs"] = status_objs

    def ac_bucket_role_set(self, role, feature, l_bucket_internal_name):
        for bucket_internal_name in l_bucket_internal_name:
            try:
                self.ac_bucket_get(internal_bucket_name=bucket_internal_name)
            except Exception:
                raise Exception("Invalid Bucket. {}".format(bucket_internal_name))
        
        if role not in self.ac_bucket_status_role:
            self.ac_bucket_status_role[role] = dict()
        self.ac_bucket_status_role[role][feature] = l_bucket_internal_name

    def ac_bucket_role_get(self, role, feature):
        bucket_objs = []
        for bucket_internal_name in self.ac_bucket_status_role[role][feature]:
            bucket_objs.append(self.ac_bucket_get(internal_bucket_name=bucket_internal_name))
        return bucket_objs
    
    #Email Trigger Configurations
    def set_email_file_upload(self):
        self.set_flag(17)
    def reset_email_file_upload(self):
        self.reset_flag(17)
    def check_email_file_upload(self):
        return self.is_flag_valid(17)

    def set_email_file_upload_complete(self):
        self.set_flag(18)
    def reset_email_file_upload_complete(self):
        self.reset_flag(18)
    def check_email_file_upload_complete(self):
        return self.is_flag_valid(18)

    def set_email_status_change(self):
        self.set_flag(19)
    def reset_email_status_change(self):
        self.reset_flag(19)
    def check_email_status_change(self):
        return self.is_flag_valid(19)

    def set_email_user_message(self):
        self.set_flag(20)
    def reset_email_user_message(self):
        self.reset_flag(20)
    def check_email_user_message(self):
        return self.is_flag_valid(20)

    def set_email_todo_list(self):
        self.set_flag(21)
    def reset_email_todo_list(self):
        self.reset_flag(21)
    def check_email_todo_list(self):
        return self.is_flag_valid(21)

    def set_email_invoice(self):
        self.set_flag(22)
    def reset_email_invoice(self):
        self.reset_flag(22)
    def check_email_invoice(self):
        return self.is_flag_valid(22)

    def create_admin_manual_task_buckets(self):
        #Create Admin Manual Task Buckets here
        l_all_status = [
            "assigned", "in_progress", "mgr_review", "admin_review", "info_pending", "client_review", "closed"
        ]

        l_admin_bucket = [
            {"internal": "manual_admin_preparation", "display": "Preparation", "l_status_internal_name": ["assigned", "in_progress", "mgr_review"]},
            {"internal": "manual_admin_review", "display": "Review", "l_status_internal_name": ["admin_review"]},
            {"internal": "manual_admin_finalization", "display": "Finalization", "l_status_internal_name": ["info_pending", "client_review"]},
            {"internal": "manual_admin_closure", "display": "Closure", "l_status_internal_name": ["closed"]},
            {"internal": "manual_admin_overview", "display": "Overview", "l_status_internal_name": l_all_status},
            {"internal": "manual_admin_templates", "display": "Project Templates", "l_status_internal_name": l_all_status},
        ]

        l_manual_task_bucket_name = []
        for admin_bucket in l_admin_bucket:
            self.ac_bucket_create(internal_bucket_name=admin_bucket['internal'],
                display_name=admin_bucket['display'], l_status_internal_name=admin_bucket['l_status_internal_name'])
            l_manual_task_bucket_name.append(admin_bucket['internal'])
        self.ac_bucket_role_set(role="admin", feature="manual_task", l_bucket_internal_name=l_manual_task_bucket_name)

        l_admin_bucket = [
            {"internal": "admin_manual_dashboard", "display": "Task Due", "l_status_internal_name": ["assigned", "in_progress", "mgr_review", "admin_review"]}
        ]
        for admin_bucket in l_admin_bucket:
            self.ac_bucket_create(internal_bucket_name=admin_bucket['internal'],
                display_name=admin_bucket['display'], l_status_internal_name=admin_bucket['l_status_internal_name'])

        l_admin_bucket = [
            {"internal": "admin_manual_client_facing", "display": "NA", "l_status_internal_name": ["in_progress", "info_pending", "client_review", "closed"]}
        ]
        for admin_bucket in l_admin_bucket:
            self.ac_bucket_create(internal_bucket_name=admin_bucket['internal'],
                display_name=admin_bucket['display'], l_status_internal_name=admin_bucket['l_status_internal_name'])

    def create_recep_manual_task_buckets(self):
        #Create Admin Manual Task Buckets here
        l_all_status = [
            "assigned", "in_progress", "mgr_review", "admin_review", "info_pending", "client_review", "closed"
        ]

        l_recep_bucket = [
            {"internal": "manual_recep_overview", "display": "Overview", "l_status_internal_name": l_all_status}
        ]

        l_manual_task_bucket_name = []
        for recep_bucket in l_recep_bucket:
            self.ac_bucket_create(internal_bucket_name=recep_bucket['internal'],
                display_name=recep_bucket['display'], l_status_internal_name=recep_bucket['l_status_internal_name'])
            l_manual_task_bucket_name.append(recep_bucket['internal'])
        self.ac_bucket_role_set(role="recep", feature="manual_task", l_bucket_internal_name=l_manual_task_bucket_name) 

        l_recep_bucket = [
            {"internal": "recep_manual_dashboard", "display": "Task Due", "l_status_internal_name": ["assigned", "in_progress", "mgr_review", "admin_review"]}
        ]
        for recep_bucket in l_recep_bucket:
            self.ac_bucket_create(internal_bucket_name=recep_bucket['internal'],
                display_name=recep_bucket['display'], l_status_internal_name=recep_bucket['l_status_internal_name'])

    def create_manager_manual_task_buckets(self, create_bucket=True):
        #Create Manager Manual Task Buckets here
        l_all_status = []

        l_mgr_bucket = [
            {"internal": "manual_mgr_preparation", "display": "Preparation", "l_status_internal_name": ["assigned", "in_progress", "mgr_review"]},
            {"internal": "manual_mgr_finalization", "display": "Finalization", "l_status_internal_name": ["info_pending", "client_review"]},
            {"internal": "manual_mgr_closure", "display": "Closure", "l_status_internal_name": ["closed"]},
            {"internal": "manual_mgr_overview", "display": "Overview", "l_status_internal_name": []}
        ]

        l_manual_task_bucket_name = []

        #Preparation
        l_manual_task_bucket_name.append(l_mgr_bucket[0]["internal"])
        l_all_status += l_mgr_bucket[0]["l_status_internal_name"]
        if self.ac_access_settings['manager']['client_interaction']:
            #Finalization
            l_manual_task_bucket_name.append(l_mgr_bucket[1]["internal"])
            l_all_status += l_mgr_bucket[1]["l_status_internal_name"]
            #Closure
            l_manual_task_bucket_name.append(l_mgr_bucket[2]["internal"])
            l_all_status += l_mgr_bucket[2]["l_status_internal_name"]
        
        l_mgr_bucket[3]["l_status_internal_name"] = l_all_status
        l_manual_task_bucket_name.append(l_mgr_bucket[3]["internal"])
        
        if create_bucket: 
            for mgr_bucket in l_mgr_bucket:
                self.ac_bucket_create(internal_bucket_name=mgr_bucket['internal'],
                    display_name=mgr_bucket['display'], l_status_internal_name=mgr_bucket['l_status_internal_name'])
        else:
            self.ac_bucket_status_set(internal_bucket_name=l_mgr_bucket[2]["internal"], 
                l_status_internal_name=l_mgr_bucket[2]["l_status_internal_name"])
        self.ac_bucket_role_set(role="manager", feature="manual_task", l_bucket_internal_name=l_manual_task_bucket_name)

        l_mgr_bucket = [
            {"internal": "manager_manual_dashboard", "display": "Task Due", "l_status_internal_name": ["assigned", "in_progress", "mgr_review", "admin_review"]}
        ]
        if create_bucket:
            for mgr_bucket in l_mgr_bucket:
                self.ac_bucket_create(internal_bucket_name=mgr_bucket['internal'],
                    display_name=mgr_bucket['display'], l_status_internal_name=mgr_bucket['l_status_internal_name'])

    def create_employee_manual_task_buckets(self, create_bucket=True):
        #Create Employee Manual Task Buckets here
        l_all_status = []

        l_emp_bucket = [
            {"internal": "manual_emp_preparation", "display": "Preparation", "l_status_internal_name": ["assigned", "in_progress", "mgr_review"]},
            {"internal": "manual_emp_finalization", "display": "Finalization", "l_status_internal_name": ["info_pending", "client_review"]},
            {"internal": "manual_emp_closure", "display": "Closure", "l_status_internal_name": ["closed"]},
            {"internal": "manual_emp_overview", "display": "Overview", "l_status_internal_name": []}
        ]

        l_manual_task_bucket_name = []

        #Preparation
        l_manual_task_bucket_name.append(l_emp_bucket[0]["internal"])
        l_all_status += l_emp_bucket[0]["l_status_internal_name"]
        if self.ac_access_settings['employee']['client_interaction']:
            #Finalization
            l_manual_task_bucket_name.append(l_emp_bucket[1]["internal"])
            l_all_status += l_emp_bucket[1]["l_status_internal_name"]
            #Closure
            l_manual_task_bucket_name.append(l_emp_bucket[2]["internal"])
            l_all_status += l_emp_bucket[2]["l_status_internal_name"]
        
        l_emp_bucket[3]["l_status_internal_name"] = l_all_status
        l_manual_task_bucket_name.append(l_emp_bucket[3]["internal"])
        
        if create_bucket: 
            for emp_bucket in l_emp_bucket:
                self.ac_bucket_create(internal_bucket_name=emp_bucket['internal'],
                    display_name=emp_bucket['display'], l_status_internal_name=emp_bucket['l_status_internal_name'])
        else:
            self.ac_bucket_status_set(internal_bucket_name=l_emp_bucket[2]["internal"], 
                l_status_internal_name=l_emp_bucket[2]["l_status_internal_name"])
        self.ac_bucket_role_set(role="employee", feature="manual_task", l_bucket_internal_name=l_manual_task_bucket_name)

        l_emp_bucket = [
            {"internal": "employee_manual_dashboard", "display": "Task Due", "l_status_internal_name": ["assigned", "in_progress"]}
        ]
        if create_bucket:
            for emp_bucket in l_emp_bucket:
                self.ac_bucket_create(internal_bucket_name=emp_bucket['internal'],
                    display_name=emp_bucket['display'], l_status_internal_name=emp_bucket['l_status_internal_name'])

    def create_direct_employee_manual_task_buckets(self, create_bucket=True):
        #Create Direct Employee Manual Task Buckets here
        l_all_status = []

        l_emp_bucket = [
            {"internal": "manual_direct_emp_preparation", "display": "Preparation", "l_status_internal_name": ["assigned", "in_progress", "mgr_review"]},
            {"internal": "manual_direct_emp_finalization", "display": "Finalization", "l_status_internal_name": ["info_pending", "client_review"]},
            {"internal": "manual_direct_emp_closure", "display": "Closure", "l_status_internal_name": ["closed"]},
            {"internal": "manual_direct_emp_overview", "display": "Overview", "l_status_internal_name": []}
        ]

        l_manual_task_bucket_name = []

        #Preparation
        l_manual_task_bucket_name.append(l_emp_bucket[0]["internal"])
        l_all_status += l_emp_bucket[0]["l_status_internal_name"]
        if self.ac_access_settings['direct_employee']['client_interaction']:
            #Finalization
            l_manual_task_bucket_name.append(l_emp_bucket[1]["internal"])
            l_all_status += l_emp_bucket[1]["l_status_internal_name"]
            #Closure
            l_manual_task_bucket_name.append(l_emp_bucket[2]["internal"])
            l_all_status += l_emp_bucket[2]["l_status_internal_name"]
        
        l_emp_bucket[3]["l_status_internal_name"] = l_all_status
        l_manual_task_bucket_name.append(l_emp_bucket[3]["internal"])
        
        if create_bucket: 
            for emp_bucket in l_emp_bucket:
                self.ac_bucket_create(internal_bucket_name=emp_bucket['internal'],
                    display_name=emp_bucket['display'], l_status_internal_name=emp_bucket['l_status_internal_name'])
        else:
            self.ac_bucket_status_set(internal_bucket_name=l_emp_bucket[2]["internal"], 
                l_status_internal_name=l_emp_bucket[2]["l_status_internal_name"])
        self.ac_bucket_role_set(role="direct_employee", feature="manual_task", l_bucket_internal_name=l_manual_task_bucket_name)

        l_emp_bucket = [
            {"internal": "direct_employee_manual_dashboard", "display": "Task Due", "l_status_internal_name": ["assigned", "in_progress"]}
        ]
        if create_bucket:
            for emp_bucket in l_emp_bucket:
                self.ac_bucket_create(internal_bucket_name=emp_bucket['internal'],
                    display_name=emp_bucket['display'], l_status_internal_name=emp_bucket['l_status_internal_name'])
    
    def create_admin_task_buckets(self):
        l_all_status = [
            "initial", "assigned", "in_progress", "mgr_review", "admin_review", "info_pending", "client_review", "efile_auth", "efiled", "closed"
        ]

        l_admin_bucket = [
            {"internal": "admin_unassigned", "display": "Unassigned", "l_status_internal_name": ["initial"]},
            {"internal": "admin_preparation", "display": "Preparation", "l_status_internal_name": ["assigned", "in_progress", "mgr_review"]},
            {"internal": "admin_review", "display": "Review", "l_status_internal_name": ["admin_review"]},
            {"internal": "admin_finalization", "display": "Finalization", "l_status_internal_name": ["info_pending", "client_review", "efile_auth"]},
            {"internal": "admin_closure", "display": "Closure", "l_status_internal_name": ["efiled", "closed"]},
            {"internal": "admin_extension", "display": "Extension", "l_status_internal_name": l_all_status},
            {"internal": "admin_overview", "display": "Overview", "l_status_internal_name": l_all_status},
            {"internal": "admin_change_states", "display": "Admin Change States", "l_status_internal_name": l_all_status}
        ]

        l_task_bucket_name = []
        for admin_bucket in l_admin_bucket:
            self.ac_bucket_create(internal_bucket_name=admin_bucket['internal'],
                display_name=admin_bucket['display'], l_status_internal_name=admin_bucket['l_status_internal_name'])
            if admin_bucket["internal"] != "admin_change_states":
                l_task_bucket_name.append(admin_bucket['internal'])
        self.ac_bucket_role_set(role="admin", feature="task", l_bucket_internal_name=l_task_bucket_name)

        l_admin_bucket = [
            {"internal": "admin_task_dashboard", "display": "Task Due", "l_status_internal_name": ["assigned", "in_progress", "mgr_review", "admin_review"]}
        ]
        for admin_bucket in l_admin_bucket:
            self.ac_bucket_create(internal_bucket_name=admin_bucket['internal'],
                display_name=admin_bucket['display'], l_status_internal_name=admin_bucket['l_status_internal_name'])

    def create_recep_task_buckets(self):
        l_all_status = [
            "initial", "assigned", "in_progress", "mgr_review", "admin_review", "info_pending", "client_review", "efile_auth", "efiled", "closed"
        ]

        l_recep_bucket = [
            {"internal": "recep_extension", "display": "Extension", "l_status_internal_name": l_all_status},
            {"internal": "recep_overview", "display": "Overview", "l_status_internal_name": l_all_status}
        ]

        l_task_bucket_name = []
        for recep_bucket in l_recep_bucket:
            self.ac_bucket_create(internal_bucket_name=recep_bucket['internal'],
                display_name=recep_bucket['display'], l_status_internal_name=recep_bucket['l_status_internal_name'])
            l_task_bucket_name.append(recep_bucket['internal'])
        self.ac_bucket_role_set(role="recep", feature="task", l_bucket_internal_name=l_task_bucket_name) 

        l_recep_bucket = [
            {"internal": "recep_task_dashboard", "display": "Task Due", "l_status_internal_name": ["assigned", "in_progress", "mgr_review", "admin_review"]}
        ]
        for recep_bucket in l_recep_bucket:
            self.ac_bucket_create(internal_bucket_name=recep_bucket['internal'],
                display_name=recep_bucket['display'], l_status_internal_name=recep_bucket['l_status_internal_name'])

    def create_manager_task_buckets(self, create_bucket=True):
        l_mgr_bucket = [
            {"internal": "mgr_unassigned", "display": "Unassigned", "l_status_internal_name": ["initial"]},
            {"internal": "mgr_preparation", "display": "Preparation", "l_status_internal_name": ["assigned", "in_progress"]},
            {"internal": "mgr_review", "display": "Review", "l_status_internal_name": ["mgr_review"]},
            {"internal": "mgr_finalization", "display": "Finalization", "l_status_internal_name": ["info_pending", "client_review", "efile_auth"]},
            {"internal": "mgr_closure", "display": "Closure", "l_status_internal_name": ["efiled", "closed"]},
            {"internal": "mgr_extension", "display": "Extension", "l_status_internal_name": []},
            {"internal": "mgr_overview", "display": "Overview", "l_status_internal_name": []}
        ]
        l_mgr_composite_status_name = []
        l_mgr_change_status_name = ["assigned", "in_progress", "mgr_review", "admin_review"]
        l_task_bucket_name = []
        #Unassigned
        if self.ac_access_settings['manager']['unassigned']:
            l_task_bucket_name.append(l_mgr_bucket[0]["internal"])
            l_mgr_composite_status_name += l_mgr_bucket[0]["l_status_internal_name"]
        #Preparation
        l_task_bucket_name.append(l_mgr_bucket[1]["internal"])
        l_mgr_composite_status_name += l_mgr_bucket[1]["l_status_internal_name"]
        #Review
        l_task_bucket_name.append(l_mgr_bucket[2]["internal"])
        l_mgr_composite_status_name += l_mgr_bucket[2]["l_status_internal_name"]
        if self.ac_access_settings['manager']['client_interaction']:
            #Finalization
            l_task_bucket_name.append(l_mgr_bucket[3]["internal"])
            l_mgr_composite_status_name += l_mgr_bucket[3]["l_status_internal_name"]
            #Closure
            l_task_bucket_name.append(l_mgr_bucket[4]["internal"])
            l_mgr_composite_status_name += l_mgr_bucket[4]["l_status_internal_name"]
            #Change states
            l_mgr_change_status_name += ["info_pending", "client_review", "efile_auth", "efiled", "closed"]
        #Extension
        l_mgr_bucket[5]["l_status_internal_name"] = l_mgr_composite_status_name
        l_task_bucket_name.append(l_mgr_bucket[5]["internal"])
        #Overview
        l_mgr_bucket[6]["l_status_internal_name"] = l_mgr_composite_status_name
        l_task_bucket_name.append(l_mgr_bucket[6]["internal"])

        l_mgr_bucket.append({"internal": "mgr_change_states", "display": "Mgr Change States", "l_status_internal_name": l_mgr_change_status_name})

        if create_bucket: 
            for mgr_bucket in l_mgr_bucket:
                self.ac_bucket_create(internal_bucket_name=mgr_bucket['internal'],
                    display_name=mgr_bucket['display'], l_status_internal_name=mgr_bucket['l_status_internal_name'])
        else:
            self.ac_bucket_status_set(internal_bucket_name=l_mgr_bucket[5]["internal"], 
                l_status_internal_name=l_mgr_bucket[5]["l_status_internal_name"])
            self.ac_bucket_status_set(internal_bucket_name=l_mgr_bucket[6]["internal"], 
                l_status_internal_name=l_mgr_bucket[6]["l_status_internal_name"])
            self.ac_bucket_status_set(internal_bucket_name=l_mgr_bucket[7]["internal"], 
                l_status_internal_name=l_mgr_bucket[7]["l_status_internal_name"])
        self.ac_bucket_role_set(role="manager", feature="task", l_bucket_internal_name=l_task_bucket_name)

        l_mgr_bucket = [
            {"internal": "manager_task_dashboard", "display": "Task Due", "l_status_internal_name": ["assigned", "in_progress", "mgr_review", "admin_review"]}
        ]
        if create_bucket:
            for mgr_bucket in l_mgr_bucket:
                self.ac_bucket_create(internal_bucket_name=mgr_bucket['internal'],
                    display_name=mgr_bucket['display'], l_status_internal_name=mgr_bucket['l_status_internal_name'])

    def create_employee_task_buckets(self, create_bucket=True):
        l_emp_bucket = [
            {"internal": "emp_preparation", "display": "Preparation", "l_status_internal_name": ["assigned", "in_progress"]},
            {"internal": "emp_finalization", "display": "Finalization", "l_status_internal_name": ["info_pending", "client_review", "efile_auth"]},
            {"internal": "emp_closure", "display": "Closure", "l_status_internal_name": ["efiled", "closed"]},
            {"internal": "emp_extension", "display": "Extension", "l_status_internal_name": []},
            {"internal": "emp_overview", "display": "Overview", "l_status_internal_name": []}
        ]
        l_emp_composite_status_name = []
        l_emp_change_status_name = ["assigned", "in_progress", "mgr_review"]
        l_task_bucket_name = []
        #Preparation
        l_task_bucket_name.append(l_emp_bucket[0]["internal"])
        l_emp_composite_status_name += l_emp_bucket[0]["l_status_internal_name"]
        if self.ac_access_settings['employee']['client_interaction']:
            #Finalization
            l_task_bucket_name.append(l_emp_bucket[1]["internal"])
            l_emp_composite_status_name += l_emp_bucket[1]["l_status_internal_name"]
            #Closure
            l_task_bucket_name.append(l_emp_bucket[2]["internal"])
            l_emp_composite_status_name += l_emp_bucket[2]["l_status_internal_name"]
            #Change states
            l_emp_change_status_name += ["info_pending", "client_review", "efile_auth", "efiled", "closed"]
        #Extension
        l_emp_bucket[3]["l_status_internal_name"] = l_emp_composite_status_name
        l_task_bucket_name.append(l_emp_bucket[3]["internal"])
        #Overview
        l_emp_bucket[4]["l_status_internal_name"] = l_emp_composite_status_name
        l_task_bucket_name.append(l_emp_bucket[4]["internal"])

        l_emp_bucket.append({"internal": "emp_change_states", "display": "Emp Change States", "l_status_internal_name": l_emp_change_status_name})

        if create_bucket: 
            for emp_bucket in l_emp_bucket:
                self.ac_bucket_create(internal_bucket_name=emp_bucket['internal'],
                    display_name=emp_bucket['display'], l_status_internal_name=emp_bucket['l_status_internal_name'])
        else:
            self.ac_bucket_status_set(internal_bucket_name=l_emp_bucket[3]["internal"], 
                l_status_internal_name=l_emp_bucket[3]["l_status_internal_name"])
            self.ac_bucket_status_set(internal_bucket_name=l_emp_bucket[4]["internal"], 
                l_status_internal_name=l_emp_bucket[4]["l_status_internal_name"])
            self.ac_bucket_status_set(internal_bucket_name=l_emp_bucket[5]["internal"], 
                l_status_internal_name=l_emp_bucket[5]["l_status_internal_name"])
        self.ac_bucket_role_set(role="employee", feature="task", l_bucket_internal_name=l_task_bucket_name)

        l_emp_bucket = [
            {"internal": "employee_task_dashboard", "display": "Task Due", "l_status_internal_name": ["assigned", "in_progress"]}
        ]
        if create_bucket:
            for emp_bucket in l_emp_bucket:
                self.ac_bucket_create(internal_bucket_name=emp_bucket['internal'],
                    display_name=emp_bucket['display'], l_status_internal_name=emp_bucket['l_status_internal_name'])

    def create_direct_employee_task_buckets(self, create_bucket=True):
        l_emp_bucket = [
            {"internal": "direct_emp_preparation", "display": "Preparation", "l_status_internal_name": ["assigned", "in_progress"]},
            {"internal": "direct_emp_finalization", "display": "Finalization", "l_status_internal_name": ["info_pending", "client_review", "efile_auth"]},
            {"internal": "direct_emp_closure", "display": "Closure", "l_status_internal_name": ["efiled", "closed"]},
            {"internal": "direct_emp_extension", "display": "Extension", "l_status_internal_name": []},
            {"internal": "direct_emp_overview", "display": "Overview", "l_status_internal_name": []}
        ]
        l_emp_composite_status_name = []
        l_emp_change_status_name = ["assigned", "in_progress", "admin_review"]
        l_task_bucket_name = []
        #Preparation
        l_task_bucket_name.append(l_emp_bucket[0]["internal"])
        l_emp_composite_status_name += l_emp_bucket[0]["l_status_internal_name"]
        if self.ac_access_settings['direct_employee']['client_interaction']:
            #Finalization
            l_task_bucket_name.append(l_emp_bucket[1]["internal"])
            l_emp_composite_status_name += l_emp_bucket[1]["l_status_internal_name"]
            #Closure
            l_task_bucket_name.append(l_emp_bucket[2]["internal"])
            l_emp_composite_status_name += l_emp_bucket[2]["l_status_internal_name"]
            #Change states
            l_emp_change_status_name += ["info_pending", "client_review", "efile_auth", "efiled", "closed"]
        #Extension
        l_emp_bucket[3]["l_status_internal_name"] = l_emp_composite_status_name
        l_task_bucket_name.append(l_emp_bucket[3]["internal"])
        #Overview
        l_emp_bucket[4]["l_status_internal_name"] = l_emp_composite_status_name
        l_task_bucket_name.append(l_emp_bucket[4]["internal"])
        
        l_emp_bucket.append({"internal": "direct_emp_change_states", "display": "Direct Emp Change States", "l_status_internal_name": l_emp_change_status_name})

        if create_bucket: 
            for emp_bucket in l_emp_bucket:
                self.ac_bucket_create(internal_bucket_name=emp_bucket['internal'],
                    display_name=emp_bucket['display'], l_status_internal_name=emp_bucket['l_status_internal_name'])
        else:
            self.ac_bucket_status_set(internal_bucket_name=l_emp_bucket[3]["internal"], 
                l_status_internal_name=l_emp_bucket[3]["l_status_internal_name"])
            self.ac_bucket_status_set(internal_bucket_name=l_emp_bucket[4]["internal"], 
                l_status_internal_name=l_emp_bucket[4]["l_status_internal_name"])
            self.ac_bucket_status_set(internal_bucket_name=l_emp_bucket[5]["internal"], 
                l_status_internal_name=l_emp_bucket[5]["l_status_internal_name"])
        self.ac_bucket_role_set(role="direct_employee", feature="task", l_bucket_internal_name=l_task_bucket_name) 

        l_emp_bucket = [
            {"internal": "direct_employee_task_dashboard", "display": "Task Due", "l_status_internal_name": ["assigned", "in_progress"]}
        ]
        if create_bucket:
            for emp_bucket in l_emp_bucket:
                self.ac_bucket_create(internal_bucket_name=emp_bucket['internal'],
                    display_name=emp_bucket['display'], l_status_internal_name=emp_bucket['l_status_internal_name'])
    
    def create_due_date_show_task_buckets(self):
        l_due_date_bucket = [
            {"internal": "due_date_states", "display": "Due Date States", "l_status_internal_name": ["assigned", "in_progress", "mgr_review", "admin_review"]}
        ]

        l_task_bucket_name = []
        for due_date_bucket in l_due_date_bucket:
            self.ac_bucket_create(internal_bucket_name=due_date_bucket["internal"],
                display_name=due_date_bucket["display"], l_status_internal_name=due_date_bucket["l_status_internal_name"])
            l_task_bucket_name.append(due_date_bucket["internal"])

    def create_client_task_buckets(self):
        l_client_bucket = [
            {"internal": "client_facing_states", "display": "Client Facing States", "l_status_internal_name": [
                "initial", "in_progress", "info_pending", "client_review", "efile_auth", "efiled", "closed"
            ]}
        ]
        l_task_bucket_name = []
        for client_bucket in l_client_bucket:
            self.ac_bucket_create(internal_bucket_name=client_bucket["internal"],
                display_name=client_bucket["display"], l_status_internal_name=client_bucket["l_status_internal_name"])
            l_task_bucket_name.append(client_bucket["internal"])
        self.ac_bucket_role_set(role="client", feature="task", l_bucket_internal_name=l_task_bucket_name)

    def create_manual_client_task_buckets(self):
        l_client_bucket = [
            {"internal": "manual_task_client_facing_states", "display": "Client Facing States", "l_status_internal_name": [
                "initial", "in_progress", "info_pending", "client_review", "closed"
            ]}
        ]
        l_task_bucket_name = []
        for client_bucket in l_client_bucket:
            self.ac_bucket_create(internal_bucket_name=client_bucket["internal"],
                display_name=client_bucket["display"], l_status_internal_name=client_bucket["l_status_internal_name"])
            l_task_bucket_name.append(client_bucket["internal"])
        self.ac_bucket_role_set(role="client", feature="manual_task", l_bucket_internal_name=l_task_bucket_name)

    def create_task_buckets(self):
        self.create_admin_task_buckets()
        self.create_recep_task_buckets()
        self.create_manager_task_buckets()
        self.create_employee_task_buckets()
        self.create_direct_employee_task_buckets()
        self.create_due_date_show_task_buckets()
        self.create_client_task_buckets()

    def create_manual_task_buckets(self):
        self.create_admin_manual_task_buckets()
        self.create_manager_manual_task_buckets()
        self.create_employee_manual_task_buckets()
        self.create_direct_employee_manual_task_buckets()
        self.create_recep_manual_task_buckets()
        self.create_manual_client_task_buckets()

    def create_admin_insight_buckets(self):
        l_admin_insight_bucket = [
            {"internal": "admin_insight_cpa_pending", "display": "Admin Task", "l_status_internal_name": ["initial", "admin_review"]},
            {"internal": "admin_insight_emp_followup", "display": "Team Task", "l_status_internal_name": ["assigned", "in_progress", "mgr_review"]},
            {"internal": "admin_insight_client_followup", "display": "Client Finalization", "l_status_internal_name": ["info_pending", "client_review", "efile_auth"]},
            {"internal": "admin_insight_client_filing_status", "display": "Client Finalized", "l_status_internal_name": ["efiled", "closed"]}
        ]

        l_insight_bucket_name = []
        for admin_insight_bucket in l_admin_insight_bucket:
            self.ac_bucket_create(internal_bucket_name=admin_insight_bucket['internal'],
                display_name=admin_insight_bucket['display'], l_status_internal_name=admin_insight_bucket['l_status_internal_name'])
            l_insight_bucket_name.append(admin_insight_bucket['internal'])
        self.ac_bucket_role_set(role="admin", feature="insight", l_bucket_internal_name=l_insight_bucket_name)

    def create_insight_buckets(self):
        self.create_admin_insight_buckets()

    def set_default_status_config(self):
        l_status_obj = [
            {"internal": "initial", "display": "Initial"},
            {"internal": "assigned", "display": "Assigned"},
            {"internal": "in_progress", "display": "In Progress"},
            {"internal": "mgr_review", "display": "Mgr Review"},
            {"internal": "admin_review", "display": "Admin Review"},
            {"internal": "info_pending", "display": "Info Pending"},
            {"internal": "client_review", "display": "Client Review"},
            {"internal": "efile_auth", "display": "Efile Auth"},
            {"internal": "efiled", "display": "Efiled"},
            {"internal": "closed", "display": "Closed"}
        ]

        # Create all the possible status in the AdminConfig 
        for status_obj in l_status_obj:
            self.ac_status_create(internal_status_name=status_obj['internal'], display_name=status_obj['display'])
 
    def set_default_config(self):
        self.ac_status = []
        self.ac_bucket_status = []
        self.ac_bucket_status_role = {}
        self.ac_next_status_id = 1
        self.ac_next_bucket_id = 1
        self.set_default_status_config()
        self.create_task_buckets()
        self.create_insight_buckets()
        self.create_manual_task_buckets()

class AdminTemplate(models.Model, Bitmap):
    #Fields
    at_admin_id = models.IntegerField()
    at_cat_id = models.IntegerField()
    at_cat_name = models.CharField(max_length=1000)
    at_file_name = models.CharField(max_length=1000)
    at_upload_time = models.DateTimeField(default=timezone.now)
    flag = models.IntegerField(default=0)
    flag2 = models.IntegerField(default=0)

    def at_get_path(self):
        UPLOAD_DIR = list(Packaging.objects.all())[0].get_dir()
        return UPLOAD_DIR + str(self.at_admin_id) + "/templates"

    def at_add_file(self, file):
        path = self.at_get_path()
        if self.at_check_ext(file):
            if settings.USE_S3:
                path = os.path.join(path, str(self.id))
                if not default_storage.exists(path):
                    default_storage.save(path, file) 
                    return default_storage.exists(path)
                else:
                    return False
            else:
                if os.path.isdir(path) == False:
                    os.makedirs(path)
                fs = FileSystemStorage(location=path)
                filename = fs.save(str(self.id), file)
                if os.path.isfile(path + "/" + str(self.id)):
                    return True
                else:
                    return False
        else:
            return False

    def at_del_file(self):
        file_path = self.at_get_path() + "/" + str(self.id) 
        if settings.USE_S3:
            default_storage.delete(file_path)
        else:
            os.remove(file_path)

    def at_check_ext(self, file):
        allowed_extensions = ['pdf', 'txt', 'doc', 'docx', 'xls', 'xlsx', 'jpg', 'jpeg', 'png']
        file_extension = file.name.split(".")[-1]
        if file_extension.lower() in allowed_extensions:
            return True
        else:
            return False

class Admin(BaseAdmin):
    #Fields
    admin_company_name = models.CharField(max_length=1000, default="")
    admin_company_url = models.CharField(max_length=1000, default="")
    admin_timezone = models.CharField(max_length=1000, default="America/Los_Angeles")

    admin_logo_name = models.CharField(max_length=1000, default="")

    #Methods
    def __str__(self):
        return str(self.admin_full_name)

    def get_path(self):
        UPLOAD_DIR = list(Packaging.objects.all())[0].get_dir()
        return UPLOAD_DIR + str(self.pk)

    def get_logo_path(self):
        return self.get_path() + "/logo/"

    def add_logo(self, file):
        path = self.get_logo_path()
        if self.check_ext(file):
            if settings.USE_S3:
                path = os.path.join(path, str(self.id))
                if not default_storage.exists(path):
                    default_storage.save(path, file) 
                    return default_storage.exists(path)
                else:
                    return False
            else:
                if os.path.isdir(path) == False:
                    os.makedirs(path)
                fs = FileSystemStorage(location=path)
                filename = fs.save(str(self.id), file)
                if os.path.isfile(path + "/" + str(self.id)):
                    return True
                else:
                    return False
        else:
            return False

    def check_ext(self, file):
        allowed_extensions = ['jpg', 'jpeg', 'png']
        file_extension = file.name.split(".")[-1]
        if file_extension.lower() in allowed_extensions:
            return True
        else:
            return False

    def del_logo(self):
        path = self.get_logo_path() + "/" + str(self.id)
        if settings.USE_S3:
            default_storage.delete(path)
        else:
            os.remove(path) 

    def get_logo_url(self):
        path = self.get_logo_path() + "/" + str(self.id)
        return default_storage.url(path)

    def set_esign(self):
        self.set_flag(5)

    def reset_esign(self):
        self.reset_flag(5)

    def check_esign(self):
        return self.is_flag_valid(5)

    def set_payment_merchant_acc(self):
        self.set_flag(6)

    def reset_payment_merchant_acc(self):
        self.reset_flag(6)

    def check_payment_merchant_acc(self):
        return self.is_flag_valid(6)

class User(BaseUser):
    #Spouse Information
    user_sp_full_name = models.CharField(max_length=1000, default="")
    user_sp_first_name = models.CharField(max_length=1000, default="")
    user_sp_last_name = models.CharField(max_length=1000, default="")
    user_sp_phone_num = models.CharField(max_length=128, default="")
    user_sp_email = models.CharField(max_length=1000, default="")

    """
    object repr for user_dependants:
    {
        "ud_id": number,
        "ud_type": string,
        "ud_full_name": string,
        "ud_first_name": string,
        "ud_last_name": string,
        "ud_email": string,
        "ud_phone_num": string,
    }
    """
    user_ud = models.JSONField(default=list)
    user_ud_index = models.IntegerField(default=0)

    #Methods
    def __str__(self):
        return str(self.user_full_name)

    def ud_add_spouse(self, ud_first, ud_last, ud_email, **kwargs):
        self.ud_add("Spouse", ud_first, ud_last, ud_email=ud_email, **kwargs)

    def ud_add(self, ud_type, ud_first, ud_last, **kwargs):
        ud_id = self.user_ud_index + 1

        d_ud = {
            "ud_id": ud_id,
            "ud_type": ud_type,
            "ud_full": ud_first + " " + ud_last,
            "ud_first": ud_first,
            "ud_last": ud_last,
        }

        if "ud_email" in kwargs:
            d_ud['ud_email'] = kwargs['ud_email']

        if "ud_phone_num" in kwargs:
            d_ud['ud_phone_num'] = kwargs['ud_phone_num']

        self.user_ud.append(d_ud)
        self.user_ud_index = ud_id

    def ud_lookup(self, ud_id):
        list_index = 0

        if ud_id > self.user_ud_index:
            return -1, None

        for ud_obj in self.user_ud:
            if ud_id == ud_obj.ud_id:
                return list_index, ud_obj
            list_index = list_index + 1

        return -1, None

    def ud_update(self, ud_id, **kwargs):
        index, ud_obj = self.ud_lookup(ud_id)

        if index == -1:
            return

        if "ud_first" in kwargs:
            ud_obj['ud_first'] = kwargs['ud_first']

        if "ud_last" in kwargs:
            ud_obj['ud_last'] = kwargs['ud_last']

        ud_obj['ud_full'] = ud_obj['ud_first'] + " " + ud_obj['ud_last']
        if "ud_email" in kwargs:
            ud_obj['ud_email'] = kwargs['ud_email']

        if "ud_phone_num" in kwargs:
            ud_obj['ud_phone_num'] = kwargs['ud_phone_num']

        self.user_ud[index] = ud_obj

    def ud_del(self, ud_id):
        index, ud_obj = self.ud_lookup(ud_id)

        if index == -1:
            return

        del self.user_ud[index]

    def get_path(self, admin_id, user_id, year, cat):
        UPLOAD_DIR = list(Packaging.objects.all())[0].get_dir()
        user_name = str(User.objects.get(user_admin_id=admin_id, id=user_id).user_full_name)
        admin_name = str(Admin.objects.get(id=admin_id).admin_full_name)
        path = UPLOAD_DIR  + str(str(admin_id) + "_" + str(admin_name)) + "/" + str(str(user_id) + "_" + str(user_name)) + "/" + str(year) + "/" + str(cat)
        return path

class Business(models.Model, Bitmap):
    # bns_type: soleprop lp llp llc c-corp s-corp non-profit
    # bns_incorp_state: It is logically a list for storing multiple states
    # services:
    # book-keeping (frequency: monthly, quarterly, yearly)
    # payroll (frequency: bi-monthly, monthly, quarterly, yearly)
    # sales tax (frequency: monthly, quarterly, yearly)
    # tax-planning (frequency: monthly, quarterly, yearly)
    #Fields
    bns_admin_id = models.IntegerField()
    bns_user_id = models.IntegerField()
    bns_user_name = models.CharField(max_length=1000)
    bns_name = models.CharField(max_length=1000)
    bns_type = models.IntegerField()
    bns_type_name = models.CharField(max_length=1000)
    bns_incorp_date = models.DateTimeField()
    bns_incorp_state = models.TextField(blank=True)
    bns_additional_state = models.TextField(blank=True)

    bns_bk_freq = models.IntegerField(default=0)
    bns_bk_task_tracking_id = models.IntegerField(default=0)

    bns_pr_freq = models.IntegerField(default=0)
    bns_pr_task_tracking_id = models.IntegerField(default=0)

    bns_st_freq = models.IntegerField(default=0)
    bns_st_task_tracking_id = models.IntegerField(default=0)

    bns_tp_freq = models.IntegerField(default=0)
    bns_tp_task_tracking_id = models.IntegerField(default=0)

    bns_create_time = models.DateTimeField(default=timezone.now)
    flag = models.IntegerField(default=0)
    flag2 = models.IntegerField(default=0)

    #Methods
    def __str__(self):
        str_1 = str()
        str_1 += "  admin_id: " + str(self.bns_admin_id)
        str_1 += "  user_id: " + str(self.bns_user_id)
        str_1 += "  name: " + str(self.bns_name)
        str_1 += "  type: " + str(self.bns_type)
        str_1 += "  incorp_date: " + str(self.bns_incorp_date)
        str_1 += "  incorp_state: " + str(self.bns_incorp_state)
        str_1 += "  incorp_additional_state: " + str(self.bns_additional_state)
        str_1 += "  create_time: " + str(self.bns_create_time)
        return str_1

    #BitMap: 1:Book-keeping 2:Payroll 3:SalesTax 4:Tax-Planning
    def set_book_keeping(self):
        self.set_flag(1)

    def reset_book_keeping(self):
        self.reset_flag(1)

    def check_book_keeping(self):
        return self.is_flag_valid(1)

    def set_payroll(self):
        self.set_flag(2)

    def reset_payroll(self):
        self.reset_flag(2)

    def check_payroll(self):
        return self.is_flag_valid(2)

    def set_sales_tax(self):
        self.set_flag(3)

    def reset_sales_tax(self):
        self.reset_flag(3)

    def check_sales_tax(self):
        return self.is_flag_valid(3)

    def set_tax_planning(self):
        self.set_flag(4)

    def reset_tax_planning(self):
        self.reset_flag(4)

    def check_tax_planning(self):
        return self.is_flag_valid(4)

    def add_additional_state(self, element):
        l_state = self.get_additional_state()
        if l_state is None or element not in l_state:
            if self.bns_additional_state:
                self.bns_additional_state = self.bns_additional_state + ";" + element
            else:
                self.bns_additional_state = element

    def delete_additional_state(self, element):
        if self.bns_additional_state:
            l_state = self.get_additional_state()
            try:
                l_state.remove(element)
            except ValueError:
                pass
            else:
                self.bns_additional_state = ""
                if len(l_state) != 0:
                    for state in l_state:
                        self.add_additional_state(state)

    def get_additional_state(self):
        if self.bns_additional_state:
            return self.bns_additional_state.split(";")
        else:
            None

class Employee(BaseEmployee):
    pass

class Files(models.Model, Bitmap):
    #Fields
    f_admin_id = models.IntegerField()
    f_user_id = models.IntegerField()
    f_bns_id = models.IntegerField(default=0)
    f_bns_name = models.CharField(max_length=1000, default="")
    f_cat_id = models.IntegerField()
    f_cat_name = models.CharField(max_length=1000)
    f_year = models.IntegerField()
    f_version = models.IntegerField(default=1)
    f_file_name = models.CharField(max_length=1000)

    f_signers = models.TextField()
    f_signers_status = models.TextField()

    f_file_cat_id = models.IntegerField()
    f_file_cat_name = models.CharField(max_length=1000)
    f_upload_time = models.DateTimeField(default=timezone.now)
    flag = models.IntegerField(default=0)
    flag2 = models.IntegerField(default=0)

    #Methods
    def __str__(self):
        return str(self.f_user_id)

    """
    set_upload_self - From Client
    UploadedAdminForUser - To Client
    set_uploaded_admin_only - Internal(Admin Only)
    set_upload_admin_employee - Internal(Team Only)
    
    """
    def set_upload_self(self):
        self.set_flag(1)

    def reset_upload_self(self):
        self.reset_flag(1)

    def check_upload_self(self):
        return self.is_flag_valid(1)

    def set_upload_admin_for_user(self):
        self.set_flag(2)

    def reset_upload_admin_for_user(self):
        self.reset_flag(2)

    def check_upload_admin_for_user(self):
        return self.is_flag_valid(2)

    def set_upload_admin_employee(self):
        self.set_flag(3)

    def reset_upload_admin_employee(self):
        self.reset_flag(3)

    def check_upload_admin_employee(self):
        return self.is_flag_valid(3)

    def set_uploaded_admin_only(self):
        self.set_flag(4)

    def reset_uploaded_admin_only(self):
        self.reset_flag(4)

    def check_uploaded_admin_only(self):
        return self.is_flag_valid(4)

    def set_uploaded_esign(self):
        self.set_flag(8)

    def reset_uploaded_esign(self):
        self.reset_flag(8)

    def check_uploaded_esign(self):
        return self.is_flag_valid(8)

    def set_admin_check(self):
        self.set_flag(5)

    def reset_admin_check(self):
        self.reset_flag(5)

    def check_admin_check(self):
        return self.is_flag_valid(5)

    def set_mgr_check(self):
        self.set_flag(6)

    def reset_mgr_check(self):
        self.reset_flag(6)

    def check_mgr_check(self):
        return self.is_flag_valid(6)

    def set_emp_check(self):
        self.set_flag(7)

    def reset_emp_check(self):
        self.reset_flag(7)

    def check_emp_check(self):
        return self.is_flag_valid(7)

    #Esign bits with third party
    def set_raised_for_esign(self):
        self.set_flag(9)

    def reset_raised_for_esign(self):
        self.reset_flag(9)

    def check_raised_for_esign(self):
        return self.is_flag_valid(9)

    def set_processing_esign(self):
        self.set_flag(10)

    def reset_processing_esign(self):
        self.reset_flag(10)

    def check_processing_esign(self):
        return self.is_flag_valid(10)

    def set_processing_cancel_esign(self):
        self.set_flag(14)

    def reset_processing_cancel_esign(self):
        self.reset_flag(14)

    def check_processing_cancel_esign(self):
        return self.is_flag_valid(14)

    def set_raised_fail_for_esign(self):
        self.set_flag(11)

    def reset_raised_fail_for_esign(self):
        self.reset_flag(11)

    def check_raised_fail_for_esign(self):
        return self.is_flag_valid(11)

    def set_client_signed_esign(self):
        self.set_flag(12)

    def reset_client_signed_esign(self):
        self.reset_flag(12)

    def check_client_signed_esign(self):
        return self.is_flag_valid(12)

    def set_all_signed_esign(self):
        self.set_flag(13)

    def reset_all_signed_esign(self):
        self.reset_flag(13)

    def check_all_signed_esign(self):
        return self.is_flag_valid(13)

    def set_lock(self):
        self.set_flag(15)

    def reset_lock(self):
        self.reset_flag(15)

    def check_lock(self):
        return self.is_flag_valid(15)

    def new_get_path(self):
        UPLOAD_DIR = list(Packaging.objects.all())[0].get_dir()
        return UPLOAD_DIR + str(self.f_admin_id) + "/taxdoc/" + str(self.f_user_id)

    def new_add_file(self, file):
        path = self.new_get_path()
        if self.check_ext(file):
            if settings.USE_S3:
                path = os.path.join(path, str(self.id))
                if not default_storage.exists(path):
                    default_storage.save(path, file)
                    return default_storage.exists(path)
                else:
                    return False
            else:
                if os.path.isdir(path) == False:
                    os.makedirs(path)
                fs = FileSystemStorage(location=path)
                filename = fs.save(str(self.id), file)
                if os.path.isfile(path + "/" + str(self.id)):
                    return True
                else:
                    return False
        else:
            return False

    def new_del_file(self):
        file_path = self.new_get_path() + "/" + str(self.id)
        if settings.USE_S3:
            default_storage.delete(file_path)
        else:
            os.remove(file_path)

    def check_ext(self, file):
        allowed_extensions = ['pdf', 'txt', 'doc', 'docx', 'xls', 'xlsx', 'jpg', 'jpeg', 'png', 'csv']
        file_extension = file.name.split(".")[-1]
        if file_extension.lower() in allowed_extensions:
            return True
        else:
            return False

    def get_file_name(self):
        if self.f_version > 1:
            l_file_name = self.f_file_name.split(".")
            new_file_name = str()
            i = 0
            for file_part in l_file_name:
                if len(l_file_name) - 1 == i:
                    new_file_name += " (" + str(self.f_version) + ")." + file_part
                else:
                    if i > 0:
                        new_file_name += "."
                    new_file_name += file_part
                i += 1
            return new_file_name
        return self.f_file_name

class UserTracking(models.Model, Bitmap):
    #Fields
    ut_admin_id = models.IntegerField()
    ut_user_id = models.IntegerField()
    ut_user_name = models.CharField(max_length=1000)
    ut_user_email = models.CharField(max_length=1000)
    ut_bns_id = models.IntegerField(default=0)
    ut_bns_name = models.CharField(max_length=1000, default="")
    ut_cat_id = models.IntegerField()
    ut_cat_name = models.CharField(max_length=1000)
    ut_year = models.IntegerField()

    ut_current_status = models.IntegerField(default=1)
    ut_current_status_name = models.CharField(max_length=1000)
    int_prev_status = models.IntegerField(default=1)
    int_prev_status_name = models.CharField(max_length=1000, default="")

    ut_status_updated_time = models.DateTimeField(default=timezone.now)
    ut_last_uploaded_time = models.DateTimeField(default=_set_default_upload_time)
    ut_assign_time = models.DateTimeField(default=timezone.now)

    ut_emp_assigned = models.IntegerField(default=0)
    ut_emp_assigned_name = models.CharField(max_length=1000, default="None")
    ut_mgr_assigned_name = models.CharField(max_length=1000, default="None")
    ut_mgr_assigned = models.IntegerField(default=0)
    int_prev_emp = models.IntegerField(default=0)
    int_prev_mgr = models.IntegerField(default=0)

    ut_due_date = models.DateTimeField(null=True, blank=True)
    ut_mgr_assigned_date = models.DateTimeField(null=True, blank=True)
    ut_emp_assigned_date = models.DateTimeField(null=True, blank=True)

    ut_estimated_price = models.IntegerField(default=0)
    ut_price_adjustments = models.IntegerField(default=0)
    flag = models.IntegerField(default=0)
    flag2 = models.IntegerField(default=0)

    #Methods
    def __str__(self):
        return str(self.ut_current_status_name)

    def get_due_info(self):
        l_status_to_show_color = get_status_id_from_bucket(self.ut_admin_id, "due_date_states")
        if self.ut_current_status in l_status_to_show_color and self.ut_due_date != None:
            if timezone.localtime(self.ut_due_date).date() < timezone.localtime(timezone.now()).date():
                return "overdue"
            elif timezone.localtime(self.ut_due_date).date() <= (timezone.localtime(timezone.now()).date() + dt.timedelta(days=2)):
                return "upcoming"
            else:
                return "none"
        else:
            return "none"

    def get_client_state(self):
        client_states = get_status_obj_from_bucket(self.ut_admin_id, "client_facing_states")
        last_relevant_state = client_states[0]["display_name"]
        for status_obj in client_states:
            if status_obj["id"] > self.ut_current_status:
                break
            last_relevant_state = status_obj["display_name"]
        return last_relevant_state

    def set_upload_complete(self):
        self.set_flag(1)

    def reset_upload_complete(self):
        self.reset_flag(1)
    
    def check_upload_complete(self):
        return self.is_flag_valid(1)

    def set_extension(self):
        self.set_flag(2)
    
    def reset_extension(self):
        self.reset_flag(2)

    def check_extension(self):
        return self.is_flag_valid(2)

    def set_eg_sent(self):
        self.set_flag(3)

    def reset_eg_sent(self):
        self.reset_flag(3)

    def check_eg_sent(self):
        return self.is_flag_valid(3)

    def set_eg_signed(self):
        self.set_flag(4)

    def reset_eg_signed(self):
        self.reset_flag(4)

    def check_eg_signed(self):
        return self.is_flag_valid(4)

    def set_last_uploaded_time(self):
        self.ut_last_uploaded_time = timezone.localtime(timezone.now())

    def set_status_updated_time(self):
        self.ut_status_updated_time = timezone.localtime(timezone.now())

    def get_status_updated_time(self):
        return self.ut_status_updated_time

    def get_current_status(self):
        return self.ut_current_status

    def set_current_status(self, status):
        self.ut_current_status = status

    def set_emp_assigned(self, emp):
        self.ut_emp_assigned = emp

    def get_emp_assigned(self):
        return self.ut_emp_assigned

    def set_assign_time(self):
        self.ut_assign_time = timezone.localtime(timezone.now())

class TaskFiles(BaseTaskFiles):
    def new_get_path(self):
        UPLOAD_DIR = list(Packaging.objects.all())[0].get_dir()
        return super().new_get_path(UPLOAD_DIR)

class TaskTracking(BaseTaskTracking):
    def get_template_type_str(self):
        if self.check_template_bk():
            return "Book-Keeping", "secondary"
        elif self.check_template_pr():
            return "Payroll", "danger"
        elif self.check_template_st():
            return "Sales Tax", "info"
        elif self.check_template_tp():
            return "Tax Planning", "primary"
        return "Misc", "success"

    def get_task_type_str(self):
        if self.check_instance_bk():
            return "Book-Keeping", "secondary"
        elif self.check_instance_pr():
            return "Payroll", "danger"
        elif self.check_instance_st():
            return "Sales Tax", "info"
        elif self.check_instance_tp():
            return "Tax Planning", "primary"
        elif self.check_instance_notice():
            return "Notice", "warning"
        return "Misc", "success"

    def get_client_state(self):
        client_states = get_status_obj_from_bucket(self.tt_admin_id, "manual_task_client_facing_states")
        last_relevant_state = client_states[0]["display_name"]
        for status_obj in client_states:
            if status_obj["id"] > self.tt_current_status:
                break
            last_relevant_state = status_obj["display_name"]
        return last_relevant_state

    def _create_project_from_template(self, due_date):
        status_obj = get_status_obj_from_internal_name(self.tt_admin_id, "assigned")
        super()._create_project_from_template(TaskTracking, due_date, status_obj)

    #Template Business Services
    def set_template_bk(self):
        self.set_flag(2)

    def reset_template_bk(self):
        self.reset_flag(2)

    def check_template_bk(self):
        return self.is_flag_valid(2)

    def set_template_pr(self):
        self.set_flag(3)

    def reset_template_pr(self):
        self.reset_flag(3)

    def check_template_pr(self):
        return self.is_flag_valid(3)

    def set_template_st(self):
        self.set_flag(4)

    def reset_template_st(self):
        self.reset_flag(4)

    def check_template_st(self):
        return self.is_flag_valid(4)

    def set_template_tp(self):
        self.set_flag(5)

    def reset_template_tp(self):
        self.reset_flag(5)

    def check_template_tp(self):
        return self.is_flag_valid(5)

    #Instance Business Serivces
    def set_instance_bk(self):
        self.set_flag(6)

    def reset_instance_bk(self):
        self.reset_flag(6)

    def check_instance_bk(self):
        return self.is_flag_valid(6)

    def set_instance_pr(self):
        self.set_flag(7)

    def reset_instance_pr(self):
        self.reset_flag(7)

    def check_instance_pr(self):
        return self.is_flag_valid(7)

    def set_instance_st(self):
        self.set_flag(8)

    def reset_instance_st(self):
        self.reset_flag(8)

    def check_instance_st(self):
        return self.is_flag_valid(8)

    def set_instance_tp(self):
        self.set_flag(9)

    def reset_instance_tp(self):
        self.reset_flag(9)

    def check_instance_tp(self):
        return self.is_flag_valid(9)

    def set_instance_notice(self):
        self.set_flag(10)

    def reset_instance_notice(self):
        self.reset_flag(10)

    def check_instance_notice(self):
        return self.is_flag_valid(10)

    def set_file_uploaded(self):
        self.set_flag(11)

    def reset_file_uploaded(self):
        self.reset_flag(11)

    def check_file_uploaded(self):
        return self.is_flag_valid(11)

class HistoryStatus(models.Model, Bitmap):
    #Fields
    hs_admin_id = models.IntegerField()
    hs_user_id = models.IntegerField()
    hs_bns_id = models.IntegerField(default=0)
    hs_bns_name = models.CharField(max_length=1000, default="")
    hs_cat_id = models.IntegerField()
    hs_year = models.IntegerField()
    hs_time = models.DateTimeField()
    hs_emp_id = models.IntegerField(default=0)
    hs_emp_name = models.CharField(max_length=1000, default="")
    hs_status = models.IntegerField(default=1)
    hs_status_name = models.CharField(max_length=1000)
    flag = models.IntegerField(default=0)
    flag2 = models.IntegerField(default=0)

    #Methods
    def __str__(self):
        return str(str(self.hs_user_id) + "-" + str(self.hs_year))

    def set_time(self, time):
        self.hs_time = time

    def get_client_state(self):
        client_states = get_status_obj_from_bucket(self.hs_admin_id, "client_facing_states")
        last_relevant_state = client_states[0]["display_name"]
        for status_obj in client_states:
            if status_obj["id"] > self.hs_status:
                break
            last_relevant_state = status_obj["display_name"]
        return last_relevant_state 

class Notifications(BaseNotifications):
    ntfy_batch_num_files = models.IntegerField(default=0)

    def set_value(self, identifier, value):
        already_set = super().set_value(identifier, value)
        mapping = {
            "num_files": "ntfy_batch_num_files",
        }
        if not already_set:
            setattr(self, mapping[identifier], value)

    def get_value(self, identifier, emp=None):
        process_value = super().get_value(identifier, emp)
        mapping = {
            "num_files": "ntfy_batch_num_files",
        }
        if process_value == None:
            return getattr(self, mapping[identifier])
        return process_value

    def increment(self, identifier, emp_exclude=None):
        already_set = super().increment(identifier, emp_exclude)
        mapping = {
            "num_files": "ntfy_batch_num_files"
        }
        if not already_set:
            prev_value = getattr(self, mapping[identifier])
            setattr(self, mapping[identifier], prev_value + 1)

    def decrement(self, identifier):
        already_set = super().decrement(identifier)
        mapping = {
            "num_files": "ntfy_batch_num_files"
        }
        if not already_set:
            prev_value = getattr(self, mapping[identifier])
            setattr(self, mapping[identifier], prev_value - 1)

    def clear(self, identifier, emp=None):
        already_set = super().clear(identifier, emp)
        mapping = {
            "num_files": "ntfy_batch_num_files"
        }
        if not already_set:
            setattr(self, mapping[identifier], 0)

    def set_send_file_email(self):
        if self.check_active():
            self.set_flag(1, 2)

    def reset_send_file_email(self):
        self.reset_flag(1, 2)

    def check_send_file_email(self):
        return self.is_flag_valid(1, 2)

    def set_send_task_email(self):
        if self.check_active():
            self.set_flag(2, 2)

    def reset_send_task_email(self):
        self.reset_flag(2, 2)

    def check_send_task_email(self):
        return self.is_flag_valid(2, 2)

    def reset_all_batch_triggers(self):
        super().reset_all_batch_triggers()
        self.reset_send_file_email()
        self.reset_send_task_email()

class Alert(BaseAlert):
    def get_resolved_alert_name(self, should_parse_source=True):
        alert_info = self.al_info.split("*")
        if len(alert_info) == 1:
            alert_info = alert_info[0]
        else:
            if should_parse_source:
                alert_info = [
                    {"type": "text", "value": alert_info[0]}, 
                    {"type": "link", "action": "sameWindow", 
                        "url": PROJECT_DASHBOARD.format(str(self.al_user_id), str(self.al_source_id)), "display": alert_info[1]},
                    {"type": "text", "value": alert_info[2]}
                ]
            else:
                alert_info = alert_info[0] + alert_info[1] + alert_info[2]
        return alert_info

class Messages(BaseMessages):
    pass

class TodoList(BaseTodoList):
    pass

class Appointments(BaseAppointments):
    pass

class ApplicationLeads(BaseApplicationLeads):
    def stringfy_firm_employee(self):
        if self.al_firm_employee == 1:
            return "1 - 2"
        elif self.al_firm_employee == 2:
            return "3 - 5"
        elif self.al_firm_employee == 3:
            return "6 - 8"
        elif self.al_firm_employee == 4:
            return "9 - 10"
        elif self.al_firm_employee == 5:
            return "10+"

    def stringfy_firm_clients(self):
        if self.al_firm_clients == 1:
            return "1 - 10"
        elif self.al_firm_clients == 2:
            return "11 - 25"
        elif self.al_firm_clients == 3:
            return "26 - 50"
        elif self.al_firm_clients == 4:
            return "51 - 100"
        elif self.al_firm_clients == 5:
            return "100+"

class Invoices(BaseInvoices):
    pass 

class SupportTickets(models.Model, Bitmap):
    st_admin_id = models.IntegerField()
    st_admin_full_name = models.CharField(max_length=1000)
    st_admin_email = models.CharField(max_length=100)
    st_subject = models.CharField(max_length=100)
    st_sent = models.TextField(default="")
    st_message = models.TextField(default="")
    st_time_stamp = models.TextField(default="")
    st_files = models.TextField(default="")
    st_create_date = models.DateTimeField(default=timezone.now)
    st_reply_date = models.DateTimeField(default=timezone.now)
    flag = models.IntegerField(default=0)
    flag2 = models.IntegerField(default=0)

    def set_close(self):
        self.set_flag(1)
    
    def reset_close(self):
        self.reset_flag(1)

    def check_close(self):
        return self.is_flag_valid(1)

    def set_admin_notif(self):
        self.set_flag(2)
    
    def reset_admin_notif(self):
        self.reset_flag(2)

    def check_admin_notif(self):
        return self.is_flag_valid(2)

    def set_super_admin_notif(self):
        self.set_flag(3)
    
    def reset_super_admin_notif(self):
        self.reset_flag(3)

    def check_super_admin_notif(self):
        return self.is_flag_valid(3)

    def set_sent(self, sent):
        self.st_sent = json.dumps(sent)

    def get_sent(self):
        return json.loads(self.st_sent)

    def append_sent(self, sent):
        if self.st_sent == str():
            self.set_sent([sent])
        else:
            l_sent = self.get_sent()
            l_sent.append(sent)
            self.set_sent(l_sent)

    def set_message(self, message):
        self.st_message = json.dumps(message)

    def get_message(self):
        return json.loads(self.st_message)

    def append_message(self, message):
        if self.st_message == str():
            self.set_message([message])
        else:
            l_message = self.get_message()
            l_message.append(message)
            self.set_message(l_message)

    def set_files(self, files):
        self.st_files = json.dumps(files)

    def get_files(self):
        if self.st_files == "":
            return [[]]
        return json.loads(self.st_files)

    def append_files(self, files):
        if self.st_files == str():
            self.set_files([files])
        else:
            l_l_files = self.get_files()
            l_l_files.append(files)
            self.set_files(l_l_files)

    def set_time_stamp(self, time_stamp):
        self.st_time_stamp = json.dumps(time_stamp)

    def get_time_stamp(self):
        return json.loads(self.st_time_stamp)

    def append_time_stamp(self, time_stamp):
        if self.st_time_stamp == str():
            self.set_time_stamp([time_stamp])
        else:
            l_time_stamp = self.get_time_stamp()
            l_time_stamp.append(time_stamp)
            self.set_time_stamp(l_time_stamp)

    def st_get_path(self, message_index):
        UPLOAD_DIR = list(Packaging.objects.all())[0].get_dir()
        return UPLOAD_DIR + str(self.st_admin_id) + "/support/" + str(self.id) + "/" + str(message_index)

    def st_add_file(self, message_index, file_index, file):
        path = self.st_get_path(message_index)
        if self.st_check_ext(file):
            if settings.USE_S3:
                path = os.path.join(path, str(file_index))
                if not default_storage.exists(path):
                    default_storage.save(path, file) 
                    return default_storage.exists(path)
                else:
                    return False
            else:
                if os.path.isdir(path) == False:
                    os.makedirs(path)
                fs = FileSystemStorage(location=path)
                filename = fs.save(str(file_index), file)
                if os.path.isfile(path + "/" + str(file_index)):
                    return True
                else:
                    return False
        else:
            return False 

    def st_del_file(self, message_index, file_index):
        file_path = self.st_get_path(message_index) + "/" + str(file_index)
        if settings.USE_S3:
            default_storage.delete(file_path)
        else:
            os.remove(file_path)

    def st_check_ext(self, file):
        allowed_extensions = ['pdf', 'txt', 'doc', 'docx', 'xls', 'xlsx', 'jpg', 'jpeg', 'png', 'csv']
        file_extension = file.name.split(".")[-1]
        if file_extension.lower() in allowed_extensions:
            return True
        else:
            return False

class LeadTracking(BaseLeadTracking):
    pass

class CmtyQues(BaseCmtyQues):
    pass

class BulkMsg(BaseBulkMsg):
    pass