from django import forms
from .models import Book, LibraryUser

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']  # Only include fields that exist

class LibraryUserForm(forms.ModelForm):
    class Meta:
        model = LibraryUser
        fields = ['name','email']
