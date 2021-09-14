from django.db import models


# Create your models here.

class Flat(models.Model):
    name = models.CharField(unique=True, max_length=50)
    description = models.CharField(blank=True, max_length=200, null=True)
    flat_rent = models.IntegerField()
    electric_meter = models.CharField(max_length=30, null=True)
    renter_id = models.CharField(blank=True, max_length=30, null=True)
    status = models.CharField(blank=True,max_length=50, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
