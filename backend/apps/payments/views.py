from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import PaymentTransaction
from .services import ProprietaryGatewayService


class PaymentViewSet(viewsets.GenericViewSet):
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['post'])
    def proprietary_reference(self, request):
        order_number = request.data['order_number']
        amount = request.data['amount']
        currency = request.data.get('currency', 'EUR')
        payload = ProprietaryGatewayService().create_reference(order_number, amount, currency)
        return Response(payload)

    @action(detail=False, methods=['post'], permission_classes=[permissions.AllowAny])
    def proprietary_callback(self, request):
        reference = request.data.get('reference_code')
        PaymentTransaction.objects.filter(external_reference=reference).update(status='paid')
        return Response({'detail': 'Callback recebido.'})
