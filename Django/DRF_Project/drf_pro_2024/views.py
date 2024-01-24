from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import College,Student,Course
from .serializers import CollegeSer, StudentSer,CourseSer
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser,AllowAny,IsAuthenticated

# Create your views here.
class StudentAPIView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]

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
