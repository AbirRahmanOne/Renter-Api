from django.db import models

# Create your models here.


class Renter(models.Model):
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=200)
    nid = models.CharField(unique=True, max_length=50)
    # NID_Image_Scan
    # Avatar (recent Picture)

    def __str__(self):
        return self.name