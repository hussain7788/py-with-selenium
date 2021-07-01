from django.urls import path, include
from .views import index

urlpatterns = [
    path('', index),
    path('add', index),
    path('view', index),
    path('add_emp', index),
    path('view_emp', index),

]
