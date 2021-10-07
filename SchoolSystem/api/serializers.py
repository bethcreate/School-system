from rest_framework import serializers
from Student.models import Student
from trainer.models import Trainer
from course.models import Course
from cal.models import Event



class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=("first_name", "last_name", "age")


class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Trainer
        fields=("first_name", "last_name", "age")
        

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields=("course_name", "course_code")



class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Event
        fields=("title", "description", "start_time", "end_time")