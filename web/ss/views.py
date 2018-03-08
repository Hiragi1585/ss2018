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
        "reply_token":request.POST["reply_token"],
    }
    
    data = LineUser.objects.filter(line_id=db_param["line_id"])
    if str(data) == "<QuerySet []>":
        print("Fatal to Find Query")
        data = LineUser()
        data.line_id = db_param["line_id"]
        data.hw_id = db_param["hw_id"]
        data.timestamp = db_param["timestamp"]
        data.reply_token = db_param["reply_token"]
        data.save()
    else:
        print("Find Query")
        data = LineUser.objects.get(line_id=db_param["line_id"])
        data.hw_id = db_param["hw_id"]
        data.timestamp = db_param["timestamp"]
        data.reply_token = db_param["reply_token"]
        data.save()
    
    close_user = {}
    
    data = LineUser.objects.order_by("-timestamp")[:10]
    print(data.raw)
    return HttpResponse("Data received")
