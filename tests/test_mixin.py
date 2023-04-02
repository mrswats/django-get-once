import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from testing.models import TestModel


@pytest.fixture
def model():
    return TestModel.objects.create(name="test-name")


@pytest.fixture
def get(model):
    client = APIClient()
    url = reverse("test-detail", kwargs={"pk": model.pk})
    return client.get(url)


@pytest.mark.django_db
def test_view_returns_ok_status_code(get):
    assert get.status_code == 200


@pytest.mark.django_db
def test_view_returns_object_data(get):
    assert get.json() == {"name": "test-name"}


@pytest.mark.django_db
def test_view_deletes_object_after_retrieve(get):
    assert TestModel.objects.count() == 0
