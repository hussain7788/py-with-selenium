import pm.src.api.api_client_dashboard.api_client_dashboard_utils as client_dashboard_module
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from rest_framework.views import APIView


class ClientDashboard(APIView):
    def get(self, request, format=None):
        return client_dashboard_module.client_dashboard(request)

    @method_decorator(csrf_protect)
    def post(self, request, format=None):
        return client_dashboard_module.client_dashboard_post(request)
