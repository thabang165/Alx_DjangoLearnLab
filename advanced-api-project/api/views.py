from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # read-only for unauthenticated users

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # only authenticated users can create

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # only authenticated users can update

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # only authenticated users can delete

from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    """
    GET /api/books/
    Retrieves a list of books with filtering, searching, and ordering.
    
    Features:
    - Filter by title, author, and publication_year using query params.
    - Search in title and author fields using ?search=keyword
    - Order results by title or publication_year using ?ordering=field
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Add DRF filtering, search, and ordering
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    
    # Fields available for filtering via ?field=value
    filterset_fields = ['title', 'author', 'publication_year']

    # Fields available for search via ?search=keyword
    search_fields = ['title', 'author__name']  # author__name for related Author model

    # Fields available for ordering via ?ordering=field
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering
