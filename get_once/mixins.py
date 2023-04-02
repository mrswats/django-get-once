import copy
from collections.abc import Callable

from django.db.models import Model
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import Serializer


class GetOnceMixin:
    get_object: Callable[[], Model]
    get_serializer: Callable[[Model], type[Serializer]]

    def retrieve(self, request: Request, *args, **kwargs) -> Response:
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        serializer_data = copy.deepcopy(serializer.data)
        instance.delete()
        return Response(serializer_data)
