import pytest

from profiles.models import Profile


@pytest.mark.django_db
def test_profile_fixture_type(profile):
    """Test if profile became a fixture of the instance type."""
    assert isinstance(profile, Profile)


@pytest.mark.django_db
def test_profile_model(profile):
    """Test profile model attributes."""
    assert profile.favorite_city == "Paris"
    assert profile.user.username == "elisa"
    assert str(profile) == "elisa"
    assert Profile.objects.count() == 1
