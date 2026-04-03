from decimal import Decimal


class ProprietaryGatewayService:
    def create_reference(self, order_number: str, amount: Decimal, currency: str) -> dict:
        return {
            'provider': 'proprietary',
            'reference_code': f'REF-{order_number}',
            'amount': str(amount),
            'currency': currency,
            'callback_expected': True,
        }
