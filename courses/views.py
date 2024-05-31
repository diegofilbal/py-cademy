from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Course, Rate
from .serializers import CourseSerializer, RateSerializer


class CoursesAPIView(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class RatesAPIView(ListCreateAPIView):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer


class RateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
