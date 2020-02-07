from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    today = datetime.datetime.now().date()
    return render(request, 'index.html', {"today" : today})

def about(request):
    return render(request, 'about.html')

def contact(request):
    first_name = "Phakon"
    last_name = "Rujireksareekul"
    email = "58030205@kmitl.ac.th"
    return render(request, 'contact.html', {"first_name" : first_name, "last_name" : last_name, "email" : email })