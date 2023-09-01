from django.shortcuts import render, HttpResponse
from . import ex3 as e
# Create your views here.

def index(request):
    return render(request,'index.html')

def tshirt(request):
    if request.method =="POST":
        vid=e.video()
        if vid==True:
            return render(request, "index.html", {'alert_message': "You came out of Frame!!!!"})
        return render(request,'index.html')

def specs(request):
    if request.method =="POST":
        spec=e.specs()
        if spec==True:
            return render(request, "index.html", {'alert_message': "You came out of Frame!!!!"})
        return render(request,'index.html')

def jewellery(request):
    if request.method =="POST":
        jew=e.jewellery()
        if jew==True:
            return render(request, "index.html", {'alert_message': "You came out of Frame!!!!"})
        return render(request,'index.html')
