"""This file contains common fixtures for pytest tests."""

import pytest
from django.test import Client


@pytest.fixture
def client():
    """Return a Django test client."""
    client_obj = Client()
    return client_obj
