from django.db import models

class CourseModel(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=50,unique=True)
    course_fee = models.FloatField()

class StudentModel(models.Model):
    student_id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=50)
    student_contactno = models.IntegerField(unique=True)
    student_courses = models.ManyToManyField(CourseModel)

