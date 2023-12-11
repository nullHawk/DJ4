from django.shortcuts import render
from django.urls import path
from polls import views

# Create your views here.
def index(request):
    sites = {
        "polls/owner": "Owner",
        "polls": "A Polls Application",
        "hello": "Test the session",
        "autos":"Autos CRUD",
        "cats":"Cats CRUD",
    }
    data = {'sites' : sites}
    return render(request, 'home/index.html',data)

