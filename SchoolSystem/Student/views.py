from django .shortcuts import render
from .forms import StudentRegistritionForm
from django .shortcuts import render

def register_student(request):
    form = StudentRegistritionForm()
    return render(request, "register_student.html",{
        "form":form
    })



