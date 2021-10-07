from django.shortcuts import render,redirect
from .forms import CourseRegistritionForm
from django .shortcuts import render
from .models import Course



def register_course(request):
    if request.method=="POST":
        form = CourseRegistritionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)

    else:
        form= CourseRegistritionForm()
    return render(request,"register_course.html",{"form":form,})


def course_list(request):
    courses= Course.objects.all()
    return render(request, "course_list.html", {"courses":courses})


def course_profile(request,id):
    course=Course.objects.get(id=id)
    return render(request,"course_profile.html", {"course":course})

def edit_course(request, id):
    course=Course.objects.get(id=id)

    if request.method == "POST":
        form = CourseRegistritionForm(request.post,instance=course)
        if form.is_valid():
            form.save()
        return redirect("trainer_profile", id=course.id, )

    else:
        form=CourseRegistritionForm(instance=course)

        return render(request,"edit_course.html", {"form": form})
