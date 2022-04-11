from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from datetime import datetime

from .models import *

# Create your views here.
def rexsite(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    else:
        return render(request, "rexsite/index.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("rexsite"))
        else:
             render(request, "rexsite/login.html", {
            "message": "Invalid Credentials"
        })

    return render(request, "rexsite/login.html")
    

def signup_view(request):
    form = UserCreationForm()
    context = {"form": form}

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, "rexsite/signup.html", context)

def logout_view(request):
    logout(request)
    return render(request, "rexsite/login.html", {
        "message": "Bye for now!"
    })

def reserve(request):
    if request.method == "POST":
        court = Courts.objects.get(courtname = request.POST["court"])        
        reservation = Reservation.objects.filter(court = court.id).values()
        start_time = datetime.strptime(request.POST["starttime"], '%H:%M')
        end_time = datetime.strptime(request.POST["endtime"], '%H:%M')
        for x in range(len(reservation)):
            if reservation[x]["starttime"].hour <= start_time.hour or reservation[x]["endtime"].hour >= end_time.hour:
                return render(request, "rexsite/index.html", {
                    "message": "This court is already booked, please try another court or another time."
                })
            elif request.POST["endtime"] >= (request.POST["starttime"].hour + 2):
                return render(request, "rexsite/index.html", {
                    "message": "Your Reservation either exceeds 2 hours or is invalid, please input a vaild reservation"
                })
            else:
                newrez = Reservation()
                newrez.court = int(request.POST["court"])
                newrez.starttime = request.POST["starttime"]
                newrez.endtime = request.POST["endtime"]
                newrez.save()
                return render(request, "rexsite/index.html", {
                    "message": "Your Reservation has been registered! Thanks for using Rec-Serve!"
                })




    