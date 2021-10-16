from django.db import models
from shortuuidfield import ShortUUIDField

class ShortIdModel(models.Model):
    id = ShortUUIDField(primary_key=True, editable=False)

    class Meta:
        abstract = True