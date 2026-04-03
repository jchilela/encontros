from datetime import timedelta
from django.utils import timezone
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import MembershipPlan, PlanPrice, UserSubscription
from .serializers import MembershipPlanSerializer, UserSubscriptionSerializer


class PlanViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MembershipPlan.objects.filter(is_active=True).order_by('tier_rank')
    serializer_class = MembershipPlanSerializer
    permission_classes = [permissions.AllowAny]


class SubscriptionViewSet(viewsets.GenericViewSet):
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['get'])
    def current(self, request):
        subscription = UserSubscription.objects.filter(user=request.user, status__in=['active', 'trialing', 'past_due']).select_related('plan').first()
        if not subscription:
            return Response({'detail': 'Sem subscrição ativa.'}, status=404)
        return Response(UserSubscriptionSerializer(subscription).data)

    @action(detail=False, methods=['post'])
    def subscribe(self, request):
        plan = MembershipPlan.objects.get(id=request.data['plan_id'])
        price = PlanPrice.objects.get(plan=plan, billing_cycle=request.data['billing_cycle'], currency=request.data['currency'])
        subscription = UserSubscription.objects.create(
            user=request.user,
            plan=plan,
            billing_cycle=price.billing_cycle,
            currency=price.currency,
            status='active' if plan.is_free else 'past_due',
            started_at=timezone.now(),
            current_period_end=timezone.now() + timedelta(days=90 if price.billing_cycle == 'quarterly' else 180 if price.billing_cycle == 'semiannual' else 365),
            auto_renew=not plan.is_free,
        )
        return Response(UserSubscriptionSerializer(subscription).data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def cancel_renewal(self, request):
        subscription = UserSubscription.objects.filter(user=request.user, status__in=['active', 'trialing', 'past_due']).first()
        if not subscription:
            return Response({'detail': 'Sem subscrição ativa.'}, status=404)
        subscription.cancel_at_period_end = True
        subscription.save(update_fields=['cancel_at_period_end', 'updated_at'])
        return Response({'detail': 'Renovação automática cancelada.'})
