from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework import viewsets

class StudentModelViewSet(viewsets.ModelViewSet):
 queryset = Student.objects.all()
 serializer_class = StudentSerializer
