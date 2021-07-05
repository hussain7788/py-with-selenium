from django.db import models

class LanguagesModel(models.Model):
    no = models.AutoField(primary_key=True)
    language_name = models.CharField(max_length=30)

    def __str__(self):
        return self.language_name


class EmployeeModel(models.Model):
    idno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    salary = models.FloatField()
    designation = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='employee_photo/')
    langs = models.ManyToManyField(LanguagesModel,default=None)


