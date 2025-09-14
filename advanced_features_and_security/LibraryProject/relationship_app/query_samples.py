# LibraryProject/relationship_app/query_samples.py

from relationship_app.models import Author, Book, Library, Librarian

# ---------- Sample Queries ----------

# 1️⃣ Query all books by a specific author
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        return [book.title for book in books]
    except Author.DoesNotExist:
        return []

# Example usage:
# print(books_by_author("J.K. Rowling"))


# 2️⃣ List all books in a library
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        return [book.title for book in books]
    except Library.DoesNotExist:
        return []

# Example usage:
# print(books_in_library("Central Library"))


# 3️⃣ Retrieve the librarian for a library
def librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        return librarian.name
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None

# Example usage:
# print(librarian_for_library("Central Library"))
