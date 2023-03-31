from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
# Model Object - Single Student Data

def student_detail(request, pk):
    try:
        stu = Student.objects.get(id = pk)
    except:
        return HttpResponse("No Data Found.")
    else:
        # print(stu)
        serializer = StudentSerializer(stu)
        # print(serializer)
        # print(serializer.data)
        json_data = JSONRenderer().render(serializer.data)
        # print(json_data)
        return HttpResponse(json_data, content_type='application/json')
        # return JsonResponse(serializer.data)

# Query Set - All Student Data
def student_list(request):
 stu = Student.objects.all()
 # print(stu)
 serializer = StudentSerializer(stu, many=True)
 print("serializer----------",serializer)
 print("serializer.data----------",serializer.data)
 json_data = JSONRenderer().render(serializer.data)
 print("json_data----------",json_data)
 return HttpResponse(json_data, content_type='application/json')
#  return JsonResponse(serializer.data, safe=False)
