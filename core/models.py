from django.db import models

from .base_models import ShortIdModel
from .publishing import PublishStatus

class Streak(ShortIdModel):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=256)
    days_engaged = models.IntegerField()
    published = models.CharField(default=PublishStatus.DRAFT, choices=PublishStatus.list(), max_length=80)