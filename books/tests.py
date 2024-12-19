from django.test import TestCase
from django.urls import reverse
from books.models import Book
from authors.models import Author

class BooksApiTests(TestCase):
    def setUp(self):
        # author_instance = Author.objects.get().first()
        author = Author.objects.create(name="Author1")
        self.book = Book.objects.create(title="Test Book", available_copies=5, author=author, isbn=1234)

    def test_books_get(self):
        response = self.client.get(reverse('books_details'))
        self.assertEqual(response.status_code, 200)

    def test_books_post(self):
        response = self.client.post(reverse('books_details'), {
            "title": "New Book",
            "available_copies": 10
        })
        self.assertEqual(response.status_code, 201)  # Assuming successful creation


# single book (GET, PUT, DELETE)
class BooksDetailApiTests(TestCase):
    def setUp(self):
        author = Author.objects.create(name="Author1")
        self.book = Book.objects.create(title="Test Book", available_copies=5, author=author, isbn=1234)

    def test_books_get_by_id(self):
        response = self.client.get(reverse('book_details', args=[self.book.id]))
        self.assertEqual(response.status_code, 200)

    def test_books_put_by_id(self):
        response = self.client.put(reverse('book_details', args=[self.book.id]), {
            "title": "Updated Book",
            "available_copies": 7
        }, content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Book")

    def test_books_delete_by_id(self):
        response = self.client.delete(reverse('book_details', args=[self.book.id]))
        self.assertEqual(response.status_code, 204)  # Assuming successful deletion
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())
