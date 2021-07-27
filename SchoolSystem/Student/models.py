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
    )

    date_of_birth = models.DateField(
        max_length=27
    )

    roll_number=models.CharField(
        max_length=10
    )

    emailAdress=models.EmailField(
        max_length=50
    )
    nationality=models.CharField(
        max_length=150
    )
    student_id=models.PositiveSmallIntegerField(
       
    )
    id_number=models.CharField(
        max_length=10
        
    )
    GENDER_CHOICES=(
        (u'M', u'Male'),
        (u'F', u'Female'),
        (u'O', u'Other'),
    )
    gender=models.CharField(
        max_length=1, choices=GENDER_CHOICES
        )

    phoneNumber=models.CharField(
        max_length=15
    )
    # image=models.ImageField(
    #     upload_to='uploads',blank=True
    # )
    medical_report=models.FileField(

    )
    date_of_enrollment=models.DateField(
        max_length=10
    )
    course_name=models.CharField(
        max_length=15
    )

    LANGUAGE_CHOICES=(
        (u'E', u'English'),
         (u'S', u'Swahili'),
    )
    language=models.CharField(
        max_length=2, choices=LANGUAGE_CHOICES
        )
    serial_number=models.CharField(
        max_length=20
    )

   






