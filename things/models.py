from django.db import models
from django.db.models import Model

# Create your models here.
class Thing(Model):
    name = models.CharField(
        max_length=30,
        blank=False,
        unique=True,
    )
    description = models.CharField(
        max_length=120
    )
    quantity = models.IntegerField(
        min_length = 0,
        max_length = 100
    )
