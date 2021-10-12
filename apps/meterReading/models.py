from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from apps.flats.models import Flat

# Create your models here.


class MeterReading(models.Model):
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE, null=True) #Q
    # name = models.CharField(unique=True, max_length=20)
    current_reading = models.FloatField()
    month = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
    year = models.SmallIntegerField()
    #
    # class Meta:
    #     unique_together = ('flat', 'month', 'year')

    def __str__(self):
        self.name
