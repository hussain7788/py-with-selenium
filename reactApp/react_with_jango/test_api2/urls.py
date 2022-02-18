from rest_framework import routers
from django.urls import path, include
from .views import StudentApiView, StudentGenericAPI

urlpatterns = [
    path('student/', StudentApiView.as_view()),
    path('student/<int:pk>/', StudentApiView.as_view()),

    path("std/", StudentGenericAPI.as_view())


]
