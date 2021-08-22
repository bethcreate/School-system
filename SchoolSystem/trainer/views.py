from django.shortcuts import render

from .forms import TrainerRegistritionForm
from django .shortcuts import render
from .models import Trainer

# Create your views here.

def register_trainer(request):
    if request.method=="POST":
        form = TrainerRegistritionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)

    else:
        form=TrainerRegistritionForm()
    return render(request,"register_trainer.html",{"form":form, "Name":"Joyce Kamau"})

def trainer_list(request):
    trainers= Trainer.objects.all()
    return render(request, "trainer_list.html", {"trainers": trainers})