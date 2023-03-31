from enroll.models import User
from enroll.api.serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.viewsets import generics
class UserViewSet(viewsets.ModelViewSet):
 queryset = User.objects.all()
 serializer_class = UserSerializer
 authentication_classes = [JWTAuthentication]
 permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class GenericListViewSets(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GenericRetViewSets(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# class GenericViewSets(generics.UpdateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
