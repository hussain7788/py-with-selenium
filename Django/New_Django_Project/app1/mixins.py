from app1.models import *
import re
from django import forms

class PersonMixins:
    gender_choices = (
            ('MALE', 'male'),
            ('FEMALE', 'female'),
            ('OTHERS', 'others')

        )
    gender = forms.ChoiceField(label="person gender", choices=gender_choices, widget=forms.RadioSelect)
    name = forms.CharField(label="person name")
    age = forms.IntegerField(label="person age")

    def check_name(p_name):
        res = re.findall(r"^[A-Z a-z 0-9]*$", p_name)
        # res = p_name.startswith("m")
        if res:
            return p_name
        else:
            raise forms.ValidationError("Invalid Name")
    
    def check_age(p_age):
        if p_age >= 18:
            return p_age
        else:
            raise forms.ValidationError("Age Must Be 18+ or 18")
    
    def check_gender(p_gender):
        if p_gender == "MALE" or p_gender == "FEMALE":
            return p_gender
        else:
            raise forms.ValidationError("gender should be male or female")



