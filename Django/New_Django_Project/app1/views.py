from typing import List
from django.contrib import auth
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, View, RedirectView
from django.contrib.messages.views import SuccessMessageMixin

from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

from .forms import UserLoginForm
from django.core.mail import send_mail
from New_Django_Project import settings as se
import random

email_otp = str()

def add_product(request):
    pro = Products.objects.all()
    session(request)
    response = render(request, "add_product.html", {"product":pro})
    response.set_cookie("name", "mahammed", 60)
    return response

def save_product(request):
    name = request.POST.get("p1")
    price = request.POST.get("p2")
    image = request.FILES["p3"]

    pro = Products(p_name = name, p_price=price, p_photo=image)
    pro.save()
    messages.success(request, "product added")
    return redirect("add_product")

def delete_product(request):
    id = request.GET.get("no")
    Products.objects.get(id=id).delete()
    messages.success(request, "deleted")
    return redirect("add_product")

def update_form(request, id_no):
    # p_id = request.GET.get(id_no)
    data = Products.objects.get(id=id_no)
    d1 = Products.objects.filter(id=id_no)
    print("id_no", id_no)
    ## get method will give one object only 
    print("update get", data.p_name)
    for filt in d1:
        ## filter method will give list of objects 
        print("update_form filter", filt.p_name)
    return render( request, "update_product.html", {"data":data})

def save_updated_pro(request):
    p_id = request.POST.get("p")
    na = request.POST.get("p1")
    pr = request.POST.get("p2")
    img = request.FILES["p3"]

    Products.objects.filter(id=p_id).update(p_name=na, p_price=pr, p_photo=img)
    messages.success(request, "updated successfully")
    return redirect("add_product")


################################################
## class based views starts
class add_emp(SuccessMessageMixin, CreateView):
    template_name = "add_emp.html"
    model = Employee
    fields = "__all__"
    success_url = '/add_emp/'
    success_message = "emp details saved"

class view_emp(ListView):
    template_name = "view_emp.html"
    model = Employee
    fields = ("emp_name", "emp_salary", "emp_degn")

class update_emp(UpdateView):
    template_name = "update_emp.html"
    model = Employee
    fields = "__all__"
    success_url = "/view_emp/"

class delete_emp(DeleteView):
    template_name = "delete_emp.html"
    model = Employee
    success_url = "/view_emp/"

###############################

def user_reg(request):
    if request.method == "POST":
        f_name = request.POST['f1']
        l_name = request.POST['f2']
        u_name = request.POST['f3']
        email = request.POST['f4']
        ps = request.POST['f5']
        c_ps = request.POST['f6']

        if ps == c_ps:
            if User.objects.filter(username=u_name).exists():
                messages.info(request, "username taken")
                return redirect("user_reg")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email taken")
                return redirect("user_reg")
            global email_otp
            num = random.randint(2000, 5000)
            email_otp = str(num)
            send_mail("OTP for Django Project", email_otp, se.EMAIL_HOST_USER, [email])
            messages.info(request, "Enter OTP Which We Sent To Your Email")
            data = {"fname":f_name, "lname":l_name, "uname":u_name, 'email':email, "password":ps, "c_password":c_ps}
            return render(request, "email_valid.html", {"data":data})
        else:
            messages.error(request, "password miss match")
        return redirect("user_reg")
    else:
        return render(request, "user_reg.html")

def email_valid(request):
    otp = request.POST['otp']
    f_name = request.POST['f1']
    l_name = request.POST['f2']
    u_name = request.POST['f3']
    email = request.POST['f4']
    ps = request.POST['f5']

    global email_otp
    if otp == email_otp:
        user = User(username=u_name, password=ps, email=email, first_name=f_name, last_name=l_name)
        user.save()
        messages.success(request, "user registered successfully.. login now..")
        return redirect("user_login")
    else:
        messages.error(request, "invalid OTP")
        return redirect("user_reg")

def user_login(request):
    if request.method == "POST":
        f1 = AuthenticationForm(request=request, data=request.POST)
        if f1.is_valid():
            un = f1.cleaned_data['username']
            ps = f1.cleaned_data['password']
            print("username", un)
            print("password", ps)
            
            # try:
            #     res = User.objects.filter(username=un, password=ps)
            #     print("res", res, res[0].username,res[0].password)
            # except:
            #     messages.error(request, "invalid user")
            #     return redirect("user_login")
            # else:
            #     messages.success(request, "valid user")
            #     return redirect("user_login")

            user = auth.authenticate(username=un, password=ps)
            l_users = User.objects.filter(username=un, password=ps).values()
            print("l_users", l_users)
            print("user", user)
            if user is not None:
                auth.login(request, user)
                # set session to the browser
                request.session['username'] = un
                messages.success(request, "valid user")
                return redirect("user_profile")
            else:
                messages.error(request, "invalid user")
                return redirect("user_login")
        else:
            print("not f1 is valid")
            return redirect("user_login")
    else:
        fm = AuthenticationForm()
        if "name" in request.COOKIES:
            ck1 = request.COOKIES.get("name")
            print("cookie 1", ck1)
    # get cookie from get method and if not present set default 
        ck2 = request.COOKIES.get("name", "its default cookie")
        print("cookie 2", ck2)
        return render(request, "user_login.html", {"form":fm})

def user_profile(request):
    if request.user.is_authenticated:
        # get session from the browser
        username = request.session.get("username", default="this is default session")
        # get keys from the sessions
        keys = request.session.keys()
        print("get session", keys)
        print("session for username", username)
        return render(request, "user_profile.html", {"name":request.user})
    else:
        messages.info(request, "user is not authenticated")
        return redirect("user_login")

def user_logout(request):
    #delete session from the browser
    auth.logout(request)
    # if "username" in request.session:
    #     del request.session['username']
    request.session.flush()
    return redirect("user_login")

#########################################################################
## this is sessions function 
def session(request):
    # set session 
    request.session['name'] = "hussain786"
    ## set expiry date for session
    request.session.set_expiry(500)
    # get session
    name = request.session['name']
    #set default session if required session is not available
    request.session.get("name", default="default")
    ## session age and expiry date 
    print(request.session.get_session_cookie_age())
    print(request.session.get_expiry_date())
    print(request.session.get_expiry_age())
    # print(request.session.get_expiry_at_browser_close())
    # delete session
    del request.session['name']
    ## clear all sessions
    request.session.flush()


#########################################################################

def cookie(request):
### set cookie 
    response = HttpResponse("cookie set")
    response.set_cookie("emp_name", "john", 60)
    # return response
### get cookie method
    emp_name = request.COOKIES.get['emp_name']

### delete cookie
    response = HttpResponse("deleted cookie") 
    response.delete_cookie("emp_name")

### set expiry time of cookie







        









