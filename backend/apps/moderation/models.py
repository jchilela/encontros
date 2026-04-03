from django.conf import settings
from django.db import models
from apps.common.models import TimeStampedModel


class Report(TimeStampedModel):
    STATUS_CHOICES = [('pending', 'Pendente'), ('reviewing', 'Em análise'), ('resolved', 'Resolvida'), ('rejected', 'Rejeitada')]
    reporter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reports')
    target_type = models.CharField(max_length=32)
    target_id = models.CharField(max_length=64)
    reason = models.CharField(max_length=120)
    details = models.TextField(blank=True)
    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default='pending')


class AuditLog(TimeStampedModel):
    actor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    action = models.CharField(max_length=120)
    resource_type = models.CharField(max_length=64, blank=True)
    resource_id = models.CharField(max_length=64, blank=True)
    metadata = models.JSONField(default=dict, blank=True)
