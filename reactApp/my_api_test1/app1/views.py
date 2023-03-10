from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from app1.models import Student
from app1.serializer import StudentSerializer
from django.http import HttpResponse
from rest_framework.generics import ListAPIView

# Create your views here.

class StudentGenericAPI(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # if we want to use filters from backend we need to use generics
    # these filters we need to set in backend settings.py file
    filterset_fields = ['sname', 'sage']

class StudentAPIview(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            try:
                obj = Student.objects.get(id=pk)
            except:
                return Response({"Warning": "No Record Found"})
            else:
                ser = StudentSerializer(obj)
        else:
            obj = Student.objects.all()
            ser = StudentSerializer(obj, many=True)
            print("serialized data::::::::::")
            print(ser.data)
            import json
            with open("app1/test.json", 'w') as f:
                data = json.dump(ser.data, f, indent=4)
        return Response(ser.data) 

    def post(self, request):
        data = StudentSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return Response({"Success":"Data stored SUccessfully"})
        else:
            return Response({"Error":"Something error"})
    
    def put(self, request, pk=None, format=None):
        print("pkkkkkkkkkkkk::", pk)
        obj = Student.objects.get(id=pk)
        ser = StudentSerializer(obj, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"Success":"Updated SUccessfully"})
        else:
            return Response({"Error":"Something error"})
    
    def delete(self, request, pk=None):
        print("pk::::::::::", pk)
        obj = Student.objects.get(id=pk)
        obj.delete()
        return Response({obj.sname: "deleted"})
                                                                  


