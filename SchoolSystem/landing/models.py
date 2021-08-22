from django.db import models

# Create your models here.
class Landing(models.Model):
    my_page=models.CharField(
        max_length=200
    )