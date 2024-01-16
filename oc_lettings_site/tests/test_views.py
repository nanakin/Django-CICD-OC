import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed


def test_index_view(client):
    path = reverse("index")
    response = client.get(path)
    assert "Welcome to Holiday Homes" in response.content.decode()
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
    assert response.status_code == 200
    assert "Django administration" in content


def test_connected_admin_view(admin_client, admin_user):
    admin_client.login(username=admin_user.username, password=admin_user.password)
    response = admin_client.get("/admin/")
    assert response.status_code == 200
    content = response.content.decode()
    assert "Site administration" in content
    assert "Welcome" in content
