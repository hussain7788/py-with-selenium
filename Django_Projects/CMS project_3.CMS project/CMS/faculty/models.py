from django.db import models
from hod.models import CommonModel

class FacultyModel(CommonModel):
    salary = models.FloatField()
    subject = models.CharField(max_length=100)

