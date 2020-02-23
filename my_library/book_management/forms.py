from django import forms
from .models import Book, Author

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["name", "surname", "email"]

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["isbn", "title", "author", "publisher", "price"]
