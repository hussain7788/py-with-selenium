
from django import forms

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






