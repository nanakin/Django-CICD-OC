import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_index_view(client, profile_elisa, profile_peter):
    path = reverse("profiles:index")
    response = client.get(path)
    content = response.content.decode()
    assert "Profiles" in content
    for profile in [profile_elisa, profile_peter]:
        assert profile.user.username in content
    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/index.html")


@pytest.mark.django_db
def test_profile_view(client, profile_peter):
    path = reverse("profiles:profile", kwargs={"username": "peter"})
    response = client.get(path)
    content = response.content.decode()
    assert profile_peter.user.username in content
    assert profile_peter.user.last_name in content
    assert profile_peter.favorite_city in content
    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/profile.html")


@pytest.mark.django_db
def test_empty_profiles_list_view(client, caplog):
    path = reverse("profiles:index")
    response = client.get(path)
    assert response.status_code == 200
    assert "No profile found" in caplog.text
