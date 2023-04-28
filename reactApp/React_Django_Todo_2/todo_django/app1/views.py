from django.shortcuts import render
from rest_framework.views import APIView
from .models import TodoModel
from .serializers import TodoSerializer
from rest_framework.response import Response
# Create your views here.


class Todo(APIView):

    def get(self, request, pk=None):
        if pk is not None:
            try:
                obj = TodoModel.objects.get(id=pk)
            except:
                return Response({"Data not found"}, status=404)
            else:
                ser = TodoSerializer(obj).data
                return Response(ser, status=200)

        obj = TodoModel.objects.all()
        ser = TodoSerializer(obj, many=True).data
        return Response(ser)
    
    def post(self, request):
        if request.query_params['section'] == 'create':
            t_name = request.POST.get('task_name')
            obj = TodoModel(name=t_name)
            obj.save()
            ser = TodoSerializer(obj).data
            
        
        elif request.query_params['section'] == 'mark_completed':
            task_id = request.POST.get('task_id')
            obj = TodoModel.objects.get(id=task_id)
            obj.completed = 1
            obj.save()
            ser = TodoSerializer(obj).data
            
        
        elif request.query_params['section'] == 'filter':
            filter_value = request.POST.get('filter_value')
            if filter_value == "all_tasks":
                obj = TodoModel.objects.all()
            
            elif filter_value == "pending_tasks":
                obj = TodoModel.objects.filter(completed=0)
            
            elif filter_value == "completed_tasks":
                obj = TodoModel.objects.filter(completed=1)

            ser = TodoSerializer(obj, many=True).data
            return Response(ser, status=200)

        return Response(ser, status=200)
        
    def delete(self, request, pk):
        print("delete id", pk)
        try:
            obj = TodoModel.objects.get(id=pk)
        except:
            return Response({"Data not found"}, status=404)
        else:
            obj.delete()
            all = TodoModel.objects.all()
            ser = TodoSerializer(all, many=True).data
            return Response(ser, status=200)
