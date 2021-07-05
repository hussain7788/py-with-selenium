from django import forms
from app29.models import EmployeeModel

class EmployeeForm(forms.ModelForm):
    #salary = forms.FloatField(min_value=10000)
    class Meta:
        model = EmployeeModel
        fields = "__all__"

    def clean_salary(self):
        sal = self.cleaned_data["salary"]
        if sal >= 10000:
            return sal
        else:
            raise forms.ValidationError("Salary Must be Min 10000/-")
    
    def clean_designation(self):
        desig = self.cleaned_data["designation"]
        if desig != "Select":
            #sal = self.cleaned_data["salary"]
            sal = self.cleaned_data.get("salary",0)
            if desig == "Manager" and sal >= 50000:
                return desig
            else:
                raise forms.ValidationError("Manager Salary Min of 50000/-")
        else:
            raise forms.ValidationError("Please Select Designation")
