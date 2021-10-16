from rest_framework import serializers

from .models import Streak
from .publishing import PublishStatus

class StreakSerializer(serializers.ModelSerializer):

    published = serializers.ChoiceField(choices=PublishStatus.list())

    class Meta:
        model = Streak
        fields = ['id', 'name', 'description', 'days_engaged', 'published']
        read_only_fields = ['id']