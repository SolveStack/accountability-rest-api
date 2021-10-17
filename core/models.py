from django.core import validators
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models.enums import Choices
from django.db.models.fields import DurationField

from .base_models import ShortIdModel, NameDescriptionModel
from .field_choices import (
    PublishStatusChoices,
    NumberOfServingsRepresentationChoices,
    FractionDenominatorChoices,
    OneToTenMeasurementTypeChoices,
    UnitOfMeasureTypeChoices,
)


class DayStreakGoal(ShortIdModel, NameDescriptionModel):
    days_engaged = models.IntegerField(validators=[MinValueValidator(0)])
    published = models.CharField(default=PublishStatusChoices.DRAFT, choices=PublishStatusChoices.choices, max_length=80)
    # TODO: owner


# TODO: subscriber


class UnitOfMeasure(ShortIdModel):
    name = models.CharField(max_length=80)
    plural = models.CharField(max_length=80)
    unit_of_measure_type = models.CharField(choices=UnitOfMeasureTypeChoices.choices, max_length=80)


class ConsumptionPerDayGoal(ShortIdModel, NameDescriptionModel):
    units = models.ForeignKey("UnitOfMeasure", on_delete=models.SET_NULL, blank=True, null=True)
    representation = models.CharField(
        default=NumberOfServingsRepresentationChoices.DECIMAL, choices=NumberOfServingsRepresentationChoices.choices, max_length=80
    )
    fraction_whole_number = models.IntegerField(validators=[MinValueValidator(0)], null=True)
    fraction_numerator = models.IntegerField(validators=[MinValueValidator(0)], null=True)
    fraction_denominator = models.IntegerField(choices=FractionDenominatorChoices.choices, null=True)
    # TODO: owner


class AmountOfTimePerDayGoal(ShortIdModel, NameDescriptionModel):
    duration = models.DurationField()


class TimesPerDayStreakGoal(ShortIdModel, NameDescriptionModel):
    times_engaged = models.IntegerField(validators=[MinValueValidator(0)])


class OneToTenMeasurement(ShortIdModel, NameDescriptionModel):
    one_to_ten_measurement_type = models.CharField(choices=OneToTenMeasurementTypeChoices.choices, max_length=80)
