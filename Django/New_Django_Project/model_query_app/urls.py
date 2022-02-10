from django.urls import path, include
from .views import index, movies_api_data


urlpatterns = [
    path('', index, name="index"),
    path("movies_api_data/", movies_api_data, name="movies_api_data")
]
