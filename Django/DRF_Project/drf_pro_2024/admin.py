from django.contrib import admin
from .models import College, Student, Company, Employee

# Register your models here.
admin.site.register(College)
admin.site.register(Student)
# admin.site.register(Company)
# admin.site.register(Employee)

@admin.register(Company)
class Companylist(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Employee)
class EmployeeList(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'salary', 'doj', 'dor', 'city', 'company']