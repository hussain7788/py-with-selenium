from attr import dataclass
from rest_framework import serializers
from .models import Student

list_dict = [
    {"id": 2, "name": "hussain", "age": 23, "course": "python"},
    {"id": 3, "name": "valli", "age": 24, "course": "java"},
    {"id": 4, "name": "ajay", "age": 25, "course": "php"},
    {"id": 5, "name": "vijay", "age": 26, "course": "react"},

]


class StudentSerializer(serializers.ModelSerializer):

    extra_test_fields = serializers.SerializerMethodField(
        method_name="get_extra_fields")

    def to_representation(self, obj):
        data = super().to_representation(obj)
        data['name'] = obj.name
        data['age'] = obj.age
        data['course'] = obj.course
        return data

    class Meta:
        model = Student
        fields = "__all__"

    def get_extra_fields(self, obj):
        return {"field1": "save", "field2": "updated"}
