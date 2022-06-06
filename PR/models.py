# Django
from django.contrib.auth.models import User
from django.db import models
from location_field.models.plain import PlainLocationField


class Impression(models.Model):
    title = models.CharField("Impression title", max_length=50)
    content = models.TextField("Твои впечатления")

    date_created = models.DateTimeField("Date of creation", auto_now=True)
    date_changed = models.DateTimeField("Date of change", auto_now=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Owner")

    address = models.CharField(max_length=255)
    location = PlainLocationField(
        based_fields=["address"], zoom=7, verbose_name="Координаты"
    )

    class Meta:
        verbose_name = "Impression"
        verbose_name_plural = "Impressions"

    def __str__(self):
        return f"{self.title}"
