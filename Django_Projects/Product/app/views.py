from django.shortcuts import render,redirect
from django.contrib import messages
from app.models import ProductModel

def showIndex(request):
    result = ProductModel.objects.all()
    return render(request,"index.html",{"data":result})


def admin_login(request):
    return render(request,"admin_login.html")


def admin_login_check(request):
    un = request.POST.get("t1")
    pa = request.POST.get("t2")


    if un == "naveen" and pa == "naveen":
        return redirect('admin_home')
    else:
        messages.error(request,"Invalid User")
        return redirect('admin_login')


def admin_home(request):
    return render(request,"admin_home.html")


def admin_view_users(request):
    return render(request,"admin_view_users.html")


def admin_view_products(request):
    result = ProductModel.objects.all()
    return render(request,"admin_view_products.html",{"data":result})


def save_product(request):
    na = request.POST.get("p1")
    pr = request.POST.get("p2")
    qty = request.POST.get("p3")
    img = request.FILES["p4"]
    status = "active"
    ProductModel(name=na,price=pr,quantity=qty,photo=img,status=status).save()
    return redirect('admin_view_products')