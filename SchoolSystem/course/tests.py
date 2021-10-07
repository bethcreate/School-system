from django.test import TestCase

# Create your tests here.
class CoursesModelTestCase(TestCase):
    def setUp(self):
        self.courses=Courses(Course_name="Stella",
        Course_duration="78 weeks",
        Course_code="21313C",
       Course_id="12c",
        )
        def test_courses_Course_duration(self):
            self.assertIn(self.courses.Course_duration())
        def test_courses_Course_code(self):
            self.assertIn(self.courses.Course_code())
        def test_courses_Course_id(self):
            self.assertIn(self.courses.Course_id())
        def test_courses_Course_name(self):
            self.assertIn(self.courses.Course_name())