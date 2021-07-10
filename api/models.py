from django.db import models


# Create your models here.

# Creating Flat Model below
class Flat(models.Model):
    name = models.CharField(unique=True, max_length=120)
    description = models.CharField(blank=True, max_length=200, null=True)
    flat_rent = models.CharField(max_length=10)
    e_meter_id = models.CharField(max_length=25, null=True)
    renter_id = models.CharField(blank=True, max_length=25, null=True)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
