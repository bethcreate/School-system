from django .shortcuts import render
from .forms import StudentRegistritionForm
from django .shortcuts import render
from .models import Student



def register_student(request):
    if request.method=="POST":
        form = StudentRegistritionForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)

    else:
        form=StudentRegistritionForm()
    return render(request,"register_student.html",{"form":form, "Name":"Beth Kamau"})


def student_list(request):
    students= Student.objects.all()
    return render(request, "student_list.html", {"students":students})




