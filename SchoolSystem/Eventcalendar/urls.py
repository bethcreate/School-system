from django.urls import path

from .views import register_event
from .views import register_event, event_list

app_name="Eventcalendar"
urlpatterns=[
    path("beth/",register_event, name ="register_event"),
      path("list/", event_list, name="event_list"),
]