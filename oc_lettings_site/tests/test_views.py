from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed


def test_index_view(client):
    path = reverse("index")
    response = client.get(path)
    content = response.content.decode()
    assert "Welcome to Holiday Homes" in content
    assert response.status_code == 200
    assertTemplateUsed(response, "oc_lettings_site/index.html")


def test_admin_view(client):
    response = client.get("/admin/login/")
    content = response.content.decode()
    assert "Django administration" in content
    assert response.status_code == 200
