import re

from django.core.validators import RegexValidator, MinValueValidator
from django.db import models

from django.db.models import SET_NULL


# Heading means first 4 digits of code.
heading_regex = re.compile("^[0-9]{4}$")
heading_validator = RegexValidator(heading_regex, "invalid heading")

# Digits 5,6,7...
_remaining_digits_regex = re.compile("^[0-9]{1,10}$")
_remaining_digits_validator = RegexValidator(
    _remaining_digits_regex, "invalid digits 5,6,7..."
)

_positive_validator = MinValueValidator(0, "Negative value not allowed")


class Heading(models.Model):
    heading_digits = models.CharField(
        primary_key=True,
        max_length=4,
        validators=[heading_validator],)
    description = models.CharField(max_length=200, blank=True)
    last_updated = models.DateTimeField()


class Commodity(models.Model):
    remaining_digits = models.CharField(
        max_length=10, validators=[_remaining_digits_validator],
    )
    belongs_to = models.ForeignKey(Heading, null=True, on_delete=SET_NULL)
    description = models.CharField(max_length=200, blank=True)
    indent = models.IntegerField()

    # TODO For MVP - the following numeric fields have no units,
    # and the duty is a plain number - (no =/-volume element)
    vat = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        blank=True,
        null=True,
        validators=[_positive_validator],
    )
    duty = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        blank=True,
        null=True,
        validators=[_positive_validator],
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        blank=True,
        null=True,
        validators=[_positive_validator],
    )
    volume = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        blank=True,
        null=True,
        validators=[_positive_validator],
    )