from django.db import models


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Course(Base):
    title = models.CharField(max_length=255)
    url = models.URLField(unique=True)

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
        ordering = ["id"]

    def __str__(self):
        return self.title


class Rate(Base):
    course = models.ForeignKey(Course, related_name="rates", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    comment = models.TextField(blank=True, default="")
    rate = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        verbose_name = "Rate"
        verbose_name_plural = "Rates"
        unique_together = ["course", "email"]
        ordering = ["id"]

    def __str__(self):
        return f"{self.name} rated '{self.course.title}' course with {self.rate} rate."
