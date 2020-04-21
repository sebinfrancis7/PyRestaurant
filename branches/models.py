from django.db import models

# Create your models here.
class Branch(models.Model):
    location = models.CharField(max_length=10)
    manager = models.CharField(max_length=30)