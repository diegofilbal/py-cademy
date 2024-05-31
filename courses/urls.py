from django.urls import path
from .views import CourseApiView, RateApiView

urlpatterns = [
    path("courses/", CourseApiView.as_view(), name="courses"),
    path("rates/", RateApiView.as_view(), name="rates"),
]
