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

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RateApiView(APIView):
    def get(self, request):
        rates = Rate.objects.all()
        serializer = RateSerializer(rates, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
