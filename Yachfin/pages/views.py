from django.shortcuts import render, redirect
from .models import Reservation

def index(request):
    if request.method == "POST":
        print(request.POST)
        name = request.POST.get("fullname")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        days = request.POST.getlist("day")   # multiple choice
        time = request.POST.get("time")
        notes = request.POST.get("notes")

        data=Reservation(
            names=name,
            emails=email,
            phones=phone,
            days=",".join(days),
            times=time,
            notes=notes,
        )
        data.save()

        return redirect("index")

    return render(request, "pages/index.html")

