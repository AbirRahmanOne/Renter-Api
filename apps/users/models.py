from django.db import models
from django.contrib.auth.models import User, AbstractUser


# Create your models here.
#
class User(AbstractUser):
    user_type = models.CharField(max_length=50, blank=False)



