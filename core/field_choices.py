from django.db import models
from django.utils.translation import gettext_lazy as _


class PublishStatusChoices(models.TextChoices):
    PUBLISHED = "published"
    QA = "qa", _("Q/A")
    DRAFT = "draft"


class NumberOfServingsRepresentationChoices(models.TextChoices):
    FRACTIONS = "fractions", _("Fractions")
    DECIMAL = "decimal", _("Decimal")


class FractionDenominatorChoices(models.IntegerChoices):
    HALF = 2
    THIRD = 3
    QUARTER = 4
    EIGHTH = 8


class UnitOfMeasureTypeChoices(models.TextChoices):
    FOOD = "food"
    TIME = "time"


class OneToTenMeasurementTypeChoices(models.TextChoices):
    STOP = "stop"
    START = "start"
    CONTINUE = "continue"
