from rest_framework import routers

from .views import DayStreakGoalViewSet

router = routers.SimpleRouter()
router.register(r"DayStreakGoals", DayStreakGoalViewSet)
urlpatterns = router.urls
