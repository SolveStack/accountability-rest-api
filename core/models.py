
from django.core.validators import MinValueValidator
from django.db import models

from shortuuidfield import ShortUUIDField

from .base_models import AuditTrailModel, NameDescriptionModel
from .field_choices import (
    PublishStatusChoices,
    NumberOfServingsRepresentationChoices,
    FractionDenominatorChoices,
    OneToTenMeasurementTypeChoices,
    UnitOfMeasureTypeChoices,
)


class DayStreakGoal(AuditTrailModel, NameDescriptionModel):
    id = ShortUUIDField(primary_key=True, editable=False)
    days_engaged = models.IntegerField(validators=[MinValueValidator(0)])
    published = models.CharField(default=PublishStatusChoices.DRAFT, choices=PublishStatusChoices.choices, max_length=80)
    # TODO: owner


# TODO: subscriber


class UnitOfMeasure(AuditTrailModel):
    id = ShortUUIDField(primary_key=True, editable=False)
    name = models.CharField(max_length=80)
    plural = models.CharField(max_length=80)
    unit_of_measure_type = models.CharField(choices=UnitOfMeasureTypeChoices.choices, max_length=80)


class ConsumptionPerDayGoal(AuditTrailModel, NameDescriptionModel):
    id = ShortUUIDField(primary_key=True, editable=False)
    units = models.ForeignKey("UnitOfMeasure", on_delete=models.SET_NULL, blank=True, null=True)
    representation = models.CharField(
        default=NumberOfServingsRepresentationChoices.DECIMAL, choices=NumberOfServingsRepresentationChoices.choices, max_length=80
    )
    fraction_whole_number = models.IntegerField(validators=[MinValueValidator(0)], null=True)
    fraction_numerator = models.IntegerField(validators=[MinValueValidator(0)], null=True)
    fraction_denominator = models.IntegerField(choices=FractionDenominatorChoices.choices, null=True)
    # TODO: owner


class AmountOfTimePerDayGoal(AuditTrailModel, NameDescriptionModel):
    id = ShortUUIDField(primary_key=True, editable=False)
    duration = models.DurationField()


class TimesPerDayStreakGoal(AuditTrailModel, NameDescriptionModel):
    id = ShortUUIDField(primary_key=True, editable=False)
    times_engaged = models.IntegerField(validators=[MinValueValidator(0)])


class OneToTenMeasurement(AuditTrailModel, NameDescriptionModel):
    id = ShortUUIDField(primary_key=True, editable=False)
    one_to_ten_measurement_type = models.CharField(choices=OneToTenMeasurementTypeChoices.choices, max_length=80)
