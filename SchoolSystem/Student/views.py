from django .shortcuts import redirect, render
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
    return render(request,"register_student.html",{"form":form,})


def student_list(request):
    students= Student.objects.all()
    return render(request, "student_list.html", {"students":students})

def student_profile(request,id):
    student=Student.objects.get(id=id)
    return render(request,"student_profile.html", {"student":student})

def edit_student(request, id):
    student=Student.objects.get(id=id)

    if request.method == "POST":
        form = StudentRegistritionForm(request.post,instance=student)
        if form.is_valid():
            form.save()
        return redirect("student_profile", id=student.id, )

    else:
        form=StudentRegistritionForm(instance=student)

        return render(request,"edit_student.html", {"form": form})




