from .models import Course, Rate
from .serializers import CourseSerializer, RateSerializer
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    get_object_or_404,
)
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from .permissions import isSuperUser


# ------------------------- API V1 -------------------------


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


# ------------------------- API V2 -------------------------


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    permission_classes = (
        isSuperUser,
        permissions.DjangoModelPermissions,
    )

    @action(methods=["get"], detail=True)
    def rates(self, request, pk=None):
        self.pagination_class.page_size = 1
        rates = self.get_object().rates.filter(course_id=pk)
        page = self.paginate_queryset(rates)

        if page is not None:
            serializer = RateSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = RateSerializer(rates.all(), many=True)
        return Response(serializer.data)


class RateViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
