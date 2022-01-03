from django.db import models
from hod.models import CommonModel

class StudentModel(CommonModel):
    marks = models.IntegerField()