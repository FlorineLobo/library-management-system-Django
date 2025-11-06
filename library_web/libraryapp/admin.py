from django.contrib import admin
from .models import Book, LibraryUser

admin.site.register(Book)
admin.site.register(LibraryUser)
