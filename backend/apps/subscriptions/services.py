from decimal import Decimal


def calculate_proration(old_amount: Decimal, new_amount: Decimal, remaining_ratio: Decimal) -> Decimal:
    credit = old_amount * remaining_ratio
    debit = new_amount * remaining_ratio
    return max(debit - credit, Decimal('0.00'))
