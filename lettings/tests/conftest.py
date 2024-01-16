import factory
import pytest
from pytest_factoryboy import register

from lettings.models import Address, Letting


@register
@register(_name="address_paris")  # alias the default factory
@register(_name="address_london", city="London")
class AddressFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Address

    number = 1
    street = "rue de la paix"
    city = "Paris"
    state = "FR"
    zip_code = 75000
    country_iso_code = "FR"


@register
@register(_name="letting_paris")  # alias the default factory
@register(_name="letting_london", title="house in London")
class LettingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Letting

    title = "appartment in Paris"
    address = factory.SubFactory(AddressFactory)


@pytest.fixture
def letting_london__address(address_london):
    """Make the relation between the london letting and the london address."""
    return address_london
