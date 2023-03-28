from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserSignUpForm
from django.contrib.auth.decorators import login_required
from .decorators import unauthorised_user

# Create your views here.
@unauthorised_user
def home(request):
    return render(request, "home.html")

@unauthorised_user
def UserSignup(request):
    form = UserSignUpForm()
    context = {"form":form}

    if request.method == "POST":
        fm = UserSignUpForm(request.POST)
        if fm.is_valid():
            username = fm.cleaned_data['username']
            email = fm.cleaned_data['email']
            fm.save()
            messages.success(request, "User is Created")
            
        else:
            messages.error(request, "Form is invalid")

    return render(request, "signup.html", context)

@unauthorised_user
def UserLogin(request):
    
    if request.method == "POST":
        uname = request.POST.get('uname')
        upass = request.POST.get("upass")

        user = authenticate(request, username = uname, password= upass)

        if user is not None:
            login(request, user)
            return render(request, "user_dashboard.html", {"name":uname})
        else:
            messages.error(request, "Invalid User")
            return render(request, "login.html")
    
    return render(request, "login.html")

@login_required(login_url="login")
def UserLogout(request):
    logout(request)
    return redirect("login")

@login_required(login_url="login")
def UserProfile(request):
    print(request)
    user = User.objects.get(username=request.user)
    context= {"name":user.username, "email":user.email}

    return render(request, "user_profile.html", context)
