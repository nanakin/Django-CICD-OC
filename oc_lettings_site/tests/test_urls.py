from django.urls import resolve, reverse


def test_index_url():
    path = reverse("index")
    assert path == "/"
    assert resolve(path).view_name == "index"


def test_profiles_namespace():
    resolver = resolve("/profiles/")
    assert resolver.namespace == "profiles"


def test_lettings_namespace():
    resolver = resolve("/lettings/")
    assert resolver.namespace == "lettings"


def test_admin_namespace():
    resolver = resolve("/admin/")
    assert resolver.namespace == "admin"
