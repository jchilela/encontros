from django.conf import settings
from django.db import models
from apps.common.models import TimeStampedModel


class Conversation(TimeStampedModel):
    KIND_CHOICES = [('direct', 'Direta'), ('group_announcement', 'Anúncio de grupo'), ('event_announcement', 'Anúncio de evento')]
    kind = models.CharField(max_length=32, choices=KIND_CHOICES)
    subject = models.CharField(max_length=180, blank=True)
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='conversations')


class Message(TimeStampedModel):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    is_system = models.BooleanField(default=False)
