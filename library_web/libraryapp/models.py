from django.db import models
from django.utils import timezone
from datetime import timedelta

class LibraryUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def borrowed_count(self):
        # Count only currently borrowed books
        return Book.objects.filter(borrower=self, available=False).count()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    available = models.BooleanField(default=True)
    borrower = models.ForeignKey(LibraryUser, null=True, blank=True, on_delete=models.SET_NULL)
    borrowed_on = models.DateTimeField(null=True, blank=True)

    def borrow(self, user):
        """
        Borrow this book by a user.
        Returns True if successful, False if user cannot borrow more than 3 books or book is unavailable.
        """
        if user.borrowed_count() >= 3:
            return False  # User cannot borrow more than 3 books
        if self.available:
            self.borrower = user
            self.available = False
            self.borrowed_on = timezone.now()
            self.save()
            return True
        return False

    def return_book(self):
        """
        Return this book.
        Calculates fine if overdue and resets borrower.
        """
        fine = self.calculate_fine()
        self.borrower = None
        self.available = True
        self.borrowed_on = None
        self.save()
        return fine

    @property
    def due_date(self):
        """
        Returns the due date for the book (7 days after borrowed_on).
        """
        if self.borrowed_on:
            return self.borrowed_on + timedelta(days=7)
        return None

    @property
    def is_overdue(self):
        """
        Returns True if the book is overdue, False otherwise.
        """
        if self.borrowed_on:
            return timezone.now() > self.due_date
        return False

    def calculate_fine(self):
        """
        Calculates the fine for overdue books: Rs.10 per day after 7 days.
        """
        if self.borrowed_on:
            overdue_days = (timezone.now() - self.due_date).days
            if overdue_days > 0:
                return overdue_days * 10
        return 0

    def __str__(self):
        return self.title
