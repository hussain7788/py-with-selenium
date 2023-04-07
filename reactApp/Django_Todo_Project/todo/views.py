from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm


# Create your views here.

def index(request):
    fm = TodoForm()
    todo= Todo.objects.all()

    if request.method == "POST":

        if request.POST.get("search"):
            filter_task = request.POST.get("search", "nothing")
            print("filtered task:::", filter_task)
            if filter_task == "all_tasks":
                obj = Todo.objects.all()
            elif filter_task == "pending_tasks":
                obj = Todo.objects.filter(comepleted = False)
            else:
                obj = Todo.objects.filter(comepleted = True)
            data = {"data": obj, "form":fm, "filter": True} 
            return render(request, "index.html", data)
        
        fm = TodoForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('index')
    context = {"todo":todo, "form":fm, "name":"hussain"}
    return render(request, 'index.html', context,)


def update_task(request, pk):
    obj = Todo.objects.get(id=pk)
    fm = TodoForm(instance=obj)
    if request.method == "POST":
        fm = TodoForm(request.POST, instance=obj)
        if fm.is_valid():
            fm.save()
            return redirect('index')
        else:
            raise Exception("form is error")
    context = {"form":fm}
    return render(request, "update_task.html", context)

def delete_task(request, pk):
    obj = Todo.objects.get(id=pk)
    obj.delete()
    return redirect('index')