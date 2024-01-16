import factory
import pytest
from django.contrib.auth.models import User
from pytest_factoryboy import register

from profiles.models import Profile


@register
@register(_name="user_elisa")  # alias the default factory
@register(_name="user_peter", username="peter", last_name="Parker")
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = "elisa"
    last_name = "Dupont"


@register
@register(_name="profile_elisa")  # alias the default factory
@register(_name="profile_peter", favorite_city="London")
class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Profile

    favorite_city = "Paris"
    user = factory.SubFactory(UserFactory)


@pytest.fixture
def profile_peter__user(user_peter):
    """Make the link between the peter profile and the peter user."""
    return user_peter
