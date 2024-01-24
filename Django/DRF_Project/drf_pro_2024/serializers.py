from .models import College,Student,Course
from rest_framework import serializers


class StudentSer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'college']



class CollegeSer(serializers.ModelSerializer):
    students = StudentSer(many= True, read_only= True).data
    class Meta:
        model = College
        fields = ['id', 'name', 'students']

    
    def to_representation(self, instance):
        data=  super().to_representation(instance)
        for key, val in data.items():
            if key == 'students':
                if val:
                    objs = Student.objects.all().filter(id__in=val).values()
                    data['students'] = objs
        return data

class CourseSer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = ['id', 'name', 'students']