from django.db import models
from shortuuidfield import ShortUUIDField


class ShortIdModel(models.Model):
    id = ShortUUIDField(primary_key=True, editable=False)

    class Meta:
        abstract = True


class NameDescriptionModel(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=256)

    class Meta:
        abstract = True