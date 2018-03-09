from django.db import models
from datetime import datetime

# Create your models here.

ln = 1024 

class User(models.Model):
    user_name = models.CharField(max_length=ln)
    user_id = models.CharField(max_length=64)
    eeyan = models.IntegerField(default=0)
    password = models.CharField(max_length=32)
    beacon_id = models.CharField(max_length=10)
    url = models.CharField(max_length=1024)
    def __str__(self):
        return self.user_name


class Event(models.Model):    
    title = models.CharField(max_length=256)
    event_url = models.CharField(max_length=1024)
    start = models.DateTimeField()
    def __str__(self):
        return self.title


class LineUser(models.Model):
    user_name = models.CharField(max_length=ln)
    line_id = models.CharField(max_length=ln)
    timestamp = models.CharField(max_length=ln)
    hw_id = models.CharField(max_length=ln)
    reply_token = models.CharField(max_length=ln)
    freeday = models.DateTimeField()
    def __str__(self):
        return self.line_id+":"+self.timestamp
    
    
class log(models.Model):
    event = models.ForeignKey(Event,on_delete=models.CASCADE)
    user_name = models.CharField(max_length=ln)
    def __str__(self):
        return self.user_id + ":" + self.event_id
