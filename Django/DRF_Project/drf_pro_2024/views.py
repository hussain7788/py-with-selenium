from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import College,Student,Course, Company, Employee
from .serializers import CollegeSer, StudentSer,CourseSer
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser,AllowAny,IsAuthenticated
from django.db.models import Avg, Sum, Count, Min, Max, F
from django.db.models.functions import ExtractYear, ExtractMonth, ExtractDay
from rest_framework.parsers import FileUploadParser


# Create your views here.
class StudentAPIView(APIView):
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAdminUser]

    def get(self, request, pk=None, format=None):
        if pk is not None:
            try:
                obj = Student.objects.get(id=pk)
            except:
                error_msg = {"message": "Record Not Found"}
                return Response(error_msg)
            ser = StudentSer(obj)
            return Response({"data": ser.data}, status=200)
        objs = Student.objects.all()
        import pdb;pdb.set_trace()
        ser_objs = StudentSer(objs, many=True)
        return Response({"all_data": ser_objs.data},status=200)
    
    def delete(self, request, pk):
        if pk is not None:
            try:
                obj = Student.objects.get(id=pk)
            except:
                error_msg = {"message": "Record Not Found"}
                return Response(error_msg)
            obj.delete()
            return Response({"message": "Deleted Successfully"})
    
    def post(self, request, format=None):
        data = StudentSer(data=request.data)
        if data.is_valid():
            data.save()
            return Response({"Message": "saved"})
        else:
            return Response({"Message": "Invalid data"})

class CollegeAPIView(APIView):
    def get(self, request, pk=None, format=None):
        if pk is not None:
            try:
                obj = College.objects.get(id=pk)
            except:
                error_msg = {"message": "Record Not Found"}
                return Response(error_msg)
            import pdb;pdb.set_trace()
            ser = CollegeSer(obj)
            return Response({"data": ser.data}, status=200)
        objs = College.objects.all()
        ser_objs = CollegeSer(objs, many=True)
        return Response({"all_data": ser_objs.data},status=200)
    
    def delete(self, pk):
        if pk is not None:
            try:
                obj = College.objects.get(id=pk)
            except:
                error_msg = {"message": "Record Not Found"}
                return Response(error_msg)
            obj.delete()
            return Response({"message": "Deleted Successfully"})
    
    def post(self, request, format=None):
        data = CollegeSer(data=request.data)
        if data.is_valid():
            data.save()
            return Response({"Message": "saved"})
        else:
            return Response({"Message": "Invalid data"})
        

class CourseAPIView(APIView):

    def get(self, request, pk=None, format=None):
        if pk is not None:
            try:
                obj = Course.objects.get(id=pk)
            except:
                error_msg = {"message": "Record Not Found"}
                return Response(error_msg)
            ser = CourseSer(obj)
            return Response({"data": ser.data}, status=200)
        objs = Course.objects.all()
        ser_objs = CourseSer(objs, many=True)
        return Response({"all_data": ser_objs.data},status=200)

def sample(request):
    from datetime import time, date
    import pdb;pdb.set_trace()
    company = Company.objects.all()
    employee = Employee.objects.filter(dor__isnull=True)
    ## give 10 per hike who having age above 27
    hike = 10/100
    e1 = Employee.objects.filter(age__gte=27).annotate(total_sal=F('salary') +( F('salary') * hike)).values('name', 'total_sal')
    e2 = Employee.objects.annotate(joined_year=ExtractYear('doj'), relieved_year=ExtractYear('dor')). \
                                  filter(joined_year__gte=2021, relieved_year__lte=2022). \
                                  values('name', 'joined_year', 'relieved_year')
    
    print("companies query:-----", company.query)
    print()
    print("employees query:-----", employee.query)
    print("companies:-----", company)
    print("employees:-----", employee)
    return HttpResponse("Fetched....")

def validate_file(file):
    name = file.name.split('.')[-1]
    if name != 'xlsx':
        return Response({"Error": "Invalid file format. Allowed only excel format"})


class uploadFile(APIView):
    # parser_classes = [FileUploadParser]
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def post(self, request, name=None):
        query_param = request.query_params.get('name')
        file = request.data.get('file', None)
        if file:
            import pandas as pd
            validate_file(file)
            df = pd.read_excel(file)
            return Response({"message":"file is received"}, status=200)
        else:
            return Response({"message":"file not is received"}, status=400)
