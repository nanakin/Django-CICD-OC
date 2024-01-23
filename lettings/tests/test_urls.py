"""Test URL patterns for `lettings` app."""

import pytest
from django.urls import resolve, reverse


def test_index_url():
    """Test `index` URL pattern."""
    path = reverse("lettings:index")
    assert path == "/lettings/"
    assert resolve(path).view_name == "lettings:index"


@pytest.mark.django_db  # require at least one letting in the database
def test_letting_url(letting):
    """Test `letting` URL pattern."""
    path = reverse("lettings:letting", kwargs={"letting_id": 1})
    assert path == "/lettings/1/"
    assert resolve(path).view_name == "lettings:letting"
