from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Group, GroupMembership
from .serializers import GroupSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by('-created_at')
    serializer_class = GroupSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def join(self, request, pk=None):
        group = self.get_object()
        status_value = 'pending' if group.access_rule == 'approval' else 'active'
        membership, _ = GroupMembership.objects.get_or_create(group=group, user=request.user, defaults={'status': status_value})
        return Response({'status': membership.status})
