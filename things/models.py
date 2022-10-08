from django.db import models
from django.db.models import Model
from django.core.validators import MinValueValidator, MaxValueValidator

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
        validators = [MinValueValidator(0), MaxValueValidator(100)]
    )
