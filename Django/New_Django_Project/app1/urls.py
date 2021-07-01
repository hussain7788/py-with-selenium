from django.urls import path

from .views import *
from django.views.generic import TemplateView
urlpatterns = [
    path('index/', TemplateView.as_view(template_name="index.html"), name='index'),
    path('add_product/', add_product, name="add_product"),
    path("save_product/", save_product, name="save_product"),
    path("delete_product/", delete_product, name="delete_product"),
    ## use same argument to the function also
    path("update_form/<int:id_no>/", update_form, name="update_form"),
    path("save_updated_pro/", save_updated_pro, name="save_updated_pro"),

    ##########
    path('add_emp/', add_emp.as_view(), name="add_emp"),
    path('view_emp/', view_emp.as_view(), name="view_emp"),
    path('update_emp<int:pk>/', update_emp.as_view(), name="update_emp"),
    path('delete_emp<int:pk>/', delete_emp.as_view(), name="delete_emp"),
    path('user_reg', user_reg, name="user_reg"),
    path('user_login', user_login, name="user_login"),
    path('email_valid', email_valid, name="email_valid"),
    path('user_profile', user_profile, name="user_profile"),
    path('add_person_data/', add_person_data, name="add_person_data"),
    path("delete_records/", delete_records, name="delete_records")







]
