from django.shortcuts import render
from rest_framework.views import APIView
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.response import Response

from rest_framework.viewsets import generics
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from .PG_ADMIN_FUNC_CALLS.database_calls import get_pg_func

# Create your views here.
data = [generics.CreateAPIView, generics.ListAPIView, generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView]


class EmployeeAPIView(APIView):

    def get(self, request, pk=None):
        get_pg_func()
        if pk is not None:
            try:
                obj = Employee.objects.get(id=pk)
            except:
                message = {"message":"No Data Found"}
                return Response(message)
            ser = EmployeeSerializer(obj).data
        else:
            obj = Employee.objects.all()
            ser = EmployeeSerializer(obj, many=True).data
        
        q_params = request.query_params
        print("q_params:::::::::::::::", q_params)
        if q_params:
            if 'name' in q_params:
                filter_objs = Employee.objects.filter(name=q_params['name'])
            ser = EmployeeSerializer(filter_objs, many= True).data

        return Response(ser)

    def post(self, request, format=None):
        obj = EmployeeSerializer(data=request.data)
        if obj.is_valid():
            obj.save()
            return Response({"message":"Employee Added"})
        else:
            return Response({"message":"Invalid Data"})

    def put(self, request, pk):
        obj = Employee.objects.get(id=pk)
        ser = EmployeeSerializer(obj, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"message":"Employee Updated."})
        else:
            return Response({"message":"Invalid Data"})
        
    def delete(self, request, pk):
        try:
            obj = Employee.objects.get(id=pk)
        except:
            return Response({"Record Not Found"})
        else:
            obj.delete()
            return Response({"message":"Employee Deleted"})