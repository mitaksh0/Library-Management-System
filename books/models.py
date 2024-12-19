from django.db import models
from authors.models import Author

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    isbn = models.CharField(unique=True, max_length=13)
    available_copies = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)