from django.urls import path, include
from .views import *

urlpatterns = [
    path("main/", main, name="main"),
    path("add/", add, name="add"),
    path('delete/', delete, name="delete"),
    path('update/', update, name="update")


]
