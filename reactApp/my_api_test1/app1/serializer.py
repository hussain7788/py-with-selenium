from rest_framework import serializers
from app1.models import Student

class StudentSerializer(serializers.ModelSerializer):

    def to_representation(self, obj):
        data = super().to_representation(obj)
        print("data::", data)
        print("obj:::", obj)
        data['sname'] = obj.sname
        data['sage'] = obj.sage
    # this context is extra field. we are passing from serializer
        data['extra_field'] = "extra_field"
        return data

    class Meta:
        model = Student
        fields = "__all__"