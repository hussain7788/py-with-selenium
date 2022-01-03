from django.db import models

class Country(models.Model):
    country_no = models.AutoField(primary_key=True)
    country_name = models.CharField(max_length=50,unique=True)

class State(models.Model):
    state_no = models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=50, unique=True)
    state_country = models.ForeignKey(Country,on_delete=models.CASCADE)

class City(models.Model):
    city_no = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=50, unique=True)
    city_state = models.ForeignKey(State, on_delete=models.CASCADE)


