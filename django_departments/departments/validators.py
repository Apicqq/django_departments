import datetime
from decimal import Decimal

from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.utils.timezone import now

min_length_validator = MinLengthValidator(1)

salary_min_value_validator = MinValueValidator(Decimal("0.01"))


def validate_hired_at(value: datetime.date) -> None:
    if value > now():
        raise ValidationError("Дата приема на работу не может быть в будущем.")
