from django.urls import path
from .views import landing


urlpatterns=[
    path("",landing, name ="create_page"),
  
]