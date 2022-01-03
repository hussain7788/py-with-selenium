from django.db import models

class ProductModel(models.Model):
    no = models.AutoField(primary_key = True)
    name = models.CharField(unique=True,max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()
    photo = models.ImageField(upload_to="product_images/")
    pdate = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=100)


class UserModel(models.Model):
    no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    contact = models.IntegerField(unique=True)
    email = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    jdate = models.DateField(auto_now_add=True)
