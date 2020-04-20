import re

from django.core.validators import RegexValidator, MinValueValidator
from django.db import models

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
        primary_key=True, max_length=4, validators=[heading_validator],
    )
    description = models.CharField(max_length=200, blank=True)
    last_updated = models.DateTimeField()


class Commodity(models.Model):
    remaining_digits = models.CharField(
        max_length=10, validators=[_remaining_digits_validator],
    )
    belongs_to = models.ForeignKey(Heading, null=True, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, blank=True)
    is_leaf = models.BooleanField(default=False)
    indent = models.IntegerField(default=0)

    # TODO For MVP - the following numeric-like fields should be number types,
    # and have units - to support calculations.
    # And have validators!
    vat = models.CharField(max_length=4, blank=True, null=True,)
    duty = models.CharField(max_length=20, blank=True, null=True,)
    price = models.CharField(max_length=9, blank=True, null=True,)
    volume = models.CharField(max_length=9, blank=True, null=True,)
