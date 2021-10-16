from django.db import models

from .base_models import ShortIdModel

class Streak(ShortIdModel):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=256)
    days_engaged = models.IntegerField()