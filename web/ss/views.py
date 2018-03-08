from django.shortcuts import render
from django.http import HttpResponse
from .models import LineUser,Event,User


# Create your views here.

def index(request):
    return render(request,"ss/index.html")


def register(request):
    user_id = request.POST["user_id"]
    password = request.POST["password"]
    beacon_id = request.POST["beacon_id"]
    url = request.POST["url"]
    
    user = User()
    user.user_id = user_id
    user.user_password = password
    user.beacon_id = beacon_id
    user.user_url = url
    user.save()
    
    login(request)

def login(request):
    user_id = request.POST["user_id"]
    password = request.POST["password"]
    fatal = False
    #It's exactly Haribote!!!!
    if user_id == "admin" and password == "admin":
        HttpResponseRedirect("manager/")
    else:
        HttpResponseRedirect(reverse("index",args=(fatal)))
    


def receive(request):
    db_param = {
        "line_id":request.POST["line_id"],
        "hw_id":request.POST["hw_id"],
        "timestamp":request.POST["timestamp"],
    }
    
    data = LineUser()
    data.line_id = db_param["user_id"]
    data.hw_id = db_param["hw_id"]
    data.timestamp = db_param["timestamp"]
    
    data.save()
    
    print("DB_Inserted")
    print(LineUser.objects.all())
    
    owner = User.objects.filter(beacon_id=db_param["hw_id"])
    recent_event = Event.objects.filter(user=owner)
    print(recent_event)
    
    return HttpResponse("Data received")
