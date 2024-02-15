from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [
    path("students/", StudentAPIView.as_view()),
    path("students/<int:pk>/", StudentAPIView.as_view()),
    path("college/", CollegeAPIView.as_view()),
    path("college/<int:pk>/", CollegeAPIView.as_view()),
    path("course/", CourseAPIView.as_view()),
    path("course/<int:pk>/", CourseAPIView.as_view()),
    path('gettoken/', TokenObtainPairView.as_view()),
    path('refresh_token/', TokenRefreshView.as_view()),
    path('verify_token/', TokenVerifyView.as_view()),
    path('sample/', sample, name='sample'),
    path("upload/", uploadFile.as_view())
]