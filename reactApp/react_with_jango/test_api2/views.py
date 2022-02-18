import json
from textwrap import indent
from typing import List
from django.http import JsonResponse
from django.shortcuts import get_list_or_404, get_object_or_404, render

from test_api2.models import Student
from rest_framework.response import Response
from .serializers import StudentSerializer
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView


class StudentGenericAPI(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # if we want to use filters from backend we need to use generics
    # these filters we need to set in backend settings.py file
    filterset_fields = ['name', 'age']


class StudentApiView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            try:
                obj = Student.objects.get(id=pk)
            except:
                return Response({"staus": "No Record Found"})
            else:
                ser = StudentSerializer(obj)
        else:
            m = Student.objects.all()
            ser = StudentSerializer(m, many=True)

            dt = json.dumps(ser.data, indent=4)
            f1 = open("test_api2/student.json", 'w')
            f1.write(dt)
            f1.close()
        return JsonResponse({"data": ser.data})

    def post(self, request):
        obj = StudentSerializer(data=request.data)
        if obj.is_valid():
            obj.save()
            return Response({"staus": "student added"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"staus": "Not added "}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        obj = Student.objects.get(id=pk)
        ser = StudentSerializer(instance=obj, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"staus": "student updated"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"staus": "Not updated "}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        try:
            obj = Student.objects.get(id=pk)
        except:
            return Response({"staus": "No Record Found"})
        else:
            obj.delete()
            return Response({"staus": f"{obj.name} deleted"}, status=status.HTTP_200_OK)
