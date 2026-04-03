from django.conf import settings
from django.db import models
from apps.common.models import TimeStampedModel
from apps.events.models import Event


class TicketTier(TimeStampedModel):
    TIER_CHOICES = [('normal', 'Normal'), ('promo', 'Promocional'), ('early_bird', 'Early Bird')]
    MIN_PLAN_CHOICES = [('none', 'Sem restrição'), ('silver', 'Silver'), ('gold', 'Gold')]

    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='ticket_tiers')
    name = models.CharField(max_length=140)
    tier_type = models.CharField(max_length=32, choices=TIER_CHOICES, default='normal')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=8)
    quantity_total = models.PositiveIntegerField(null=True, blank=True)
    quantity_sold = models.PositiveIntegerField(default=0)
    sale_starts_at = models.DateTimeField(null=True, blank=True)
    sale_ends_at = models.DateTimeField(null=True, blank=True)
    min_plan = models.CharField(max_length=32, choices=MIN_PLAN_CHOICES, default='none')
    is_active = models.BooleanField(default=True)


class Order(TimeStampedModel):
    ORDER_TYPE_CHOICES = [('ticket', 'Bilhete'), ('subscription', 'Subscrição')]
    STATUS_CHOICES = [('draft', 'Rascunho'), ('pending_payment', 'Pagamento pendente'), ('paid', 'Pago'), ('cancelled', 'Cancelado'), ('refunded', 'Reembolsado')]

    number = models.CharField(max_length=32, unique=True)
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    event = models.ForeignKey(Event, null=True, blank=True, on_delete=models.SET_NULL)
    order_type = models.CharField(max_length=32, choices=ORDER_TYPE_CHOICES)
    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default='draft')
    subtotal = models.DecimalField(max_digits=12, decimal_places=2)
    discount_total = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    fee_total = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=8)
    coupon_code = models.CharField(max_length=64, blank=True)


class OrderItem(TimeStampedModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    ticket_tier = models.ForeignKey(TicketTier, null=True, blank=True, on_delete=models.SET_NULL)
    description = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=12, decimal_places=2)
    discount_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
