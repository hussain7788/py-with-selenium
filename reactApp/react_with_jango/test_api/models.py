from django.db import models

# Create your models here.


class PersonModel(models.Model):
    gender_choices = (
        ("MALE", "male"),
        ("FEMALE", "female"),
        ("OTHERS", "others")

    )
    name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=10, choices=gender_choices)

class Student(models.Model):
    sname = models.CharField(max_length=100)
    sage = models.IntegerField(default=0)
    

