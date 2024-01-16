import pytest
from django.urls import resolve, reverse


def test_index_url():
    path = reverse("profiles:index")
    assert path == "/profiles/"
    assert resolve(path).view_name == "profiles:index"


@pytest.mark.django_db
def test_profile_url(profile):
    path = reverse("profiles:profile", kwargs={"username": profile.user.username})
    assert path == f"/profiles/{profile.user.username}/"
    assert resolve(path).view_name == "profiles:profile"
