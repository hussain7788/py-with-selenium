from rest_framework import serializers
from .models import Student

# class StudentSerializer(serializers.ModelSerializer):
#  name = serializers.CharField(max_length=100)
#  roll = serializers.IntegerField()
#  city = serializers.CharField(max_length=100)

#  def create(self, validated_data):
#   return Student.objects.create(**validated_data)
 

#  def validate(self, data):
#   name = data.get('name')
#   roll = data.get('roll')
#   city = data.get('city')
#   if name == "hussain" and city != "kadapa":
#    raise serializers.ValidationError("City must be Kadapa")
#   return data

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


    def validate(self, attrs):
        import re
        name = attrs.get('name')
        city = attrs.get('city')
        # if name.startswith('h'):
        #     raise serializers.ValidationError("City must not startswith 'h' ")
        # if len(name) <8:
        #     raise serializers.ValidationError("name should contain atleast 8 charachers")
        res = re.match('^[a-zA-Z0-9]+$', name)
        if not res:
            raise serializers.ValidationError("name should contain atleast 8 charachers")
        return super().validate(attrs)