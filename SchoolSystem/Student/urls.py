from django.urls import path
from .views import edit_student, register_student, student_profile
from .views import register_student,student_list
from .views import student_profile
from django.urls import reverse



urlpatterns =[
    path("register",register_student, name ="register_student"),
    path("list/", student_list, name="student_list"),
    path("profile/<int:id>/", student_profile, name="student_profile"),
    path("edit/<int:id>/", edit_student, name="edit_student"),
]


def test_register_student_view(self):
    url=reverse("register_student")
    data={
        "first_name": self.student.first_name,
        "last_name":self.student.last_name,
        "age": self.student.last_name,
        "language":self.student.last_name,
        "course_name": self.student.last_name,
        "email_address":self.student.last_name      
    }


    request=self.client.post(url,data)
    self.assertEqual(request.status_code,200)