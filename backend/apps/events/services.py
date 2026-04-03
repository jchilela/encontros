from apps.subscriptions.models import UserSubscription


def has_plan_access(user, required_plan: str) -> bool:
    if required_plan in ('', 'none', None):
        return True
    if not user or not user.is_authenticated:
        return False
    subscription = UserSubscription.objects.filter(user=user, status='active').select_related('plan').first()
    if required_plan == 'silver':
        return bool(subscription and subscription.plan.code in {'silver', 'gold'})
    if required_plan == 'gold':
        return bool(subscription and subscription.plan.code == 'gold')
    return False
