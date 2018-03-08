from django.shortcuts import render
from django.http import HttpResponse

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
    
    for key,value in db_param.items():
        print(key + ":" + value)
    return HttpResponse("Data received")
