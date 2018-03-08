from django.shortcuts import render
from django.http import HttpResponse
from .models import Beacon,Event,User


# Create your views here.

def index(request):
    return render(request,"ss/index.html")


def register(request):
    pass


def receive(request):
    db_param = {
        "user_id":request.POST["user_id"],
        "hw_id":request.POST["hw_id"],
        "timestamp":request.POST["timestamp"],
    }
    
    data = Beacon()
    data.user_id = db_param["user_id"]
    data.hw_id = db_param["hw_id"]
    data.timestamp = db_param["timestamp"]
    
    data.save()
    
    print("DB_Inserted")
    print(Beacon.objects.all())
    
    owner = User.objects.filter(beacon_id=db_param["hw_id"])
    print(owner)
    
    return HttpResponse("Data received")
