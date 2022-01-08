from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Programmer(models.Model):
    name = models.CharField(max_length=30, null=True)
    age = models.IntegerField(null=True)
    company = models.ForeignKey(Company, null=True, on_delete=models.CASCADE)
    language = models.ManyToManyField(Language, null=True)

    def __str__(self):
        return self.name
