from django.urls import path
from app1 import views
app_name = 'scmapp'

urlpatterns = [
    path('registration', views.index),
    path('user_home/', views.user_home),
    path('test', views.test, name='test'),
    path('login_user', views.login_user, name='login_user'),
    path('admin_login', views.admin_login, name='admin_login'),
    path('login_admin', views.login_admin, name='login_admin'),
    path('admin_home', views.admin_home, name='admin_home'),
    path('user_home', views.user_home, name='user_home'),
    path('user_event', views.user_event, name='user_event'),
    path('ground_booking', views.ground_booking, name='ground_booking'),
    path('db_ground_booking', views.db_ground_booking, name='db_ground_booking'),
    path('admin_booking', views.admin_booking, name='admin_booking'),
    path('admin_event', views.admin_event, name='admin_event'),
    path('update_event/(?P<id>\d+)/$', views.update_event, name='update_event'),
    path('db_update_event/(?P<id>\d+)/$',
         views.db_update_event, name='db_update_event'),
    path('db_delete_event/(?P<id>\d+)/$',
         views.db_delete_event, name='db_delete_event'),
    path('add_event', views.add_event, name='add_event'),
    path('db_add_event', views.db_add_event, name='db_add_event'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('admin_logout', views.admin_logout, name='admin_logout'),
]
