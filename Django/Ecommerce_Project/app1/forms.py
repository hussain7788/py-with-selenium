from tkinter import Widget
from attr import attr, attrs
from django.contrib.auth.models import User
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm


class UserRegForm(UserCreationForm):
    password1 = forms.CharField(label="password", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'id': 'password1'}))
    password2 = forms.CharField(label="confirm password", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'id': 'password2'}))

    class Meta:
        model = User
        fields = ('username', 'email')
        # fields = "__all__"
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
        }
