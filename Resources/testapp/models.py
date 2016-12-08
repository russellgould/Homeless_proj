from django.db import models

# Create your models here.
class PITSubpopulations(models.Model):
    Tab = models.CharField(max_length=18)
    Pop_Type = models.CharField(max_length=35)
    Shelter = models.CharField(max_length=11)
    Date = models.DateField()
    Value = models.IntegerField(null=True,blank=True)

class PitSummary(models.Model):
    Tab = models.CharField(max_length=19)
    Value = models.CharField(max_length=20, null=True, blank=True)
    Pop_Type = models.CharField(max_length=37)
    Shelter = models.CharField(max_length=37)
    Date = models.DateField()