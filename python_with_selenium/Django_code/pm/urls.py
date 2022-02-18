from django.urls import path
from . import views
from pm.view import api
from django.conf import settings
from django.views.decorators.csrf import ensure_csrf_cookie

app_name = 'pm'
urlpatterns = [
    # Common functions used across by Admin/User/Employees
    path('file_view/<int:user_id>/<int:file_id>/',
         views.file_view, name="file_view"),
    path('file_download/<int:user_id>/<int:file_id>/',
         views.file_download, name="file_download"),
    path('task_file_view/<int:user_id>/<int:task_id>/<int:file_id>/',
         views.task_file_view, name="task_file_view"),
    path('task_file_download/<int:user_id>/<int:task_id>/<int:file_id>/',
         views.task_file_download, name="task_file_download"),
    path('template_file_view/<int:cat>/<str:file_name>/',
         views.template_file_view, name="template_file_view"),
    path('ticket_file_view/<int:ticket_id>/<int:message_index>/<int:file_index>/',
         views.ticket_file_view, name="ticket_file_view"),
    path('template_file_download/<int:cat>/<str:file_name>/',
         views.template_file_download, name="template_file_download"),

    ############################################################################
    # Third party url
    ############################################################################
    path('auth_google/', views.auth_google, name="auth_google"),
    path('post_auth_google/<str:success>/',
         views.post_auth_google, name="post_auth_google"),

    #path('auth_qbo/', views.auth_qbo, name="auth_qbo"),
    #path('post_auth_qbo/<str:success>/', views.post_auth_qbo, name="post_auth_qbo"),

    path('auth_stripe/', views.auth_stripe, name="auth_stripe"),
    path('stripe_refresh_url/', views.stripe_refresh_url,
         name="stripe_refresh_url"),
    path('stripe_return_url/', views.stripe_return_url, name="stripe_return_url"),

    path('pm_revoke_token/<str:service>/',
         views.pm_revoke_token, name="pm_revoke_token"),


    path('api/superadmin/', api.SuperAdmin.as_view()),
    path('api/dashboard/', api.Dashboard.as_view()),
    path('api/tasklist/', api.TaskList.as_view()),
    path('api/manualtasklist/', api.ManualTaskList.as_view()),
    path('api/userlist/', api.UserList.as_view()),
    path('api/emplist/', api.EmpList.as_view()),
    path('api/insight/', api.InsightList.as_view()),
    path('api/clientdashboard/', api.ClientDashboard.as_view()),
    path('api/add/', api.AddEndpoint.as_view()),
    path('api/settings/', api.Settings.as_view()),
    path('api/config/', ensure_csrf_cookie(api.GlobalConfig.as_view())),
    path('api/tickets/', api.Tickets.as_view()),
    path('api/leads/', api.LeadTracking.as_view()),
    path('api/calendar/', api.Calendar.as_view()),
    path('api/calendarfeed/', api.CalendarFeed.as_view()),
    path('api/authentication/', api.AuthenticationEndpoint.as_view()),
    path('api/billing/', api.Billing.as_view()),
    path('api/bulkmessages/', api.BulkMessages.as_view())
]
