from rest_framework.viewsets import GenericViewSet

from get_once.mixins import GetOnceMixin
from testing.models import TestModel
from testing.serializers import TestSerializer


class TestViewSet(GetOnceMixin, GenericViewSet):
    queryset = TestModel.objects.all()
    serializer_class = TestSerializer
