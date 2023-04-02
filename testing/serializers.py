from rest_framework.serializers import ModelSerializer

from testing.models import TestModel


class TestSerializer(ModelSerializer):
    class Meta:
        model = TestModel
        fields = ("name",)
