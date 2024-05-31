from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course, Rate
from .serializers import CourseSerializer, RateSerializer


class CourseApiView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)


class RateApiView(APIView):
    def get(self, request):
        rates = Rate.objects.all()
        serializer = RateSerializer(rates, many=True)
        return Response(serializer.data)
