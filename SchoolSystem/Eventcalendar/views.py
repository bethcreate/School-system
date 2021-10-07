from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
from django.forms.forms import Form
from .forms import EventRegistrationForm
from .models import Event

from datetime import datetime

from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe



def register_event(request):
    if request.method=="POST":
        form = EventRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form=EventRegistrationForm()
    return render(request,"register_event.html",{"form":form, "Name":"Beth"})


def event_list(request):
    events= Event.objects.all()
    return render(request, "event_list.html", {"events":events})


