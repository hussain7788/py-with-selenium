from django.shortcuts import render
from rest_framework import viewsets
from api.models import ArticleModel
from api.serializer import ArticleSerializer

# Create your views here.
class ArticleViews(viewsets.ModelViewSet):
    queryset = ArticleModel.objects.all()
    serializer_class = ArticleSerializer