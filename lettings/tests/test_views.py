import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_index_view(client, letting_paris, letting_london):
    path = reverse("lettings:index")
    response = client.get(path)
    content = response.content.decode()
    assert "Lettings" in content
    for letting in [letting_paris, letting_london]:
        assert letting.title in content
    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/index.html")


@pytest.mark.django_db
def test_letting_view(client, letting_london):
    path = reverse("lettings:letting", kwargs={"letting_id": 1})
    response = client.get(path)
    content = response.content.decode()
    assert letting_london.title in content
    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/letting.html")


@pytest.mark.django_db
def test_empty_lettings_list_view(client, caplog):
    path = reverse("lettings:index")
    response = client.get(path)
    assert response.status_code == 200
    assert "No letting found" in caplog.text
