from rest_framework import serializers
from .models import Room,Article

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"

class CreateRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('guest_can_pause', 'votes_to_skip')

class ArticleSerializer(serializers.ModelSerializer):
    def to_representation(self, obj):
        data = super().to_representation(obj)
        data['title'] = obj.title
        data['author'] = obj.author
        data['email'] = obj.email
        return data

    class Meta:
        model = Article
        fields = ("id",)
        