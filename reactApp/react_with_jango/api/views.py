from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import Room,Article
from .serializers import RoomSerializer, CreateRoomSerializer, ArticleSerializer
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import viewsets


# Create your views here.
#### ModelViewset
class ArticleViewset(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


###  APIViewsets
class ArticleApiView(APIView):
    
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        print("request data is", request.data)
        serializer = ArticleSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
        #     Article.objects.create(id=serializer.data.get("id"),
        #                             title = serializer.data.get("title"),
        #                             author = serializer.data.get("author"),
        #                             email = serializer.data.get("email"),
        #                             )
        # articles = Article.objects.filter(id=request.data["id"]).values()
        # return Response({"Message" : "article added", "article":article})








    
