from django.shortcuts import render
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

