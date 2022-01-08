from django.shortcuts import render
from django.http import HttpResponse, request
from rest_framework import serializers, status
from rest_framework import generics
from .models import Room, Article
from .serializers import RoomSerializer, CreateRoomSerializer, ArticleSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets


# Create your views here.
# ModelViewset
class ArticleViewset(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


# APIViewsets
class ArticleApiView(APIView):

    def get(self, request, pk=None, format=None):
        print("pk::", pk)
        if pk is not None:
            art = Article.objects.get(id=pk)
            serializer = ArticleSerializer(art)
            return Response(serializer.data)
        articles = Article.objects.all()
        print(articles[0].email)
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ArticleSerializer(data=request.data)
        print("post serializer data::", serializer)
        if serializer.is_valid():
            serializer.save()
            print("serializer", serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print("not valid")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        art = Article.objects.get(id=pk)
        print(art)
        ser = ArticleSerializer(art, data=request.data)
        if ser.is_valid():
            print("put is valid")
            ser.save()
            return Response({"msg": "successfully updated"}, status=status.HTTP_201_CREATED)
        else:
            print("put not valid")
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        art = Article.objects.get(id=pk)
        art.delete()
        return Response({"msg": "successfully deleted"}, status=status.HTTP_200_OK)
