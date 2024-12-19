from django.db import models
from books.models import Book

# Create your models here.
class BorrowRecord(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed_by = models.CharField(max_length=255)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.borrowed_by} borrowed {self.book.title}"

