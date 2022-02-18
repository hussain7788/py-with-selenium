from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    class Meta:
        abstract = True
        verbose_name = "Person"

    def __str__(self) -> str:
        return self.name


class Student(Person):
    course = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Student"
