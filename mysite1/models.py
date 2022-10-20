from django.db import models

class test(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
# Create your models here.

class Processors(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    description = models.CharField(max_length=255)

class Cards(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    description = models.CharField(max_length=255)

class Plates(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    description = models.CharField(max_length=255)

def __str__(self):
    return self.name
