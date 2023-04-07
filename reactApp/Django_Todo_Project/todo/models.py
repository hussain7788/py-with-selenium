from django.db import models

# Create your models here.


class Todo(models.Model):
    task = models.CharField(max_length=40, null=False, blank=False)
    comepleted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.task
