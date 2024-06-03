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

    class Meta:
        model = Course
        fields = (
            "id",
            "title",
            "url",
            "created_at",
            "active",
            "rates",
        )
