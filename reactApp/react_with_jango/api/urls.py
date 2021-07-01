from django.urls import path,include
from .views import ArticleViewset, ArticleApiView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('view_article', ArticleViewset)

urlpatterns = [

    ##### this urls for ModelViewSet (mostly used for all ops)
    path('', include(router.urls)),

    #### this path for APIView
    # for all records
    path('api_article/', ArticleApiView.as_view()),
    ## for one record
    path('api_article/<int:pk>/', ArticleApiView.as_view()),



]