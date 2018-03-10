from django.db import models
from django.utils import timezone
from datetime import datetime


normal = 64

class Line(models.Model):
    lid = models.CharField(max_length=33)
    name = models.CharField(max_length=normal)
    reply_token = models.CharField(max_length=normal)
    timestamp = models.CharField(max_length=normal)
    hwid = models.CharField(max_length=normal)
    
    def __str__(self):
        return self.name
    
class Place(models.Model):
    x = models.FloatField(null=True)
    y = models.FloatField(null=True)
    zipcode = models.CharField(max_length=7)
    address = models.CharField(max_length=normal)

    def __str__(self):
        return self.zipcode


    
    
class User(models.Model):
    name = models.CharField(max_length=normal)
    password = models.CharField(max_length=normal)
    place = models.ForeignKey(Place,on_delete=models.CASCADE,null=True,blank=True)
    hwid = models.CharField(max_length=10)
    status = models.IntegerField(default=0)
    
    
    def __str__(self):
        return self.name        
    
    
class Event(models.Model):
    provider = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=normal)
    discribe = models.TextField()
    start = models.DateTimeField(blank=True)
    
    def __str__(self):
        return self.name
    
    def isClose(self):
        return (timezone.now - self.start) < datetime.timedelta(days=7)    
    
