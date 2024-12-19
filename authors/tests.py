from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Author

# Test for the list of authors (GET, POST)
class AuthorsApiTests(APITestCase):
    def setUp(self):
        # Creating an initial author instance for the tests
        self.author = Author.objects.create(name="Author1")

    def test_authors_get(self):
        """Test GET request for the list of authors"""
        url = reverse('authors_details')  # Path for listing all authors
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_authors_post(self):
        """Test POST request to create a new author"""
        url = reverse('authors_details')  # Path for creating a new author
        data = {
            "name": "Author2"
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, 201)  # Check if the author was created
        self.assertEqual(Author.objects.count(), 2)  # Check if a new author is created
        self.assertEqual(Author.objects.last().name, "Author2")  # Verify the author's name

# Test for individual author (GET, PUT, DELETE)
class AuthorDetailApiTests(APITestCase):
    def setUp(self):
        # Creating an initial author instance for the tests
        self.author = Author.objects.create(name="Author1")

    def test_author_get_by_id(self):
        """Test GET request for a specific author by ID"""
        url = reverse('author_details', args=[self.author.id])  # Path for getting a specific author by ID
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], self.author.name)  # Verify the returned data matches the created author

    def test_author_put_by_id(self):
        """Test PUT request to update a specific author by ID"""
        url = reverse('author_details', args=[self.author.id])  # Path for updating the author by ID
        data = {
            "name": "Updated Author"
        }
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, 200)
        
        # Verify the author is updated in the database
        self.author.refresh_from_db()
        self.assertEqual(self.author.name, "Updated Author")

    def test_author_delete_by_id(self):
        """Test DELETE request to delete a specific author by ID"""
        url = reverse('author_details', args=[self.author.id])  # Path for deleting an author by ID
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)  # Check if the author was deleted
        self.assertFalse(Author.objects.filter(id=self.author.id).exists())  # Verify the author no longer exists in the database
