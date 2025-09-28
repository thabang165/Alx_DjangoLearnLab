from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User

from .models import Author, Book

class BookAPITestCase(APITestCase):
    """
    Test suite for Book API endpoints.
    Covers CRUD, permissions, filtering, searching, and ordering.
    """

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='password123')
        
        # Create a test author
        self.author = Author.objects.create(name='J.K. Rowling')
        
        # Create some test books
        self.book1 = Book.objects.create(title='Harry Potter 1', publication_year=2000, author=self.author)
        self.book2 = Book.objects.create(title='Harry Potter 2', publication_year=2002, author=self.author)

        # API client
        self.client = APIClient()

    # ----------------------------
    # Test List Endpoint
    # ----------------------------
    def test_book_list(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    # ----------------------------
    # Test Retrieve Endpoint
    # ----------------------------
    def test_book_detail(self):
        url = reverse('book-detail', kwargs={'pk': self.book1.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Harry Potter 1')

    # ----------------------------
    # Test Create Endpoint (Unauthenticated)
    # ----------------------------
    def test_create_book_unauthenticated(self):
        url = reverse('book-create')
        data = {'title': 'New Book', 'publication_year': 2025, 'author': self.author.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # ----------------------------
    # Test Create Endpoint (Authenticated)
    # ----------------------------
    def test_create_book_authenticated(self):
        self.client.login(username='testuser', password='password123')
        url = reverse('book-create')
        data = {'title': 'New Book', 'publication_year': 2025, 'author': self.author.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    # ----------------------------
    # Test Update Endpoint
    # ----------------------------
    def test_update_book(self):
        self.client.login(username='testuser', password='password123')
        url = reverse('book-update', kwargs={'pk': self.book1.pk})
        data = {'title': 'Harry Potter Updated', 'publication_year': 2001, 'author': self.author.id}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Harry Potter Updated')

    # ----------------------------
    # Test Delete Endpoint
    # ----------------------------
    def test_delete_book(self):
        self.client.login(username='testuser', password='password123')
        url = reverse('book-delete', kwargs={'pk': self.book1.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # ----------------------------
    # Test Filtering
    # ----------------------------
    def test_filter_books_by_year(self):
        url = reverse('book-list') + '?publication_year=2002'
        response = self.client.get(url)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Harry Potter 2')

    # ----------------------------
    # Test Searching
    # ----------------------------
    def test_search_books_by_title(self):
        url = reverse('book-list') + '?search=Harry Potter 1'
        response = self.client.get(url)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Harry Potter 1')

    # ----------------------------
    # Test Ordering
    # ----------------------------
    def test_order_books_by_publication_year(self):
        url = reverse('book-list') + '?ordering=-publication_year'
        response = self.client.get(url)
        self.assertEqual(response.data[0]['publication_year'], 2002)
