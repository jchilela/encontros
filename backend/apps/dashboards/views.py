from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.events.models import Event, RSVP
from apps.communities.models import Group, GroupMembership
from apps.subscriptions.models import UserSubscription
from apps.tickets.models import Order
from apps.users.models import User
from apps.moderation.models import Report


class MemberDashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        subscription = UserSubscription.objects.filter(user=request.user).select_related('plan').order_by('-created_at').first()
        return Response({
            'plano_atual': subscription.plan.name if subscription else 'Sem pacote pago',
            'beneficios_ativos': subscription.plan.features if subscription else [],
            'proxima_cobranca': subscription.current_period_end if subscription else None,
            'eventos_inscritos': RSVP.objects.filter(user=request.user, status='confirmed').count(),
            'grupos_aderidos': GroupMembership.objects.filter(user=request.user, status='active').count(),
            'historico_pagamentos': Order.objects.filter(buyer=request.user, status='paid').count(),
        })


class OrganizerDashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        events = Event.objects.filter(organizer=request.user)
        return Response({
            'eventos_criados': events.count(),
            'participantes': RSVP.objects.filter(event__in=events, status='confirmed').count(),
            'receita': str(sum(order.total for order in Order.objects.filter(event__in=events, status='paid'))),
            'grupos_geridos': Group.objects.filter(owner=request.user).count(),
        })


class AdminDashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            'numero_utilizadores': User.objects.count(),
            'assinantes': UserSubscription.objects.filter(status='active').count(),
            'eventos_criados': Event.objects.count(),
            'denuncias_pendentes': Report.objects.filter(status='pending').count(),
            'organizadores': User.objects.filter(role='organizer').count(),
        })
