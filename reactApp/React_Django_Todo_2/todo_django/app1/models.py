from django.db import models

# Create your models here.


class TodoModel(models.Model):
    name = models.CharField(max_length=50, null=False)
    created = models.DateField(auto_now_add=True)
    completed = models.BooleanField(default=False)


    def __str__(self) -> str:
        return self.name