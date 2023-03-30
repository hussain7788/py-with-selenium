from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from .models import Student
from rest_framework.filters import OrderingFilter

class StudentList(ListAPIView):
 queryset = Student.objects.all()
 serializer_class = StudentSerializer
 filter_backends = [OrderingFilter]
 ordering_fields = ['name']
 # ordering_fields = ['name', 'city']
