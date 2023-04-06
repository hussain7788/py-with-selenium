from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import viewsets
from rest_framework.viewsets import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import (AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly)
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import SearchFilter, OrderingFilter

from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from .throttling import MyUserThrottle

#######################################

########## Permisssion classes ########
## AllowAny = "It will allow any user whether it is authenticated or not authenticated ."
## IsAuthenticated = "It will allow only authenticated user means only Created Users in django"
## IsAdminUser = "It will allow aonly the users who are having is_staff = True"
## IsAuthenticatedOrReadOnly = "It will allow both authenticated and unauthenticated users...but  all actions to AUthenticated User and Just Read only to UnAuthenticated Users = True"
## DjangoModel Permissions = "it will allow only Authenticated Users with  read but if we need actions then login to superuser and change model permission to users 
#                                  like this user can add employee .or delete employee etc"
## DjangoModelPermissionsOrAnonReadOnly = "This is same like DjangoModelPermission but it will also provide read to Unauthenticated users"

##############################################
######## filters in rest framework 
## there are Two types of filters 
## SearchFilter = it is used to search any data with the url .to achieve this
    # 1. filter_backends = [SearchFilter]
    # 2. search_fields = ['name', 'age']
## OrderFilter = it is used to order the filter data .To achieve this 
    # 1. filter_backends = [OrderingFilter]
    # 2. ordering_fields = ['name', 'age'] or '__all__'
##########################################################


class EmpViewSet(viewsets.ModelViewSet):
 queryset = Employee.objects.all()
 serializer_class = EmployeeSerializer
#  authentication_classes = [BasicAuthentication]
 authentication_classes = [SessionAuthentication]
 permission_classes = [IsAuthenticatedOrReadOnly]
 ## make Django Filter Backends Global level in settings and add filterset_fields here..
 filter_backends = [DjangoFilterBackend]
 filterset_fields = ["name", "age"]
#  filter_backends = [SearchFilter]
#  search_fields = ['name', 'age']

############################################
## THrottling APIs  = It is limit API requests for authorised users and unautherised users
## AnonRateThrottle = Unauthorised Users
## UserRateThrottle = AUthorised Users

# class EmpViewSet(viewsets.ModelViewSet):
#  queryset = Employee.objects.all()
#  serializer_class = EmployeeSerializer
#  authentication_classes = [SessionAuthentication]
#  permission_classes = [IsAuthenticatedOrReadOnly]
# #  throttle_classes = [AnonRateThrottle, UserRateThrottle]
#  ##### user defined Throttle
#  throttle_classes = [AnonRateThrottle, MyUserThrottle]
# #  throttle_scope = '7/hour'


# ############################################

class EmployeeAPIView(APIView):

    authentication_classes= [JWTAuthentication]
    permission_classes = [IsAdminUser]

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

