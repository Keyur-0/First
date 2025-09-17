from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello,World!")

def Keyur(request):
    return HttpResponse("Hello,Keyur!")

def Greet(request,name):
    return render(request, "Hello/Greet.html", {
        "name": name.capitalize()
    })