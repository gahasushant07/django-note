from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homepage(request):
    return HttpResponse("<h1>Welcome to my Personal Website</h1>")

def aboutpage(request):
    return HttpResponse("<h1>About Page</h1>")

def projectpage(request):
    return HttpResponse("<h1> Project Page</h1>")

def service(request):
    return HttpResponse("<h1> Service Page</h1>")

def contact(request):
    return HttpResponse("<h1> Contact Page</h1>")

def news(request):
    return HttpResponse("<h1> News Post")