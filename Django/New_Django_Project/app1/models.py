from django.db import models

# Create your models here.


class Products(models.Model):
    p_name = models.CharField(max_length=100)
    p_price = models.IntegerField()
    p_photo = models.ImageField(upload_to="product_images/")


class Employee(models.Model):
    emp_name = models.CharField(max_length=40)
    emp_salary = models.FloatField()
    emp_degn = models.CharField(max_length=30)
    emp_photo = models.ImageField(upload_to="emp_images/")


class Person(models.Model):
    p_name = models.CharField(max_length=50)
    p_age = models.IntegerField()
    p_num = models.IntegerField(unique=True)
    p_gender = models.CharField(max_length=10, null=True)


class Company(models.Model):
    c_name = models.CharField(max_length=50)

    def __str__(self):
        return self.c_name


class Language(models.Model):
    l_name = models.CharField(max_length=30)

    def __str__(self):
        return self.l_name


class Programmer(models.Model):
    p_name = models.CharField(max_length=30)
    age = models.IntegerField(null=True)
    p_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    p_language = models.ManyToManyField(Language)

    def __str__(self):
        return self.p_name


# Model inheritance
###################################################################################
# Abstract Class

# this class is not updated in database because its abstract = true.. so this props we can use in another model class
class CommonClass(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

# we r inherited commonclass ..so all props will come here


class Teacher(CommonClass):
    salary = models.FloatField()


###################################################
# Multi table inheritance

# this class can be stored in db .. when we add cname and city in student class .we will get that fields in exam center
class ExamCenter(models.Model):
    cname = models.CharField(max_length=20)
    city = models.CharField(max_length=30)


# this class can get all props of examcenter
class Student(ExamCenter):
    name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)


#########################################################################
# many to many relationship queries
class Movie(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name


class Char(models.Model):
    name = models.CharField(max_length=30)
    movie = models.ManyToManyField(Movie)

    def __str__(self) -> str:
        return self.name
