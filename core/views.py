from rest_framework import viewsets

from .serializers import StreakSerializer
from .models import Streak
class StreakViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing streaks.
    """
    queryset = Streak.objects.all()
    serializer_class = StreakSerializer
