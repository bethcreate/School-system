from django.db import models

# Create your models here.
class Trainer(models.Model):
    first_name=models.CharField(
        max_length=15
    )
    last_name=models.CharField(
        max_length=15
    )

    course=models.CharField(
        max_length=50
    )

    GENDER_CHOICES=(
        (u'M', u'Male'),
        (u'F', u'Female'),
        (u'O', u'Others'),
    )
    gender=models.CharField(
        max_length=1, choices=GENDER_CHOICES
    )

    number_of_lessons_taught=models.PositiveSmallIntegerField(
        
    )

    profile=models.ImageField(
        upload_to='images',blank=True
    )

    age=models.PositiveSmallIntegerField(
        
    )

    occupation=models.CharField(
        max_length=100
    )

    phone_number=models.CharField(
        max_length=50
    )

    bio=models.CharField(
        max_length=200
    )

    cv=models.FileField(

    )

    email=models.EmailField(
        max_length=50
    )

    contract=models.CharField(
        max_length=30
    )

    date_hired=models.DateField(
        max_length=20


    )

    LANGUAGE_CHOICES=(
        (u'E', u'English'),
         (u'S', u'Swahili'),
         (U'K', u'Kikuyu'),
         (U'R', u'kinyarwanda'),
         (U'U', u'Kiganda')
         
    )
    
    language=models.CharField(
        max_length=2, choices=LANGUAGE_CHOICES
        )
    def full_name(self):
                return f"{self.first_name} {self.last_name}"

