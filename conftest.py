import pytest
from django.test import Client


@pytest.fixture
def client():
    client_obj = Client()
    return client_obj
