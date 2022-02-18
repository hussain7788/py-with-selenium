from rest_framework import routers
from django.urls import path, include

from .views import PersonModelViewSet, PersonApiView
router = routers.DefaultRouter()
router.register("p_view_set", PersonModelViewSet)


urlpatterns = [
    path('', include(router.urls)),

    path('p_api/', PersonApiView.as_view()),
    path('p_api/<int:pk>/', PersonApiView.as_view()),

]
