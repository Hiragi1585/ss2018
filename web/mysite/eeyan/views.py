from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Event,User


# Create your views here.

def index(request):
    events = Event.objects.order_by("-start")
    users = User.objects.all()
    return render(request,"index.html",{"events":events,"users":users})


def loginForm(request):
    return HttpResponse("You're on login form.")


def login(request):
    username = request.POST["user_name"]
    password = request.POST["password"]
    
    """
    Login processing...
    ...
    ...
    """
    
    return HttpResponse("LoginSuccessed()")


def detail(request,event_id):
    event = Event.objects.get(id=event_id)
    return HttpResponse("You're on detail page of %s" % event.name)


def provider(request,user_id):
    user = User.objects.get(id=user_id)
    return HttpResponse("You're on provider user page of %s" % user.name)