from django.db import models

# Create your models here.

class Course(models.Model):
    profile=models.ImageField(
        upload_to='images',blank=True
    )
    course_name=models.CharField(
        max_length=50, null=True
    )

    course_code=models.CharField(
        max_length=50
    )

    syllabus=models.CharField(
        max_length=200
    )

    course_trainer=models.CharField(
        max_length=50
    )

    course_schedule=models.FileField(

    )

    course_duration=models.CharField(
        max_length=30

    )
