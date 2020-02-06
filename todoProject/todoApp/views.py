from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    today = datetime.datetime.now().date()
    return render(request, 'index.html', {"today" : today})

def about(request):
    return render(request, 'about.html')