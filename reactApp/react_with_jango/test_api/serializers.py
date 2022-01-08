from .models import PersonModel
from rest_framework import serializers


class PersonSerializer(serializers.ModelSerializer):

    extra_test_fields = serializers.SerializerMethodField(
        method_name="test_fields")

    def to_representation(self, obj):
        data = super().to_representation(obj)
        print("data::", data, obj)
        data['name'] = obj.name
        data['age'] = obj.age
        data['gender'] = obj.gender
    # this context is extra field. we are passing from serializer
        data['extra_field'] = "extra_field"
        return data

    class Meta:
        model = PersonModel
        fields = "__all__"

# this is way to pass extra fields to object
    def test_fields(self, obj):
        return {"field1": "this is test field one", "field2": "this is test field two"}
