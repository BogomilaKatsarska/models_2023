from datetime import date

from django.core.exceptions import ValidationError


def validate_before_today(value):
    if date.today() < value:
        raise ValidationError('Vale is in the future.')
