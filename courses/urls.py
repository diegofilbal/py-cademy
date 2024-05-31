from django.urls import path
from .views import CoursesAPIView, CourseAPIView, RatesAPIView, RateAPIView

urlpatterns = [
    path("courses/", CoursesAPIView.as_view(), name="courses"),
    path("courses/<int:pk>/", CourseAPIView.as_view(), name="course"),
    path("rates/", RatesAPIView.as_view(), name="rates"),
    path("rates/<int:pk>/", RateAPIView.as_view(), name="rate"),
]
