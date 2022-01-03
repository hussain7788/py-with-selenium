from django.shortcuts import render,redirect
from django.contrib import messages
from app.models import ProductModel
from django.core.paginator import Paginator


def showIndex(request):
    #result = ProductModel.objects.all()
    #return render(request,"index.html",{"data":result})

    result = ProductModel.objects.all()
    pa = Paginator(result,4)
    page_no = request.GET.get("page_no",1)
    page = pa.page(page_no)
    print(page.object_list)
    return render(request, "index.html", {"page": page})



def admin_login(request):
    return render(request,"admin_login.html")


def admin_login_check(request):
    un = request.POST.get("t1")
    pa = request.POST.get("t2")

    if un == "naveen" and pa == "naveen":
        request.session['admin_name'] = un
        return redirect('admin_home')
    else:
        messages.error(request,"Invalid User")
        return redirect('admin_login')


def admin_home(request):
    return render(request,"admin_home.html")


def admin_view_users(request):
    print("session id for admin", request.session['admin_name'])
    return render(request,"admin_view_users.html")


def admin_view_products(request):
    #result = ProductModel.objects.all()
    #return render(request,"admin_view_products.html",{"data":result})

    result = ProductModel.objects.all()
    pa = Paginator(result,2)
    page_number = request.GET.get("page_no",1)
    page = pa.page(page_number)
    return render(request,"admin_view_products.html",{"page":page})



def save_product(request):
    na = request.POST.get("p1")
    pr = request.POST.get("p2")
    qty = request.POST.get("p3")
    img = request.FILES["p4"]
    status = "active"
    ProductModel(name=na,price=pr,quantity=qty,photo=img,status=status).save()
    return redirect('admin_view_products')


def add_to_cart(request):
    k = request.GET.get("c1")
    v = request.GET.get("c2")
    response = redirect('in_cart')
    response.set_cookie(k,v)
    return response


def in_cart(request):
    return render(request,"in_cart.html",{"data":request.COOKIES})