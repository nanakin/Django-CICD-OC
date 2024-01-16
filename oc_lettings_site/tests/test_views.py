import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed


def test_index_view(client):
    path = reverse("index")
    response = client.get(path)
    content = response.content.decode()
    assert "Welcome to Holiday Homes" in content
    assert response.status_code == 200
    assertTemplateUsed(response, "oc_lettings_site/index.html")


def test_404_view(client):
    response = client.get("/invalidurl/")
    assert response.status_code == 404
    assert "Page not found" in response.content.decode()
    assertTemplateUsed(response, "404.html")


@pytest.mark.django_db
def test_500_view(client):
    client.raise_request_exception = False
    response = client.get("/profiles/invalidusername/")
    assert response.status_code == 500
    assert "Internal Server Error" in response.content.decode()
    assertTemplateUsed(response, "500.html")


def test_admin_view(client):
    response = client.get("/admin/login/")
    content = response.content.decode()
    assert "Django administration" in content
    assert response.status_code == 200
