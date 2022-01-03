"""Project33 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from Project33 import settings
from app33 import views
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',views.ShowMain.as_view(),name="main"),

    path('main/',TemplateView.as_view(template_name="index.html"),name="main"),

    path('add_new/',views.AddNewEmployee.as_view(),name="add_new"),

    path('view_all/',views.ViewAllEmployees.as_view(),name="view_all"),

    path('update_emp<int:pk>/',views.UpdateEmployee.as_view(),name="update_emp"),

    path('delete_emp<int:pk>/',views.DeleteEmployee.as_view(),name="delete_emp"),

    path('view_complete_emp<int:pk>/',views.ViewComplete.as_view(),name="view_complete_emp"),

    path('openFB/',views.OpenFacebook.as_view(),name="openFB"),

    path('user_register/',views.UserRegsiter.as_view(),name="user_register"),

    path('user_login/',TemplateView.as_view(template_name="login.html"),name="user_login"),

    path('login_check/',views.LoginCheck.as_view(),name="login_check"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
