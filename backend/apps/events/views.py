from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Event, RSVP, WaitlistEntry
from .serializers import EventSerializer, RSVPSerializer
from .services import has_plan_access


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('starts_at')
    serializer_class = EventSerializer
    filterset_fields = ['event_format', 'city', 'category', 'status']
    search_fields = ['title', 'summary', 'description', 'venue_name', 'address_line']
    ordering_fields = ['starts_at', 'created_at']

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def rsvp(self, request, pk=None):
        event = self.get_object()
        if not has_plan_access(request.user, event.required_plan):
            return Response({'detail': 'O teu plano não permite acesso a este evento.'}, status=403)

        current_confirmed = event.rsvps.filter(status='confirmed').count()
        if event.capacity and current_confirmed >= event.capacity:
            if event.waitlist_enabled:
                entry, _ = WaitlistEntry.objects.get_or_create(event=event, user=request.user)
                return Response({'status': 'waitlist', 'entry_id': str(entry.id)}, status=202)
            return Response({'detail': 'Evento esgotado.'}, status=409)

        rsvp, _ = RSVP.objects.get_or_create(event=event, user=request.user, defaults={'status': 'confirmed'})
        if rsvp.status != 'confirmed':
            rsvp.status = 'confirmed'
            rsvp.save(update_fields=['status', 'updated_at'])
        return Response(RSVPSerializer(rsvp).data, status=201)


class RSVPViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = RSVPSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return RSVP.objects.filter(user=self.request.user).select_related('event')
