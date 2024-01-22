"""Test URL patterns for :mod:`oc_lettings_site`."""

from django.urls import resolve, reverse


def test_index_url():
    """Test ``index`` URL pattern."""
    path = reverse("index")
    assert path == "/"
    assert resolve(path).view_name == "index"


def test_profiles_namespace():
    """Test ``profiles`` namespace."""
    resolver = resolve("/profiles/")
    assert resolver.namespace == "profiles"


def test_lettings_namespace():
    """Test ``lettings`` namespace."""
    resolver = resolve("/lettings/")
    assert resolver.namespace == "lettings"


def test_admin_namespace():
    """Test ``admin`` namespace."""
    resolver = resolve("/admin/")
    assert resolver.namespace == "admin"
