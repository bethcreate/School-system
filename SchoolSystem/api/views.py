from django.shortcuts import render
from.serializers import StudentSerializer
from rest_framework import viewsets
from Student.models import Student

from trainer.models import Trainer
from.serializers import TrainerSerializer

from course.models import Course
from.serializers import CourseSerializer

from cal.models import Event
from.serializers import EventSerializer


# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer


class TrainerViewSet(viewsets.ModelViewSet):
    queryset=Trainer.objects.all()
    serializer_class=TrainerSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset=Course.objects.all()
    serializer_class=EventSerializer