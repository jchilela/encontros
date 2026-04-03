from django.conf import settings
from django.db import models
from apps.common.models import TimeStampedModel
from apps.taxonomy.models import Category, City
from apps.communities.models import Group


class Event(TimeStampedModel):
    FORMAT_CHOICES = [('presencial', 'Presencial'), ('online', 'Online'), ('hibrido', 'Híbrido')]
    VISIBILITY_CHOICES = [('public', 'Público'), ('private', 'Privado'), ('unlisted', 'Não listado')]
    PLAN_CHOICES = [('none', 'Sem restrição'), ('silver', 'Silver'), ('gold', 'Gold')]
    STATUS_CHOICES = [('draft', 'Rascunho'), ('published', 'Publicado'), ('cancelled', 'Cancelado'), ('finished', 'Finalizado')]

    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='events')
    group = models.ForeignKey(Group, null=True, blank=True, on_delete=models.SET_NULL, related_name='events')
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    city = models.ForeignKey(City, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=220)
    slug = models.SlugField(max_length=260, unique=True)
    summary = models.CharField(max_length=280, blank=True)
    description = models.TextField()
    image_url = models.URLField(blank=True)
    event_format = models.CharField(max_length=32, choices=FORMAT_CHOICES)
    visibility = models.CharField(max_length=32, choices=VISIBILITY_CHOICES, default='public')
    required_plan = models.CharField(max_length=32, choices=PLAN_CHOICES, default='none')
    starts_at = models.DateTimeField()
    ends_at = models.DateTimeField()
    timezone = models.CharField(max_length=64, default='Europe/Lisbon')
    venue_name = models.CharField(max_length=180, blank=True)
    address_line = models.CharField(max_length=255, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    online_url = models.URLField(blank=True)
    capacity = models.PositiveIntegerField(null=True, blank=True)
    waitlist_enabled = models.BooleanField(default=True)
    base_currency = models.CharField(max_length=8, default='EUR')
    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default='draft')


class EventFAQ(TimeStampedModel):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='faqs')
    question = models.CharField(max_length=180)
    answer = models.TextField()


class RSVP(TimeStampedModel):
    STATUS_CHOICES = [('confirmed', 'Confirmado'), ('cancelled', 'Cancelado'), ('checked_in', 'Check-in')]
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='rsvps')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='rsvps')
    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default='confirmed')
    checked_in_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('event', 'user')


class WaitlistEntry(TimeStampedModel):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='waitlist_entries')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='waitlists')
    priority_score = models.IntegerField(default=0)
    promoted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('event', 'user')
