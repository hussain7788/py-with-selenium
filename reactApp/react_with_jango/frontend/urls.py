from django.urls import path, include
from .views import index

urlpatterns = [
    path('', index),
    path('add', index),
    path('view', index),

]
