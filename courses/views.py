from .models import Course, Rate
from .serializers import CourseSerializer, RateSerializer
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    get_object_or_404,
)


class CoursesAPIView(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class RatesAPIView(ListCreateAPIView):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer

    def get_queryset(self):
        if self.kwargs.get("course_pk"):
            return self.queryset.filter(course_id=self.kwargs.get("course_pk"))
        return self.queryset.objects.all()


class RateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer

    def get_object(self):
        if self.kwargs.get("course_pk"):
            return get_object_or_404(
                self.get_queryset(),
                course_id=self.kwargs.get("course_pk"),
                pk=self.kwargs.get("rate_pk"),
            )
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get("pk"))
