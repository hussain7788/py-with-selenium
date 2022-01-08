from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PersonSerializer
from .models import PersonModel
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class PersonModelViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = PersonModel.objects.all()


class PersonApiView(APIView):
    def get(self, request, pk=None, format=None):
        print("id is::", pk)
        if pk is not None:
            try:
                obj = PersonModel.objects.get(id=pk)
            except:
                return Response({"Warning": "No Record Found"})
            ser = PersonSerializer(obj)
            return Response(ser.data)
        obj_all = PersonModel.objects.all()
        ser = PersonSerializer(obj_all, many=True)
        return Response(ser.data)

    def post(self, request, format=None):
        ser = PersonSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            print("valid")
            return Response({"Success": "person added.."}, status=status.HTTP_201_CREATED)
        else:
            print("not valid")
            return Response({"Failed": "invalid data"}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None, format=None):
        obj = PersonModel.objects.get(id=pk)
        ser = PersonSerializer(obj, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"updated": "updated successfully"}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({"Failed": "updated Failed"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        obj = PersonModel.objects.get(id=pk)
        obj.delete()
        return Response({obj.name: "deleted"})
