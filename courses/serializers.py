from rest_framework import serializers
from .models import Course, Rate


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = (
            "id",
            "course",
            "name",
            "email",
            "comment",
            "rate",
            "created_at",
            "active",
        )
        extra_kwargs = {
            "email": {"write_only": True},
        }


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = (
            "id",
            "title",
            "url",
            "created_at",
            "active",
        )
