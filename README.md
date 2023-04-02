# Django Get Once

A Django Rest Framework Mixin for viewsets that only allows you to retrieve an object exactly once.

## Installation

From PYPi using `pip`:

```
pip install django-get-once
```

## Usage

Can only be used with ViewSets:

```python
from get_once import GetOnceMixin
from rest_framework.viewset import GenericViewSet

class MyViewSet(GetOnceMixin, GenericViewSet):
    [...]
```

## Licence

This package is distributed under [MIT Licence](./LICENCE).
