from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter

from apps.users.views import AuthViewSet, ProfileViewSet
from apps.events.views import EventViewSet, RSVPViewSet
from apps.communities.views import GroupViewSet
from apps.subscriptions.views import PlanViewSet, SubscriptionViewSet
from apps.payments.views import PaymentViewSet
from apps.messaging.views import ConversationViewSet
from apps.notifications.views import NotificationViewSet
from apps.dashboards.views import MemberDashboardView, OrganizerDashboardView, AdminDashboardView

router = DefaultRouter()
router.register('auth', AuthViewSet, basename='auth')
router.register('profile', ProfileViewSet, basename='profile')
router.register('events', EventViewSet, basename='events')
router.register('rsvps', RSVPViewSet, basename='rsvps')
router.register('groups', GroupViewSet, basename='groups')
router.register('plans', PlanViewSet, basename='plans')
router.register('subscriptions', SubscriptionViewSet, basename='subscriptions')
router.register('payments', PaymentViewSet, basename='payments')
router.register('conversations', ConversationViewSet, basename='conversations')
router.register('notifications', NotificationViewSet, basename='notifications')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/dashboards/member/', MemberDashboardView.as_view()),
    path('api/v1/dashboards/organizer/', OrganizerDashboardView.as_view()),
    path('api/v1/dashboards/admin/', AdminDashboardView.as_view()),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
