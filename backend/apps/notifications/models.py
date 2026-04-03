from django.conf import settings
from django.db import models
from apps.common.models import TimeStampedModel


class Notification(TimeStampedModel):
    CHANNEL_CHOICES = [('in_app', 'In-app'), ('email', 'Email'), ('push', 'Push')]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
    channel = models.CharField(max_length=32, choices=CHANNEL_CHOICES)
    kind = models.CharField(max_length=64)
    title = models.CharField(max_length=180)
    body = models.TextField(blank=True)
    is_read = models.BooleanField(default=False)
    payload = models.JSONField(default=dict, blank=True)
