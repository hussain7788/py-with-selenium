from django.db import models

class CommonModel(models.Model):
    idno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=30)
    contactno = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)
    department = models.CharField(max_length=100)

    class Meta:
        abstract = True

class HodModel(CommonModel):
    salary = models.FloatField()
    subject = models.CharField(max_length=100)
