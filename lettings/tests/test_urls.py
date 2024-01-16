import pytest
from django.urls import resolve, reverse


def test_index_url():
    path = reverse("lettings:index")
    assert path == "/lettings/"
    assert resolve(path).view_name == "lettings:index"


@pytest.mark.django_db
def test_letting_url(letting):
    path = reverse("lettings:letting", kwargs={"letting_id": 1})
    assert path == "/lettings/1/"
    assert resolve(path).view_name == "lettings:letting"
