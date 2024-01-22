"""Test models for the `lettings` app."""

import pytest

from lettings.models import Address, Letting


@pytest.mark.django_db
def test_address_fixture_type(address):
    """Test if ``address`` became a fixture of the instance type."""
    assert isinstance(address, Address)


@pytest.mark.django_db
def test_letting_fixture_type(letting):
    """Test if ``letting`` became a fixture of the instance type."""
    assert isinstance(letting, Letting)


@pytest.mark.django_db
def test_address_model(address):
    """Test :class:`lettings.Address` model attributes and meta."""
    assert address.number == 1
    assert address.street == "rue de la paix"
    assert address.city == "Paris"
    assert address.state == "FR"
    assert address.zip_code == 75000
    assert address.country_iso_code == "FR"
    assert str(address) == "1 rue de la paix"
    assert address._meta.verbose_name_plural == "Addresses"
    assert Address.objects.count() == 1


@pytest.mark.django_db
def test_letting_model(letting):
    """Test :class:`lettings.Letting` model attributes."""
    assert letting.title == "appartment in Paris"
    assert str(letting) == "appartment in Paris"
    assert letting.address.number == 1
    assert Letting.objects.count() == 1
