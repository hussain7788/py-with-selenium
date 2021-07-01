from django.db.models import fields
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
    extra_field_method = serializers.SerializerMethodField(method_name="get_field")
    def to_representation(self, obj):
        data = super().to_representation(obj)
        print("data::",data, obj)
        data['title'] = obj.title
        data['author'] = obj.author
        data['email'] = obj.email
    # this context is extra field. we are passing from serializer
        data['extra_field'] = "extra"
        return data

    class Meta:
        model = Article
        fields = "__all__"
    
    def get_field(self, ser_obj):
        return "sample field"



        