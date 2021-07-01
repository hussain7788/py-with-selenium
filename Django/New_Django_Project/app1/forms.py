from django import forms
from django.contrib.auth.models import User
from django import forms
from django.forms import widgets
from  .models import *
from app1.mixins import PersonMixins

class UserLoginForm(forms.Form):
    username = forms.CharField(label="enter user name")
    password = forms.CharField(label="enter password", widget=forms.PasswordInput)


class PersonForm(PersonMixins, forms.ModelForm):
    gender_choices = (
            ('MALE', 'male'),
            ('FEMALE', 'female'),
            ('OTHERS', 'others')
        )

## this validators form the mixins 
    p_name = forms.CharField(label="person name", validators=[PersonMixins.check_name])
    p_gender = forms.ChoiceField(label="person gender", choices=gender_choices, widget=forms.RadioSelect, validators=[PersonMixins.check_gender])
    p_age = forms.IntegerField(label="person age", validators=[PersonMixins.check_age])
    
    class Meta:
        model = Person
        fields = "__all__"

### fields 
    # class Meta:
    #     model = Person
    #     fields = "__all__"
        # labels = {"p_name":"name", "p_age":"age"}
        # help_text = {"p_name":"this is name helptext", "p_age":"this is age help"}
        # error_messages = {"p_name":{"required": "this p_name is required"},
        #                     "p_age":{"required": "this p_age is required"}}
        # widgets = {"p_gender":forms.ChoiceField(choices=gender_choices)}



    # def clean_p_age(self):
    #     age = self.cleaned_data["p_age"]
    #     print("type", type(age), age)
    #     if age >= 18:
    #         return age
    #     else:
    #         raise forms.ValidationError("Age Must Be 18+")
    
    # def clean_p_gender(self):
    #     gen = self.cleaned_data['p_gender']
    #     if gen == "MALE" or gen == "FEMALE":
    #         return gen
    #     else:
    #         raise forms.ValidationError("gender must be male or female")
    
#####################################
## to validate all fields at a time use this function
    # def clean(self):
    #     cleaned_data = super().clean()
    #     na = self.cleaned_data['p_name']
    #     age = self.cleaned_data['p_age']
    #     num = self.cleaned_data['p_num']
    #     gen = self.cleaned_data['p_gender']
    #     if len(na) < 5:
    #         raise forms.ValidationError("person name should be minimum five characters")
    #     if age < 18:
    #         raise forms.ValidationError("age Must be 18 or above 18")
    #     if len(str(num)) < 10:
    #         raise forms.ValidationError("number should be 10 characters")
    #     if gen == "OTHERS":
    #         raise forms.ValidationError("gender must be male or female")
        



####### this is for normal form clear

class RegistrationForm(forms.Form):

    gen = (
        ('MALE','male'),
        ('FEMALE','female'),
        ('OTHERS','others'),
    )

    des  = (
        ('manager','MANAGER'),
        ('developer','DEVELOPER'),
        ('tester','TESTER')
    )

    idno = forms.IntegerField(label="Employee IDNO",min_value=101)
    name = forms.CharField(label="Employee NAME",min_length=2)
    cno = forms.IntegerField(label="Employee Contact No")
    gender = forms.ChoiceField(label="Employee Gender",choices=gen,widget=forms.RadioSelect)
    email = forms.EmailField(label="Employee Email-Id")
    designation = forms.ChoiceField(label="Employee DESIGNATION",choices=des)
    doj = forms.DateField(label="Date of Join")
    #dob = forms.DateField(label="Date of Birth",widget=forms.SelectDateWidget)
    dob = forms.CharField(label="Date of Birth",widget=forms.DateInput(attrs={'type':'date'}))
    image = forms.ImageField(label="Employee PHOTO")
    username = forms.CharField(label="Username")
    passowrd = forms.CharField(label="Password",widget=forms.PasswordInput)
    address = forms.CharField(label="Address",widget=forms.TextInput)


    one = forms.CharField(label="Python",widget=forms.CheckboxInput)
    two = forms.CharField(label="Django",widget=forms.CheckboxInput)
    three = forms.CharField(label="Rest Api",widget=forms.CheckboxInput)


    

        