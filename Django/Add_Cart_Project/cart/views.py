from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from django.contrib.auth.models import User, Group
from .models import Products, CartItems
from django.http import JsonResponse
# Create your views here.

def index(request):
    return render(request, 'index.html', context={"name":"hussain"})

def cart_items(request):
    if request.user.is_authenticated:
       
        item_qty = CartItems.objects.filter(user=request.user).all().count()
        obj = CartItems.objects.filter(user=request.user)
        context = {"item_qty": item_qty}
        try:
            total_price = obj[0].total_price(user_obj=request.user)
            context.update({"total_price":total_price})
        except:
            context.update({"total_price":0})
        return context
    else:
        return {}
    


def products(request):
    result = Products.objects.all()
    context = {"products":result}
    return render(request, "products.html", context)

def add_cart(request, pk):
    print("cart item id", pk)
    pro = Products.objects.get(id=pk)
    if CartItems.objects.filter(p_name=pro.name, p_price=pro.price, user=request.user).exists():
        messages.info(request, "Item already added to cart")
        return redirect('products')
    cart = CartItems(p_name=pro.name, p_price=pro.price, user=request.user)
    cart.save()
    messages.success(request, "Added to cart")
    return redirect("products")

def fetch_cart_items(request):
    items = CartItems.objects.filter(user= request.user)
    context = {"items" : items}
    return render(request, "fetch_cart_items.html", context)


def login_user(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        upass = request.POST.get('password')
        user = authenticate(username=uname, password=upass)
        if user is not None:
            login(request, user)
            user_obj = User.objects.get(username=uname)
            request.session['user_id'] = user_obj.id
            context = {"username": uname}
            return render(request, "user_profile.html", context)
        else:
            messages.error(request, "invalid user")
            return redirect("login_user")
    else:
        return render(request, "login_user.html")
    

def logout_user(request):
    logout(request)
    return redirect('login_user')


def delete_item(request):
    if request.method == "POST":
        id = request.POST.get('id')
        obj = CartItems.objects.get(id=id)
        obj.delete()
        item = cart_items(request)
        return JsonResponse({"item_qty":item['item_qty'], "total_price":item.get('total_price', 0)})

