from rest_framework import serializers
from pm.models import (
    UserTracking, Files, Business, File_types, Messages, US_States, Bns_types, TodoList,
    Employee, Admin, HistoryStatus, Invoices, Employee, TaskTracking, Alert, get_status_id_from_bucket
)

from pm.src.utils.utils_common import get_emp_list, get_status_obj_from_bucket
from pm.src.api.common.url_map import *

from django_esign.api_esign import get_signers_status

from django.urls import reverse
from django.utils.timezone import get_current_timezone
from django.conf import settings

from datetime import datetime
import pdb


def get_status_and_id_from_bucket(admin_id, internal_bucket_name):
    l_status = []
    l_status_id = []
    l_status_obj = get_status_obj_from_bucket(admin_id, internal_bucket_name)
    if l_status_obj == None:
        return None, None
    for status_obj in l_status_obj:
        l_status.append(status_obj["display_name"])
        l_status_id.append(status_obj["id"])
    return l_status, l_status_id


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'emp_full_name')


class AlertSerializer(serializers.ModelSerializer):
    def to_representation(self, obj):
        data = super().to_representation(obj)
        data['al_info'] = obj.get_resolved_alert_name()
        data['al_created_time'] = obj.al_created_time.astimezone(
            get_current_timezone()).strftime('%m-%d-%Y %I:%M %p')
        return data

    class Meta:
        model = Alert
        fields = ('id',)


class TaskTrackingSerializer(serializers.ModelSerializer):
    def to_representation(self, obj):
        data = super().to_representation(obj)
        if self.context['role'] == "user":
            data['tt_current_status_name'] = obj.get_client_state()
        data['tt_current_status_name'] = [{"type": "statusdot", "status": data['tt_current_status_name']}, {
            "type": "text", "value": data['tt_current_status_name']}]
        task_type_str, task_type_badge_type = obj.get_task_type_str()
        data['tt_task_name'] = [{"type": "text", "value": obj.tt_task_name}]
        data['tt_task_name'].append(
            {"type": "badge", "badgeType": task_type_badge_type, "value": task_type_str})
        if obj.tt_bns_id == 0:
            data['tt_bns_name'] = "-"
        return data

    class Meta:
        model = TaskTracking
        fields = ('id', 'tt_task_name', 'tt_bns_name',
                  'tt_current_status_name')


class InvoiceSerializer(serializers.ModelSerializer):
    def to_representation(self, obj):
        data = super().to_representation(obj)
        data['iv_raised'] = obj.iv_raised.astimezone(
            get_current_timezone()).strftime('%m-%d-%Y')
        data['iv_due_date'] = obj.iv_due_date.astimezone(
            get_current_timezone()).strftime('%m-%d-%Y')
        data['actionButton'] = [{"type": "button", "display": {
            "icon": "View Details"}, "action": "custom", "identifier": "viewDetails"}]
        if not obj.check_paid() and self.context['role'] == "user" and self.context['is_payment']:
            data['actionButton'].append(
                {"type": "button", "display": "Pay", "action": "newWindow", "url": INVOICE_PAY.format(str(obj.id))})
        return data

    class Meta:
        model = Invoices
        fields = ('id', 'iv_grand_total', 'iv_raised', 'iv_due_date')


class InvoiceDetailsSerializer(serializers.ModelSerializer):
    def to_representation(self, obj):
        data = super().to_representation(obj)
        data['invoice_date'] = obj.iv_raised.astimezone(
            get_current_timezone()).strftime('%Y-%m-%d')
        data['invoice_due_date'] = obj.iv_due_date.astimezone(
            get_current_timezone()).strftime('%Y-%m-%d')
        data['invoice_sales_tax'] = obj.iv_sales_tax_percent
        data['invoice_notes'] = obj.iv_notes
        data['invoice_payment_notes'] = obj.iv_payment_notes
        data['invoice_allow_edit'] = False
        if self.context['role'] == "admin":
            data['invoice_allow_edit'] = True
        data['invoice_payment_method'] = obj.iv_payment_method
        data['invoice_is_paid'] = obj.check_paid()
        data['description'] = obj.get_description()
        data['qty'] = obj.get_qty()
        data['price'] = obj.get_price()
        data['total_price'] = obj.get_total()
        data['payment_price'] = obj.iv_grand_total
        return data

    class Meta:
        model = Invoices
        fields = ('id',)


class UserTrackingPersonalSerializer(serializers.ModelSerializer):
    def to_representation(self, obj):
        data = super().to_representation(obj)
        data['uploadCompleteCheckbox'] = {"type": "checkbox", "checked": obj.check_upload_complete(
        ), "disabled": obj.check_upload_complete()}
        data['extensionCheckbox'] = {"type": "checkbox", "checked": obj.check_extension(
        ), "disabled": obj.check_extension()}
        if self.context['role'] == "user":
            data['ut_current_status_name'] = obj.get_client_state()
        data['ut_current_status_name'] = [{"type": "statusdot", "status": data['ut_current_status_name']}, {
            "type": "text", "value": data['ut_current_status_name']}]
        return data

    class Meta:
        model = UserTracking
        fields = ('id', 'ut_year', 'ut_mgr_assigned_name',
                  'ut_current_status_name', 'ut_due_date', 'ut_emp_assigned_name')


class UserTrackingBusinessSerializer(serializers.ModelSerializer):
    def to_representation(self, obj):
        data = super().to_representation(obj)
        data['uploadCompleteCheckbox'] = {"type": "checkbox", "checked": obj.check_upload_complete(
        ), "disabled": obj.check_upload_complete()}
        data['extensionCheckbox'] = {"type": "checkbox", "checked": obj.check_extension(
        ), "disabled": obj.check_extension()}
        if self.context['role'] == "user":
            data['ut_current_status_name'] = obj.get_client_state()
        data['ut_current_status_name'] = [{"type": "statusdot", "status": data['ut_current_status_name']}, {
            "type": "text", "value": data['ut_current_status_name']}]
        return data

    class Meta:
        model = UserTracking
        fields = ('id', 'ut_bns_name', 'ut_year', 'ut_mgr_assigned_name',
                  'ut_current_status_name', 'ut_due_date', 'ut_emp_assigned_name')


class PersonalFilesSerializer(serializers.ModelSerializer):
    def to_representation(self, obj):
        data = super().to_representation(obj)
        data['apCheckbox'] = {"type": "checkbox",
                              "checked": obj.check_admin_check(), "disabled": True}
        data['mpCheckbox'] = {"type": "checkbox",
                              "checked": obj.check_mgr_check(), "disabled": True}
        data['epCheckbox'] = {"type": "checkbox",
                              "checked": obj.check_emp_check(), "disabled": True}
        data['actionButton'] = [{"type": "button", "action": "newWindow", "display": {"icon": "View"},
                                 "id": str(str(obj.f_year) + "-" + obj.f_file_name + "-viewBtn"),
                                 "url": settings.SERVER_EFFECTIVE_HOST + reverse("pm:file_view", args=[obj.f_user_id, obj.id])},
                                {"type": "button", "action": "newWindow", "display": {"icon": "Download"},
                                 "id": str(str(obj.f_year) + "-" + obj.f_file_name + "-downloadBtn"),
                                 "url": settings.SERVER_EFFECTIVE_HOST + reverse("pm:file_download", args=[obj.f_user_id, obj.id])}]
        if self.context['role'] == "user" and obj.check_lock() and obj.check_upload_admin_for_user():
            data['actionButton'] = [
                {"type": "button", "action": "disabled", "display": "Locked"}]
        if self.context['role'] == "admin":
            data['apCheckbox']['disabled'] = False
            data['apCheckbox']['id'] = str(
                str(obj.f_year) + "-" + obj.f_file_name + "-checkbox")
            if not obj.check_uploaded_esign():
                data['actionButton'].append({"type": "button", "action": "custom", "display": {"icon": "Delete"},
                                             "id": str(str(obj.f_year) + "-" + obj.f_file_name + "-deleteBtn"),
                                             "identifier": "delete"})
        elif self.context['role'] == "manager":
            data['mpCheckbox']['disabled'] = False
            data['mpCheckbox']['id'] = str(
                str(obj.f_year) + "-" + obj.f_file_name + "-checkbox")
        elif self.context['role'] == "employee" or self.context['role'] == "direct_employee":
            data['epCheckbox']['disabled'] = False
            data['epCheckbox']['id'] = str(
                str(obj.f_year) + "-" + obj.f_file_name + "-checkbox")
        if obj.check_uploaded_admin_only():
            data['f_file_name'] = [{"type": "text", "value": data['f_file_name']}, {
                "type": "badge", "badgeType": "danger", "value": "Admin Only"}]
        data['f_upload_time'] = obj.f_upload_time.astimezone(
            get_current_timezone()).strftime('%m-%d-%Y %I:%M %p')
        if obj.check_uploaded_esign() and not (obj.check_raised_for_esign() or obj.check_processing_esign()) and self.context['is_esign'] and self.context['role'] != "user":
            data['actionButton'].append(
                {"type": "button", "action": "custom", "display": "Raise for Esign", "identifier": "raiseEsign"})
        if obj.check_uploaded_esign() and not obj.check_all_signed_esign() and self.context['is_esign'] and self.context['role'] != "user":
            data['actionButton'].append(
                {"type": "button", "action": "custom", "display": "Cancel Esign", "identifier": "cancelEsign"})
        if self.context['role'] == "user" and obj.check_raised_for_esign() and not obj.check_client_signed_esign():
            data['actionButton'].append(
                {"type": "button", "action": "custom", "display": "Sign Document", "identifier": "signEsign"})
        data['esign_status'] = ""
        if obj.check_raised_for_esign():
            params = dict()
            response = dict()
            params['esign_id'] = obj.pk
            get_signers_status({"hello_sign": params}, response)
            if response['hello_sign']['return_value'] and (len(response['hello_sign']['emails']) == len(response['hello_sign']['statuss'])):
                i = 0
                for email in response['hello_sign']['emails']:
                    parsed_status = ""
                    if response['hello_sign']['statuss'][i] == "signed":
                        parsed_status = "Signed"
                    elif response['hello_sign']['statuss'][i] == "awaiting_signature":
                        parsed_status = "Awaiting Signature"
                    else:
                        parsed_status = "Signer Status unavaliable"
                    if i > 0:
                        data['esign_status'] += "\n"
                    data['esign_status'] += email + ": " + parsed_status
                    i += 1
            else:
                data['esign_status'] = "Esign Request Raised"

        if obj.check_processing_esign():
            data['esign_status'] = "Esign Request is being processed"
        if obj.check_raised_fail_for_esign():
            data['esign_status'] = "Esign Request Declined/Invalid. Please try again"
        if obj.check_processing_cancel_esign():
            data['esign_status'] = "Esign Request queued to cancel"
        data['f_file_name'] = obj.get_file_name()
        if obj.check_uploaded_admin_only():
            data['f_file_name'] = [{"type": "text", "value": data['f_file_name']}, {
                "type": "badge", "badgeType": "danger", "value": "Admin Only"}]
        if self.context['can_toggle_lock'] and obj.check_upload_admin_for_user():
            if obj.check_lock():
                data['actionButton'].append({"type": "button", "action": "custom", "display": {
                                            "icon": "Unlock"}, "identifier": "unlock"})
            else:
                data['actionButton'].append({"type": "button", "action": "custom", "display": {
                                            "icon": "Lock"}, "identifier": "lock"})
        return data

    class Meta:
        model = Files
        fields = ('id', 'f_file_name', 'f_file_cat_name',
                  'f_year', 'f_upload_time', 'f_version')


class BusinessFilesSerializer(serializers.ModelSerializer):
    def to_representation(self, obj):
        data = super().to_representation(obj)
        data['apCheckbox'] = {"type": "checkbox",
                              "checked": obj.check_admin_check(), "disabled": True}
        data['mpCheckbox'] = {"type": "checkbox",
                              "checked": obj.check_mgr_check(), "disabled": True}
        data['epCheckbox'] = {"type": "checkbox",
                              "checked": obj.check_emp_check(), "disabled": True}
        data['actionButton'] = [{"type": "button", "action": "newWindow", "display": {"icon": "View"},
                                 "id": str(str(obj.f_year) + "-" + obj.f_file_name + "-viewBtn"),
                                 "url": settings.SERVER_EFFECTIVE_HOST + reverse("pm:file_view", args=[obj.f_user_id, obj.id])},
                                {"type": "button", "action": "newWindow", "display": {"icon": "Download"},
                                 "id": str(str(obj.f_year) + "-" + obj.f_file_name + "-downloadBtn"),
                                 "url": settings.SERVER_EFFECTIVE_HOST + reverse("pm:file_download", args=[obj.f_user_id, obj.id])}]
        if self.context['role'] == "user" and obj.check_lock() and obj.check_upload_admin_for_user():
            data['actionButton'] = [
                {"type": "button", "action": "disabled", "display": "Locked"}]
        if self.context['role'] == "admin":
            data['apCheckbox']['disabled'] = False
            data['apCheckbox']['id'] = str(
                str(obj.f_year) + "-" + obj.f_file_name + "-checkbox")
            data['actionButton'].append({"type": "button", "action": "custom", "display": {"icon": "Delete"},
                                         "id": str(str(obj.f_year) + "-" + obj.f_file_name + "-deleteBtn"),
                                         "identifier": "delete"})
        elif self.context['role'] == "manager":
            data['mpCheckbox']['disabled'] = False
            data['mpCheckbox']['id'] = str(
                str(obj.f_year) + "-" + obj.f_file_name + "-checkbox")
        elif self.context['role'] == "employee" or self.context['role'] == "direct_employee":
            data['epCheckbox']['disabled'] = False
            data['epCheckbox']['id'] = str(
                str(obj.f_year) + "-" + obj.f_file_name + "-checkbox")
        if obj.check_uploaded_admin_only():
            data['f_file_name'] = [{"type": "text", "value": data['f_file_name']}, {
                "type": "badge", "badgeType": "danger", "value": "Admin Only"}]
        data['f_upload_time'] = obj.f_upload_time.astimezone(
            get_current_timezone()).strftime('%m-%d-%Y %I:%M %p')
        if obj.check_uploaded_esign() and not (obj.check_raised_for_esign() or obj.check_processing_esign()) and self.context['is_esign'] and self.context['role'] != "user":
            data['actionButton'].append(
                {"type": "button", "action": "custom", "display": "Raise for Esign", "identifier": "raiseEsign"})
        if obj.check_uploaded_esign() and not obj.check_all_signed_esign() and self.context['is_esign'] and self.context['role'] != "user":
            data['actionButton'].append(
                {"type": "button", "action": "custom", "display": "Cancel Esign", "identifier": "cancelEsign"})
        if self.context['role'] == "user" and obj.check_raised_for_esign() and not obj.check_client_signed_esign():
            data['actionButton'].append(
                {"type": "button", "action": "custom", "display": "Sign Document", "identifier": "signEsign"})
        data['esign_status'] = ""
        if obj.check_raised_for_esign():
            params = dict()
            response = dict()
            params['esign_id'] = obj.pk
            get_signers_status({"hello_sign": params}, response)
            if response['hello_sign']['return_value'] and (len(response['hello_sign']['emails']) == len(response['hello_sign']['statuss'])):
                i = 0
                for email in response['hello_sign']['emails']:
                    parsed_status = ""
                    if response['hello_sign']['statuss'][i] == "signed":
                        parsed_status = "Signed"
                    elif response['hello_sign']['statuss'][i] == "awaiting_signature":
                        parsed_status = "Awaiting Signature"
                    else:
                        parsed_status = "Signer Status unavaliable"
                    if i > 0:
                        data['esign_status'] += "\n"
                    data['esign_status'] += email + ": " + parsed_status
                    i += 1
            else:
                data['esign_status'] = "Esign Request Raised"

        if obj.check_processing_esign():
            data['esign_status'] = "Esign Request is being processed"
        if obj.check_raised_fail_for_esign():
            data['esign_status'] = "Esign Request Declined/Invalid. Please try again"
        if obj.check_processing_cancel_esign():
            data['esign_status'] = "Esign Request queued to cancel"
        data['f_file_name'] = obj.get_file_name()
        if obj.check_uploaded_admin_only():
            data['f_file_name'] = [{"type": "text", "value": data['f_file_name']}, {
                "type": "badge", "badgeType": "danger", "value": "Admin Only"}]
        if self.context['can_toggle_lock'] and obj.check_upload_admin_for_user():
            if obj.check_lock():
                data['actionButton'].append({"type": "button", "action": "custom", "display": {
                                            "icon": "Unlock"}, "identifier": "unlock"})
            else:
                data['actionButton'].append({"type": "button", "action": "custom", "display": {
                                            "icon": "Lock"}, "identifier": "lock"})
        return data

    class Meta:
        model = Files
        fields = ('id', 'f_file_name', 'f_file_cat_name', 'f_year',
                  'f_upload_time', 'f_bns_name', 'f_version')


class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = ('id', 'bns_name')


class BusinessDisplaySerializer(serializers.ModelSerializer):
    def to_representation(self, obj):
        mapping = {0: "-", 1: "Monthly", 2: "Quarterly",
                   3: "Yearly", 4: "Bi-Monthly"}

        data = super().to_representation(obj)
        data['bns_bk_freq'] = mapping[obj.bns_bk_freq]
        data['bns_pr_freq'] = mapping[obj.bns_pr_freq]
        data['bns_st_freq'] = mapping[obj.bns_st_freq]
        data['bns_tp_freq'] = mapping[obj.bns_tp_freq]
        data['bns_incorp_date'] = obj.bns_incorp_date.strftime('%m-%d-%Y')
        data['ut_user_name'] = obj.bns_user_name
        data['ut_user_id'] = obj.bns_user_id
        if self.context['is_edit']:
            data['editButton'] = {"type": "button", "display": {
                "icon": "Edit"}, "action": "custom", "identifier": "editBusiness"}
        return data

    class Meta:
        model = Business
        fields = ('id', 'bns_user_id', 'bns_user_name', 'bns_name',
                  'bns_type', 'bns_incorp_date', 'bns_incorp_state', 'bns_type_name')


class USStatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = US_States
        fields = ('state_abbr',)


class BnsTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bns_types
        fields = ('id', 'bns_type_name',)


class FileTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = File_types
        fields = ('id', 'file_type_name')


class MessagesSerializer(serializers.ModelSerializer):
    """
    context {
        email: <email of the current user>
    }
    """

    def to_representation(self, obj):
        data = super().to_representation(obj)
        data['initials'] = obj.get_initials()
        data['is_curr_user'] = obj.ms_sent_email == self.context['email']
        data['ms_date_only'] = obj.ms_time.strftime('%Y-%m-%d')
        data['ms_time_only'] = obj.ms_time.strftime('%I:%M %p')
        return data

    class Meta:
        model = Messages
        fields = ('id', 'ms_message', 'ms_sent_email', 'ms_sent')


class TodoSerializer(serializers.ModelSerializer):
    def to_representation(self, obj):
        data = super().to_representation(obj)
        data['td_created_date'] = obj.td_time.astimezone(
            get_current_timezone()).strftime('%m/%d/%Y')
        data['is_completed'] = obj.check_completed()
        data['td_duedate'] = obj.td_duedate.astimezone(
            get_current_timezone()).strftime('%m/%d/%Y')
        if data['is_completed']:
            data['td_completed_date'] = obj.td_completed_date.strftime(
                '%m/%d/%Y')
        data['is_auto'] = obj.check_auto()
        if data['is_auto']:
            data['td_auto_tag_name'] = obj.td_tag
            data['td_auto_tag_css'] = obj.td_tag_css
        return data

    class Meta:
        model = TodoList
        fields = ('id', 'td_time', 'td_duedate',
                  'td_task', 'td_tag', 'td_tag_css',)


class HistoryStatusSerializer(serializers.ModelSerializer):
    def to_representation(self, obj):
        data = super().to_representation(obj)
        data['hs_time'] = obj.hs_time.strftime('%m-%d-%Y %I:%M %p')
        if self.context['role'] == "user":
            data['hs_status_name'] = obj.get_client_state()
        else:
            data['hs_emp_name'] = obj.hs_emp_name
        data['hs_status_name'] = [{"type": "statusdot", "status": data['hs_status_name']}, {
            "type": "text", "value": data['hs_status_name']}]
        return data

    class Meta:
        model = HistoryStatus
        fields = ('id', 'hs_status_name', 'hs_time')


class UserTrackingStatusSerializer(serializers.ModelSerializer):
    def get_eg_value(self, obj):
        return_value = "pending"
        if obj.check_eg_signed():
            return_value = "signed"
        elif obj.check_eg_sent():
            return_value = "sent"
        return return_value

    def to_representation(self, obj):
        data = super().to_representation(obj)
        if obj.ut_bns_id != 0:
            data['ut_action'] = [{"type": "button", "action": "custom", "display": {"icon": "History Status"},
                                  "id": str(str(obj.ut_year) + "-" + str(obj.ut_bns_name) + "-" + "historyStatus"),
                                  "identifier": "history_status"}]
        else:
            data['ut_action'] = [{"type": "button", "action": "custom", "display": {"icon": "History Status"},
                                  "id": str(str(obj.ut_year) + "-" + "historyStatus"),
                                  "identifier": "history_status"}]
        data['ut_eg_status'] = [
            {"type": "badge", "badgeType": "danger", "value": "Pending"}]
        if obj.check_eg_signed():
            data['ut_eg_status'] = [
                {"type": "badge", "badgeType": "success", "value": "Signed"}]
        elif obj.check_eg_sent():
            data['ut_eg_status'] = [
                {"type": "badge", "badgeType": "warning", "value": "Sent"}]
        data['ut_due_date'] = "No Due Date"
        if obj.ut_due_date != None:
            data['ut_due_date'] = obj.ut_due_date.astimezone(
                get_current_timezone()).strftime('%m-%d-%Y')
        if obj.ut_bns_id != 0:
            data['ut_bns_name'] = obj.ut_bns_name
        if self.context['role'] == "user":
            data['ut_current_status_name'] = [{"type": "statusdot", "status": obj.get_client_state()}, {
                "type": "text", "value": obj.get_client_state()}]
        else:
            data['ut_current_status_name'] = [{"type": "statusdot", "status": obj.ut_current_status_name}, {
                "type": "text", "value": obj.ut_current_status_name}]
        if self.context['is_edit'] == "true":
            if self.context['role'] == "manager":
                options, values = get_status_and_id_from_bucket(
                    obj.ut_admin_id, "mgr_change_states")
                is_show_list = get_status_id_from_bucket(
                    obj.ut_admin_id, "mgr_overview")
                if obj.ut_current_status in is_show_list:
                    data['ut_current_status_name'] = {"type": "dropdown", "options": options,
                                                      "values": values, "value": obj.ut_current_status}

                q_emp = Employee.objects.all().filter(emp_admin_id=obj.ut_admin_id, emp_mgr=self.context['emp_id']) | \
                    Employee.objects.all().filter(
                        emp_admin_id=obj.ut_admin_id, id=self.context['emp_id'])
                if q_emp.count() > 0:
                    data['ut_emp_assigned_name'] = {"type": "dropdown", "options": q_emp.values_list("emp_full_name"),
                                                    "values": q_emp.values_list("id"), "value": obj.ut_emp_assigned}

            elif self.context['role'] == "employee":
                options, values = get_status_and_id_from_bucket(
                    obj.ut_admin_id, "emp_change_states")
                is_show_list = get_status_id_from_bucket(
                    obj.ut_admin_id, "emp_overview")
                if obj.ut_current_status in is_show_list:
                    data['ut_current_status_name'] = {"type": "dropdown", "options": options,
                                                      "values": values, "value": obj.ut_current_status}
            elif self.context['role'] == "direct_employee":
                options, values = get_status_and_id_from_bucket(
                    obj.ut_admin_id, "direct_emp_change_states")
                is_show_list = get_status_id_from_bucket(
                    obj.ut_admin_id, "direct_emp_overview")
                if obj.ut_current_status in is_show_list:
                    data['ut_current_status_name'] = {"type": "dropdown", "options": options,
                                                      "values": values, "value": obj.ut_current_status}
            elif self.context['role'] == "admin":
                if obj.ut_due_date != None:
                    data['ut_due_date'] = {"type": "date", "value": obj.ut_due_date.astimezone(
                        get_current_timezone()).strftime('%Y-%m-%d')}
                options, values = get_status_and_id_from_bucket(
                    obj.ut_admin_id, "admin_change_states")
                data['ut_current_status_name'] = {"type": "dropdown", "options": options,
                                                  "values": values, "value": obj.ut_current_status}
                data['ut_eg_status'] = {"type": "dropdown", "options": ["Pending", "Sent", "Signed"],
                                        "values": ["pending", "sent", "signed"], "value": self.get_eg_value(obj)}
                admin_obj = Admin.objects.get(id=obj.ut_admin_id)
                q_emp_mgr = Employee.objects.all().filter(
                    id__in=get_emp_list(obj.ut_admin_id, 0, admin_mgr_emp=1))
                mgr_names = list(q_emp_mgr.values_list(
                    "emp_full_name", flat=True))
                mgr_names.insert(0, Admin.objects.get(
                    id=obj.ut_admin_id).admin_full_name)
                mgr_values = list(q_emp_mgr.values_list("id", flat=True))
                mgr_values.insert(0, 0)
                iter_mgr_values = mgr_values.copy()
                data['ut_emp_assigned_combination'] = list()
                i = 0
                for mgr_value in iter_mgr_values:
                    d_dropdown = None
                    if mgr_value == 0:
                        # Take all direct employees and managers
                        q_emp = Employee.objects.all().filter(
                            id__in=get_emp_list(obj.ut_admin_id, 0, admin_all_emp=1))
                    else:
                        # Employees of normal managers
                        q_emp = Employee.objects.all().filter(
                            emp_admin_id=obj.ut_admin_id, emp_mgr=mgr_value)
                    if mgr_value == obj.ut_mgr_assigned:
                        # This is the current active object and needs to be set in ut_emp_assigned_name
                        emp_options = list(q_emp.values_list(
                            "emp_full_name", flat=True))
                        emp_values = list(q_emp.values_list("id", flat=True))
                        if mgr_value == 0:
                            emp_options.append(admin_obj.admin_full_name)
                            emp_values.append(0)
                        if obj.ut_bns_id != 0:
                            d_dropdown = {"type": "dropdown", "options": emp_options, "values": emp_values,
                                          "id": str(str(obj.ut_year) + "-" + str(obj.ut_bns_name) + "-" + "emp"),
                                          "value": obj.ut_emp_assigned, "mgr_index": mgr_value}
                        else:
                            d_dropdown = {"type": "dropdown", "options": emp_options, "values": emp_values,
                                          "value": obj.ut_emp_assigned, "id": str(str(obj.ut_year) + "-" + "emp"), "mgr_index": mgr_value}
                        data['ut_emp_assigned_name'] = d_dropdown
                        data['ut_emp_assigned_combination'].append(d_dropdown)
                    if d_dropdown == None:
                        # dropdown dict needs to be set, so this is not the current active dropdown
                        emp_options = list(q_emp.values_list(
                            "emp_full_name", flat=True))
                        emp_values = list(q_emp.values_list("id", flat=True))
                        if mgr_value == 0:
                            emp_options.append(admin_obj.admin_full_name)
                            emp_values.append(0)

                        if len(emp_values) == 0:
                            mgr_names.pop(i)
                            mgr_values.pop(i)
                            i -= 1
                        else:
                            if obj.ut_bns_id != 0:
                                d_dropdown = {"type": "dropdown", "options": emp_options, "values": emp_values,
                                              "id": str(str(obj.ut_year) + "-" + str(obj.ut_bns_name) + "-" + "emp"),
                                              "value": emp_values[0], "mgr_index": mgr_value}
                            else:
                                d_dropdown = {"type": "dropdown", "options": emp_options, "values": emp_values, "id": str(str(obj.ut_year) + "-" + "emp"),
                                              "value": emp_values[0], "mgr_index": mgr_value}
                            data['ut_emp_assigned_combination'].append(
                                d_dropdown)
                    i += 1
                    if obj.ut_bns_id != 0:
                        data['ut_mgr_assigned_name'] = {"type": "dropdown", "options": mgr_names,
                                                        "id": str(str(obj.ut_year) + "-" + str(obj.ut_bns_name) + "-" + "mgr"),
                                                        "values": mgr_values, "value": obj.ut_mgr_assigned}
                    else:
                        data['ut_mgr_assigned_name'] = {"type": "dropdown", "options": mgr_names, "id": str(str(obj.ut_year) + "-" + "mgr"),
                                                        "values": mgr_values, "value": obj.ut_mgr_assigned}
        return data

    class Meta:
        model = UserTracking
        fields = ('id', 'ut_year', 'ut_mgr_assigned_name',
                  'ut_current_status_name', 'ut_emp_assigned_name')
