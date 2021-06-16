"""Project17 URL Configuration

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
from django.contrib import admin
from django.urls import path

from app17 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.showIndex,name="main"),
    path('add_employee/',views.add_employee,name="add_employee"),
    path('save_emp/',views.save_emp,name="save_emp"),
    path('view_all/',views.view_all,name="view_all"),
    path('delete/',views.delete_employee,name="delete"),
    path('show_update/',views.show_update,name="show_update"),
    path('update_emp/',views.update_emp,name="update_emp"),
]
