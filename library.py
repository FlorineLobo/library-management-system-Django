from django.db import models

class LibraryUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    available = models.BooleanField(default=True)

    borrower = models.ForeignKey(
        LibraryUser,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="borrowed_books"
    )

    def __str__(self):
        return self.title
