from rest_framework import serializers
from .models import ArticleModel

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleModel
        fields = ['id', 'title', 'description']


