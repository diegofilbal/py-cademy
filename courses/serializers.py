from rest_framework import serializers
from .models import Course, Rate
from django.db.models import Avg


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

    def validate_rate(self, rate):
        if rate < 0 or rate > 5:
            raise serializers.ValidationError("Rate must be between 0 and 5.")


class CourseSerializer(serializers.ModelSerializer):

    # Nested Relationship
    # rates = RateSerializer(many=True, read_only=True)

    # Hyperlinked Related Field
    rates = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name="rate-detail"
    )

    # Primary Key Related Field
    # rates = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    rate_avg = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = (
            "id",
            "title",
            "url",
            "created_at",
            "active",
            "rates",
            "rate_avg",
        )

    def get_rate_avg(self, obj):
        avg = obj.rates.aggregate(Avg("rate")).get("rate__avg")
        if avg is None:
            return 0
        return round(avg, 1)
