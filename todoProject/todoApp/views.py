from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello World!, you are at the todoApp index page.")

def about(request):
    return HttpResponse("This is the about page of todoApp")