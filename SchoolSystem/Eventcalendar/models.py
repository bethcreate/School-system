from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Event(models.Model):
    event_name=models.CharField(
        max_length=100, null=True

    )

    event_date=models.DateField(
        null=True
    )

    event_time=models.TimeField(
        null=True

    )

    event_planner=models.CharField(
        max_length= 100, null= True
    )

    event_participants=models.CharField(
        max_length=200, null=True
    )

    event_duration=models.TimeField(
        null=True
    )

    event_approved_by=models.CharField(
        max_length=50, null=True
    )

    event_id=models.CharField(
        max_length=50, null=True
    )

    