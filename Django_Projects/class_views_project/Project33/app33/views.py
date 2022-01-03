from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import CreateView,FormView
from django.views.generic import ListView,RedirectView,View
from django.views.generic import UpdateView,DeleteView,DetailView
from django.contrib.messages.views import SuccessMessageMixin
from app33.models import EmployeeModel,UserModel
from app33.forms import UserForm


# class ShowMain(TemplateView):
#     template_name = "index.html"


class AddNewEmployee(SuccessMessageMixin,CreateView):
    template_name = "add_new.html"
    model = EmployeeModel
    #fields = "__all__"
    fields = ('name','photo','salary')
    success_url = '/main/'
    success_message = "Employee Details are Saved"



# Reading all rows and all cols
# class ViewAllEmployees(ListView):
#     template_name = "view_all.html"
#     model = EmployeeModel


# read all rows and 2 cols (idno and name)
class ViewAllEmployees(ListView):
    template_name = "view_all.html"
    model = EmployeeModel
## get required column fields from the object
    queryset = EmployeeModel.objects.values("idno", "name")
## get all the fields form the object
    data = EmployeeModel.objects.all().values()
    paginate_by = 3


class UpdateEmployee(UpdateView):
    template_name = "update.html"
    model = EmployeeModel
    fields = "__all__"
    success_url = '/view_all/'


class DeleteEmployee(DeleteView):
    template_name = "delete.html"
    model = EmployeeModel
    success_url = '/view_all/'


class ViewComplete(DetailView):
    template_name = "view_complete_emp.html"
    model = EmployeeModel


class OpenFacebook(RedirectView):
    url = 'http://www.facebook.com'


# class UserRegsiter(FormView):
#     template_name = "user.html"
#     form_class = UserForm

class UserRegsiter(CreateView):
    template_name = "user.html"
    model = UserModel
    form_class = UserForm
    #fields = "__all__"
    success_url = '/main/'


class LoginCheck(View):
    def post(self,request):
        un = request.POST.get("uname")
        up = request.POST.get("upass")
        try:
            res = UserModel.objects.get(contact=un,password=up)
            print("res", res.contact,res.password)
            message = {"message":"valid users"}
            return render(request, "login.html", message)
        except UserModel.DoesNotExist:
            return render(request,"login.html",{"message":"Invalid User"})
