from django.db import models

# Create your models here.


class User(models.Model):
    user_id = models.CharField(max_length=64)
    user_password = models.CharField(max_length=32)
    beacon_id = models.CharField(max_length=10)
    user_url = models.CharField(max_length=1024)
    def __str__(self):
        return self.user_id


class Event(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    zip_code = models.CharField(max_length=7)
    address = models.TextField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    discribe = models.TextField()
    event_url = models.CharField(max_length=1024)
    def __str__(self):
        return self.title
   