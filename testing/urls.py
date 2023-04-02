from rest_framework.routers import SimpleRouter

from testing.views import TestViewSet

router = SimpleRouter()
router.register("test", TestViewSet, basename="test")

urlpatterns = router.urls
