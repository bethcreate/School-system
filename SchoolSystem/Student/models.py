from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(
        max_length=12
    )

    last_name = models.CharField(
        max_length=15
    )

    age = models.PositiveSmallIntegerField(
        max_length=3
    )

    date_of_birth = models.DateField(
        max_length=27
    )