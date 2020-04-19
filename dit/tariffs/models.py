import re
from enum import Enum

from django.core.validators import RegexValidator, MinValueValidator
from django.db import models

from django.db.models import SET_NULL, CASCADE


# Heading means first 4 digits of code.
heading_regex = re.compile("^[0-9]{4}$")
heading_validator = RegexValidator(heading_regex, "invalid heading")

# Digits 5,6,7...
_remaining_digits_regex = re.compile("^[0-9]{1,10}$")
_remaining_digits_validator = RegexValidator(
    _remaining_digits_regex, "invalid digits 5,6,7..."
)

_positive_validator = MinValueValidator(0, "Negative value not allowed")


class Units(Enum):
    G = "g"
    KG = "Kg"
    TONNE = "Tonne"
    UNSPECIFIED = "Unspecified"


class LastUpdated(models.Model):
    """
    Keeps track of how old the data about a heading is.
    """

    heading = models.CharField(
        max_length=4, primary_key=True, validators=[heading_validator],
    )
    when = models.DateTimeField()


class Duty(models.Model):
    """
    Encapsulates the parameters that define a Third Country Duty.
    """

    base_rate = models.DecimalField(
        max_digits=4, decimal_places=2, blank=True, validators=[_positive_validator],
    )
    volume_rate = models.DecimalField(
        max_digits=4, decimal_places=2, blank=True
    )  # Can be negative!
    volume_units = models.CharField(
        max_length=99,
        choices=[(u.value, u.name) for u in Units],
        default=Units.UNSPECIFIED,
    )


class Product(models.Model):
    """
    The core model - one HS Code and its tariffs etc.
    """

    heading_digits = models.CharField(max_length=4, validators=[heading_validator],)
    remaining_digits = models.CharField(
        max_length=10, validators=[_remaining_digits_validator],
    )
    description = models.CharField(max_length=200, blank=True)
    parent = models.ForeignKey("Product", blank=True, null=True, on_delete=SET_NULL)
    vat = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        blank=True,
        null=True,
        validators=[_positive_validator],
    )
    # The duty details as fetched from a gov.uk source.
    govuk_duty = models.OneToOneField(
        Duty, related_name="product_as_gov", on_delete=CASCADE, blank=True, null=True,
    )
    # The duty experimentally overridden to explore revenue implications.
    overridden_duty = models.OneToOneField(
        Duty,
        related_name="product_as_override",
        on_delete=CASCADE,
        blank=True,
        null=True,
    )
