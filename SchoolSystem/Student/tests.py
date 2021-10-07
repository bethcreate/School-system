from django.test import TestCase
from .models import Student
import datetime
class StudentModelTestCase(TestCase):
    def setUp(self):
        self.student=Student(
            first_name="Beth",
            last_name="Kamau", 
            age=20, 
            language= "Kikuyu",
            course_name="javascript",
            email_address= "kamaub@gmail.com"
            )

    def test_full_name_contains_first_name(self):
        self.assertIn(self.student.first_name,self.student.full_name())

    def test_full_name_contains_last_name(self):
        self.assertIn(self.student.last_name,self.student.full_name())

    def test_student_year_of_birth(self):
        current_year=datetime.datetime.now().year
        year= current_year-self.student.age        
        self.assertequal(year, self.student.year_of_birth())