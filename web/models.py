from django.db import models

# Create your models here.
class Region(models.Model):
    id = models.IntegerField(primary_key=True, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)

class Comuna(models.Model):
    #se omite el id para que la ORM lo genere automaticamente
    name = models.CharField(max_length=50, null=False, blank=False)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

class UserType(models.Model):
    type = models.CharField(max_length=25, primary_key=True)
    canAdmin = models.BooleanField(default=False)

class User(models.Model):
    pass