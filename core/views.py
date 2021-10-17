from rest_framework import viewsets

from .serializers import DayStreakGoalSerializer
from .models import DayStreakGoal


class DayStreakGoalViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing DayStreakGoals.
    """

    queryset = DayStreakGoal.objects.all()
    serializer_class = DayStreakGoalSerializer
