
#from django import forms
# class UserForm(forms.Form):
#     name = forms.CharField(label="Person Name")
#     contactno = forms.IntegerField(label="Person Contact No")
#     password  = forms.CharField(label="Person Password",widget=forms.PasswordInput)


from django import forms
from django.forms import widgets
from app33.models import UserModel

class UserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = "__all__"
        labels = {
            "name":"Person Name",
            "contact": "Person Contact Details",
            "password": "Person Strong Password"
        }
        help_text = {"name":"enter your full name"}
        error_message = {"name":{'required':"name is required"},
                        "password":{"required":"pass is required"}}
        widgets = {"name": forms.PasswordInput(attrs={'class':'myclass'}),
                    'password':forms.PasswordInput(attrs={'class':"mypassclass"})}

