from rest_framework import serializers

from .models import DayStreakGoal
from .field_choices import PublishStatusChoices


class DayStreakGoalSerializer(serializers.ModelSerializer):

    published = serializers.ChoiceField(choices=PublishStatusChoices.choices)

    class Meta:
        model = DayStreakGoal
        fields = ["id", "name", "description", "days_engaged", "published"]
        read_only_fields = ["id"]
