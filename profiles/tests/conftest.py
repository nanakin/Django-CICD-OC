"""
Factories declaration related to the `lettings` app.

fixtures created:
- profile (also aliased profile_elisa): Elisa's profile
- profile_peter: Peter's profile
- user_admin: a superuser

note:
Factories aim to simplify tests' setup by providing an easy-to-use interface for building
complicated objects and relations (especially when combined with subfactories, lazy attributes and
faker).
"""

import factory
import pytest
from django.contrib.auth.models import User
from pytest_factoryboy import register

from profiles.models import Profile


@register
@register(_name="user_elisa")  # alias the default factory
@register(_name="user_peter", username="peter", last_name="Parker")
@register(_name="user_admin", username="thomadmin", is_superuser=True, is_staff=True,
          is_active=True, email='admin@admin.com',
          password=factory.PostGenerationMethodCall('set_password', 'adm1n'))
class UserFactory(factory.django.DjangoModelFactory):
    """Factory for `User` model."""
    class Meta:
        model = User

    username = "elisa"
    last_name = "Dupont"


@register
@register(_name="profile_elisa")  # alias the default factory
@register(_name="profile_peter", favorite_city="London")
class ProfileFactory(factory.django.DjangoModelFactory):
    """Factory for `Profile` model."""
    class Meta:
        model = Profile

    favorite_city = "Paris"
    user = factory.SubFactory(UserFactory)


@pytest.fixture
def profile_peter__user(user_peter):
    """Make the link between the Peter profile and the Peter user."""
    return user_peter
