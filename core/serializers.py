from rest_framework import serializers

from .models import Streak

class StreakSerializer(serializers.ModelSerializer):
    class Meta:
        model = Streak
        fields = ['id', 'name', 'description', 'days_engaged']