from django.db import models
from datetime import datetime, date
# Create your models here.
class ReserveInfo(models.Model):
    Name = models.CharField(max_length=20,blank=False)
    Email = models.CharField(max_length=25,blank=False)
    People = models.IntegerField(blank=False)
    
