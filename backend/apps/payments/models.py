from django.db import models
from apps.common.models import TimeStampedModel
from apps.tickets.models import Order
from apps.subscriptions.models import UserSubscription


class PaymentTransaction(TimeStampedModel):
    PROVIDER_CHOICES = [('stripe', 'Stripe'), ('paypal', 'PayPal'), ('proprietary', 'Proprietário')]
    STATUS_CHOICES = [('created', 'Criada'), ('pending', 'Pendente'), ('paid', 'Paga'), ('failed', 'Falhou'), ('refunded', 'Reembolsada')]

    order = models.ForeignKey(Order, null=True, blank=True, on_delete=models.SET_NULL, related_name='transactions')
    subscription = models.ForeignKey(UserSubscription, null=True, blank=True, on_delete=models.SET_NULL, related_name='transactions')
    provider = models.CharField(max_length=32, choices=PROVIDER_CHOICES)
    external_reference = models.CharField(max_length=120, blank=True)
    provider_reference = models.CharField(max_length=120, blank=True)
    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default='created')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=8)
    metadata = models.JSONField(default=dict, blank=True)
