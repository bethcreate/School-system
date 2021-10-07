from django.urls import include,path
from rest_framework import routers
from .views import StudentViewSet, TrainerViewSet, CourseViewSet,EventViewSet


router=routers.DefaultRouter()
router.register(r"students", StudentViewSet)
router.register(r"trainers", TrainerViewSet)
router.register(r"courses", CourseViewSet)
router.register(r"calendar", EventViewSet)



urlpatterns=[
    path("", include(router.urls)),

]