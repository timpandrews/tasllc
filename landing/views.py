from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    context = {
        "title": "TASLLC"
    }
    return render(request, "index.html", context)

def about(request):
    return HttpResponse("<h1>About</h1>")

def contact(request):
    return HttpResponse("<h1>Contact</h1>")
