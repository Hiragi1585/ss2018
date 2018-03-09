from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import LineUser,Event,User


# Create your views here.

def index(request):
    events = Event.objects.all()
    users = LineUser.objects.all()
    return render(request,"ss/index.html",{"events":events,"users":users})


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

    
def form(request):
    return render(request,"ss/form.html")


def event(request,user_id):
    return HttpResponse("You're on event page.")


def modify(request,user_id):
    return HttpResponse("You're on modify page.")


def detail(request,event_id):
    return HttpResponse("You're on detail page about %d" % event_id)


def eventList(request,line_id):
    return HttpResponse("You're on eventList page of %s" % User.objects.get(id=line_id))


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
    import json
    db_param = {
        "user_name":request.POST["user_name"],
        "line_id":request.POST["line_id"],
        "hw_id":request.POST["hw_id"],
        "timestamp":request.POST["timestamp"],
        "reply_token":request.POST["reply_token"],
    }
    
    jd = json.dumps(db_param)
    
    data = LineUser.objects.filter(line_id=db_param["line_id"])
    if str(data) == "<QuerySet []>":
        print("Fatal to Find Query")
        data = LineUser()
        data.line_id = db_param["line_id"]
        data.user_name = db_param["user_name"]
    else:
        print("Find Query")
        data = LineUser.objects.get(line_id=db_param["line_id"])
  
    data.hw_id = db_param["hw_id"]
    data.timestamp = db_param["timestamp"]
    data.reply_token = db_param["reply_token"]
#    data.freeday = timezone.now
    data.freeday = "2018-03-15"
    data.save()
    close_user = {}
    
    response = data.hw_id+"\n"+data.timestamp+"\n"+data.freeday
    
    return HttpResponse(jd)