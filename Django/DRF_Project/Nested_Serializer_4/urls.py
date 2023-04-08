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
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *

## these are the default imports from rest_framework documentation
router = DefaultRouter()
router.register('singer', SingerViewSet, basename='singer')
router.register('song', SongViewSet, basename='song')


urlpatterns = [

    path('', include(router.urls)),
    path('login/', include('rest_framework.urls'))
]