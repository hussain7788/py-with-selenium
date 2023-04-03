from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.viewsets import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

#######################################3
## This Class is used to generate Access Token with Username Attribute
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token= super().get_token(user)
        token['username'] = user.username
        return token
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
############################################################

class EmpViewSet(viewsets.ModelViewSet):
 queryset = Employee.objects.all()
 serializer_class = EmployeeSerializer
 authentication_classes = [JWTAuthentication]
 permission_classes = [permissions.IsAuthenticated]

############################################
class EmployeeAPIView(APIView):

    authentication_classes= [JWTAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, pk=None):
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
        #################################################################
            ## Generating Jwt tokens when any user send post request to add 
            ## This is manual Jwt token creation
        #########################################################   
    def post(self, request, format=None):
        obj = EmployeeSerializer(data=request.data)
        if obj.is_valid():
            obj.save()
        ## THis code us used for generating jWt token when send post request for every user
            # user = Employee.objects.get(name= obj.data['name'])
            # refresh = RefreshToken.for_user(user)
            # return Response(
            #     {"message":"Employee Added", "refresh":str(refresh), "access":str(refresh.access_token)})
            return Response({"Message":"Employee added "})
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
        print("pk::::::", pk)
        try:
            obj = Employee.objects.get(id=pk)
        except:
            return Response({"Record Not Found"})
        else:
            obj.delete()
            return Response({"message":"Employee Deleted"})

