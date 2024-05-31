from django.contrib import admin
from .models import Course, Rate


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["title", "url", "created_at", "updated_at", "active"]


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display = [
        "course",
        "name",
        "email",
        "rate",
        "created_at",
        "updated_at",
        "active",
    ]
