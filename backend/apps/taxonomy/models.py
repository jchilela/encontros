from django.db import models
from apps.common.models import TimeStampedModel


class Category(TimeStampedModel):
    name = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=140, unique=True)
    icon = models.CharField(max_length=80, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class City(TimeStampedModel):
    country_code = models.CharField(max_length=8)
    region = models.CharField(max_length=120, blank=True)
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=140, unique=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    def __str__(self):
        return self.name
