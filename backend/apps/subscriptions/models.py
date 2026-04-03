from django.conf import settings
from django.db import models
from apps.common.models import TimeStampedModel


class MembershipPlan(TimeStampedModel):
    code = models.CharField(max_length=32, unique=True)
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    tier_rank = models.PositiveIntegerField(default=0)
    is_free = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    features = models.JSONField(default=list, blank=True)
    limits = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return self.name


class PlanPrice(TimeStampedModel):
    CYCLE_CHOICES = [('quarterly', 'Trimestral'), ('semiannual', 'Semestral'), ('annual', 'Anual')]
    plan = models.ForeignKey(MembershipPlan, on_delete=models.CASCADE, related_name='prices')
    billing_cycle = models.CharField(max_length=32, choices=CYCLE_CHOICES)
    currency = models.CharField(max_length=8)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    trial_days = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('plan', 'billing_cycle', 'currency')


class UserSubscription(TimeStampedModel):
    STATUS_CHOICES = [('active', 'Ativa'), ('past_due', 'Em atraso'), ('cancelled', 'Cancelada'), ('expired', 'Expirada'), ('trialing', 'Teste')]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='subscriptions')
    plan = models.ForeignKey(MembershipPlan, on_delete=models.PROTECT, related_name='subscriptions')
    billing_cycle = models.CharField(max_length=32)
    currency = models.CharField(max_length=8)
    status = models.CharField(max_length=32, choices=STATUS_CHOICES)
    auto_renew = models.BooleanField(default=True)
    started_at = models.DateTimeField()
    current_period_end = models.DateTimeField()
    cancel_at_period_end = models.BooleanField(default=False)
    scheduled_plan = models.ForeignKey(MembershipPlan, null=True, blank=True, on_delete=models.SET_NULL, related_name='scheduled_subscriptions')
    external_reference = models.CharField(max_length=120, blank=True)
