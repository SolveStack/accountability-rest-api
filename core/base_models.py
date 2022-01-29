from django.db import models
from shortuuidfield import ShortUUIDField


class AuditTrailModel(models.Model):
    id = ShortUUIDField(primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by = ShortUUIDField(blank=True, null=True)
    modified_by = ShortUUIDField(blank=True, null=True)

    class Meta:
        abstract = True


class NameDescriptionModel(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=256)

    class Meta:
        abstract = True