from rest_framework import serializers
from .models import MembershipPlan, PlanPrice, UserSubscription


class PlanPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanPrice
        fields = ['billing_cycle', 'currency', 'amount', 'trial_days']


class MembershipPlanSerializer(serializers.ModelSerializer):
    prices = PlanPriceSerializer(many=True, read_only=True)

    class Meta:
        model = MembershipPlan
        fields = ['id', 'code', 'name', 'description', 'tier_rank', 'is_free', 'features', 'limits', 'prices']


class UserSubscriptionSerializer(serializers.ModelSerializer):
    plan = MembershipPlanSerializer(read_only=True)

    class Meta:
        model = UserSubscription
        fields = ['id', 'plan', 'billing_cycle', 'currency', 'status', 'auto_renew', 'started_at', 'current_period_end', 'cancel_at_period_end']
