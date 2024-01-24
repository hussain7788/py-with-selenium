"""DRF_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api_view/', include('CRUD_Apiview_1.urls')),
    path('jwt/', include('JWT_Token_2.urls')),
    path('auth/', include('All_Auth_Perm_3.urls')),
    path('ser/', include('Nested_Serializer_4.urls')),
    path('', include('drf_pro_2024.urls')),
    path('auth/', include('rest_framework.urls'))
    
]
