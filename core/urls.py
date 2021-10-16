from rest_framework import routers

from .views import StreakViewSet

router = routers.SimpleRouter()
router.register(r'streaks', StreakViewSet)
urlpatterns = router.urls