from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import widgets
from django.forms.fields import CharField

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {"username": "enter username",
                "password": "enter password"}
    
class UserLoginForm(forms.Form):
    username = forms.CharField(label="enter user name")
    password = forms.CharField(label="enter password", widget=forms.PasswordInput)

    

        