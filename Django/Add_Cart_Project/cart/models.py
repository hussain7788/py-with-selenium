from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=100, null=False, default='')
    price = models.FloatField(default=10.0)


    def __str__(self) -> str:
        return self.name
    


class CartItems(models.Model):
    p_name = models.CharField(max_length=100, null=False, default='')
    p_price = models.FloatField(default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_items', default='') 


    def __str__(self) -> str:
        return self.user.username


    def total_price(self, user_obj):
        obj = CartItems.objects.filter(user=user_obj).values('p_price')
        result = [item['p_price'] for item in obj]
        return sum(result)  
