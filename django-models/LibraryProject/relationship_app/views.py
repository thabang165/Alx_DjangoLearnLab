
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView
from .models import Book, Library

# Function-Based View: List all books as plain text
def list_books(request):
    books = Book.objects.all()
    book_list = "\n".join([f"{book.title} by {book.author.name}" for book in books])
    return HttpResponse(book_list, content_type="text/plain")

# Class-Based View: Display details of a specific library with all its books
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

    # Optionally, you can override get_context_data if you want extra info
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = self.object.books.all()  # all books in this library
        return context

