import datetime
from .models import Book, Author
from .forms import BookForm, AuthorForm
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    today = datetime.datetime.now().date()
    return render(request, 'index.html', { "today": today })

def about(request):
    return render(request, 'about.html')

def book(request):
    all_book = Book.objects.all
    return render(request, 'book.html', {"all_book" : all_book})