"""Database models for the lettings app."""

from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """Stores a single address entry.

    :param number: The street number.
    :param street: The street name.
    :param city: The city name.
    :param state: The state name.
    :param zip_code: The zip code.
    :param country_iso_code: The country ISO code.
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        return f'{self.number} {self.street}'

    class Meta:
        verbose_name_plural = 'Addresses'


class Letting(models.Model):
    """Stores a single letting entry.

    :param title: The title of the letting.
    :param address: The address of the letting (related to :class:`lettings.Address`).
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
