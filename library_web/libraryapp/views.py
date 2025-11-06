from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Book, LibraryUser
from .forms import BookForm, LibraryUserForm

# Home page
def home(request):
    return render(request, 'home.html')

# List of books
def book_list(request):
    books = Book.objects.all()
    return render(request, "book_list.html", {"books": books})

# Add book
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Book added successfully!")
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, "add_book.html", {"form": form})

# Add user
def add_user(request):
    if request.method == "POST":
        form = LibraryUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User added successfully!")
            return redirect('home')
    else:
        form = LibraryUserForm()
    return render(request, "add_user.html", {"form": form})

# Borrow book
def borrow_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    users = LibraryUser.objects.all()

    if request.method == "POST":
        user_id = request.POST.get("user")
        user = LibraryUser.objects.get(id=user_id)
        success = book.borrow(user)
        if not success:
            messages.error(request, f"{user.name} cannot borrow more than 3 books.")
        return redirect('book_list')

    return render(request, "borrow_book.html", {"book": book, "users": users})

# Return book
def return_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    borrower_name = book.borrower.name if book.borrower else "User"
    fine = book.return_book()  # marks book as returned
    if fine > 0:
        messages.warning(request, f"Late return! {borrower_name} owes Rs.{fine}")
    return redirect('book_list')


# List users
def user_list(request):
    users = LibraryUser.objects.all()
    return render(request, "user_list.html", {"users": users})
