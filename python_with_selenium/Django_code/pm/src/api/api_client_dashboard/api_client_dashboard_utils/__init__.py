# Importing all the private modules
from pm.src.api.api_client_dashboard.api_client_dashboard_utils.documents import (
    _client_dashboard_doc_tab_config, _client_dashboard_doc,
    _client_dashboard_doc_upload_config, _client_dashboard_doc_upload,
    _client_dashboard_doc_check, _client_dashboard_doc_delete, _client_dashboard_doc_business,
    _client_dashboard_get_esign_info, _client_dashboard_raise_esign, _client_dashboard_get_sign_url,
    _client_dashboard_cancel_esign, _client_dashboard_doc_lock_unlock
)
from pm.src.api.api_client_dashboard.api_client_dashboard_utils.dashboard import (
    _client_dashboard_active_engagements, _client_dashboard_messages,
    _client_dashboard_messages_process, _client_dashboard_todo, _client_dashboard_todo_switch_state,
    _client_dashboard_todo_process, _client_dashboard_client_info, _client_dashboard_notes,
    _client_dashboard_notes_process, _client_dashboard_upload_complete_process, _client_dashboard_extension_process,
    _client_dashboard_alerts, _client_dashboard_client_referral
)

from pm.src.api.api_client_dashboard.api_client_dashboard_utils.business import (
    _client_dashboard_business, _client_dashboard_business_add_config,
    _client_dashboard_business_add, _client_dashboard_business_business_details
)

from pm.src.api.api_client_dashboard.api_client_dashboard_utils.status import (
    _client_dashboard_status, _client_dashboard_status_tab_config, _client_dashboard_status_process,
    _client_dashboard_history_status
)

from pm.src.api.api_client_dashboard.api_client_dashboard_utils.invoice import (
    _fetch_invoices, _fetch_invoice_details, _add_invoices, _pay_invoice_details, _pay_invoice_create_payment_intent
)

from pm.src.utils.utils_common import get_rest_status

from pm.models import User

from rest_framework.response import Response
from rest_framework import status

import pdb


def _verify_user(request):
    admin_id = request.session['admin_id']
    if 'user_id' in request.query_params:
        user_id = request.query_params['user_id']
        try:
            User.objects.get(user_admin_id=admin_id, id=user_id)
        except User.DoesNotExist:
            return False
        else:
            return True
    else:
        return True


def client_dashboard(request):
    if 'role' in request.session:
        if request.session['role'] != "user" and _verify_user(request) == False:
            return Response({}, status=status.HTTP_401_UNAUTHORIZED)
        if (request.session['role'] == "admin" or request.session['role'] == "manager" or
            request.session['role'] == "employee" or request.session['role'] == "direct_employee" or
                request.session['role'] == "recep" or request.session['role'] == "user"):
            if request.query_params['section'] == "active_engagements":
                return Response(_client_dashboard_active_engagements(request), status=status.HTTP_200_OK)
            if request.query_params['section'] == "alerts":
                return Response(_client_dashboard_alerts(request), status=status.HTTP_200_OK)
            elif request.query_params['section'] == "todo":
                return Response(_client_dashboard_todo(request), status=status.HTTP_200_OK)
            elif request.query_params['section'] == "client_info":
                return Response(_client_dashboard_client_info(request), status=status.HTTP_200_OK)
            elif request.query_params['section'] == "client_notes":
                return Response(_client_dashboard_notes(request), status=status.HTTP_200_OK)
            elif request.query_params['section'] == "status_tab_config":
                return Response(_client_dashboard_status_tab_config(request), status=status.HTTP_200_OK)
            elif request.query_params['section'] == "status":
                return Response(_client_dashboard_status(request), status=status.HTTP_200_OK)
            elif request.query_params['section'] == "history_status":
                return Response(_client_dashboard_history_status(request), status=status.HTTP_200_OK)
            elif request.query_params['section'] == "document_tab_config":
                return Response(_client_dashboard_doc_tab_config(request), status=status.HTTP_200_OK)
            elif request.query_params['section'] == "doc_business":
                return Response(_client_dashboard_doc_business(request), status=status.HTTP_200_OK)
            elif request.query_params['section'] == "documents":
                """
                Query params
                cat: category
                upload_type: Inner Tab of Documents
                """
                return Response(_client_dashboard_doc(request), status=status.HTTP_200_OK)
            elif request.query_params['section'] == "documents_esign_info":
                status_code, data = _client_dashboard_get_esign_info(request)
                return Response(data, status=get_rest_status(status_code))
            elif request.query_params['section'] == "documents_sign_url":
                status_code, data = _client_dashboard_get_sign_url(request)
                return Response(data, status=get_rest_status(status_code))
            elif request.query_params['section'] == "upload_config":
                return Response(_client_dashboard_doc_upload_config(request), status=status.HTTP_200_OK)
            elif request.query_params['section'] == "messages":
                """
                Query params
                type: ('client', 'team') - For Client and Team Messages respectively
                """
                return Response(_client_dashboard_messages(request), status=status.HTTP_200_OK)
            elif request.query_params['section'] == "business":
                """
                No Additional Query params
                """
                return Response(_client_dashboard_business(request), status=status.HTTP_200_OK)
            elif request.query_params['section'] == "business_config":
                """
                No Additional Query params
                """
                return Response(_client_dashboard_business_add_config(request), status=status.HTTP_200_OK)
            elif request.query_params['section'] == "business_details":
                status_code, data = _client_dashboard_business_business_details(
                    request)
                return Response(data, status=get_rest_status(status_code))
            elif request.query_params['section'] == "invoice_fetch":
                status_code, data = _fetch_invoices(request)
                return Response(data, status=get_rest_status(status_code))
            elif request.query_params['section'] == "invoice_details_fetch":
                status_code, data = _fetch_invoice_details(request)
                return Response(data, status=get_rest_status(status_code))
            elif request.query_params['section'] == "invoice_pay_details_fetch":
                status_code, data = _pay_invoice_details(request)
                return Response(data, status=get_rest_status(status_code))
            else:
                raise NotImplementedError()
        else:
            return Response({}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        return Response({}, status=status.HTTP_401_UNAUTHORIZED)


def client_dashboard_post(request):
    if 'role' in request.session:
        if request.session['role'] != "user" and _verify_user(request) == False:
            return Response({}, status=status.HTTP_401_UNAUTHORIZED)
        if (request.session['role'] == "admin" or request.session['role'] == "manager" or
            request.session['role'] == "employee" or request.session['role'] == "direct_employee" or
                request.session['role'] == "recep" or request.session['role'] == "user"):
            if request.query_params['section'] == "documents":
                status_code, data = _client_dashboard_doc_upload(request)
                return Response(data, status=get_rest_status(status_code))
            elif request.query_params['section'] == "documents_check":
                status_code, data = _client_dashboard_doc_check(request)
                return Response(data, status=get_rest_status(status_code))
            elif request.query_params['section'] == "documents_delete" and request.session['role'] == "admin":
                status_code, data = _client_dashboard_doc_delete(request)
                return Response(data, status=get_rest_status(status_code))
            elif request.query_params['section'] == "documents_raise_esign":
                status_code, data = _client_dashboard_raise_esign(request)
                return Response(data, status=get_rest_status(status_code))
            elif request.query_params['section'] == "documents_cancel_esign":
                status_code, data = _client_dashboard_cancel_esign(request)
                return Response(data, status=get_rest_status(status_code))
            elif request.query_params['section'] == "documents_toggle_lock":
                status_code, data = _client_dashboard_doc_lock_unlock(request)
                return Response(data, status=get_rest_status(status_code))
            elif request.query_params['section'] == "todo_switch_state":
                status_code, data = _client_dashboard_todo_switch_state(
                    request)
                return Response(data, status=get_rest_status(status_code))
            elif request.query_params['section'] == "client_notes":
                status_code, data = _client_dashboard_notes_process(request)
                return Response(data, status=get_rest_status(status_code))
            elif request.query_params['section'] == "status":
                status_code, data = _client_dashboard_status_process(request)
                return Response(data, status=get_rest_status(status_code))
            elif request.query_params['section'] == "upload_complete":
                status_code, data = _client_dashboard_upload_complete_process(
                    request)
                return Response(data, status=get_rest_status(status_code))
            elif request.query_params['section'] == "extension":
                status_code, data = _client_dashboard_extension_process(
                    request)
                return Response(data, status=get_rest_status(status_code))
            elif request.query_params['section'] == "message":
                status_code, data = _client_dashboard_messages_process(request)
                return Response(data, status=get_rest_status(status_code))
            elif request.query_params['section'] == "todo":
                status_code, data = _client_dashboard_todo_process(request)
                return Response(data, status=get_rest_status(status_code))
            elif request.query_params['section'] == "business":
                status_code, d_rv = _client_dashboard_business_add(request)
                return Response(d_rv, status=get_rest_status(status_code))
            elif request.query_params['section'] == "invoice_add":
                status_code, data = _add_invoices(request)
                return Response(data, status=get_rest_status(status_code))
            elif request.query_params['section'] == "client_referral":
                status_code, data = _client_dashboard_client_referral(request)
                return Response(data, status=get_rest_status(status_code))
            elif request.query_params['section'] == "invoice_create_payment_intent":
                status_code, data = _pay_invoice_create_payment_intent(request)
                return Response(data, status=get_rest_status(status_code))
            else:
                raise NotImplementedError()
        else:
            return Response({}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        return Response({}, status=status.HTTP_401_UNAUTHORIZED)
