"""Test URL patterns for `profiles` app."""

import pytest
from django.urls import resolve, reverse


def test_index_url():
    """Test `index` URL pattern."""
    path = reverse("profiles:index")
    assert path == "/profiles/"
    assert resolve(path).view_name == "profiles:index"


@pytest.mark.django_db  # require at least one profile in the database
def test_profile_url(profile):
    """Test `profile` URL pattern."""
    path = reverse("profiles:profile", kwargs={"username": profile.user.username})
    assert path == f"/profiles/{profile.user.username}/"
    assert resolve(path).view_name == "profiles:profile"
