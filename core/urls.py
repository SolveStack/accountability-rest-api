from rest_framework import routers

from .views import DayStreakGoalViewSet

router = routers.SimpleRouter()
router.register(r"day-streak-goals", DayStreakGoalViewSet, basename="day-streak-goals")
urlpatterns = router.urls
