# Delete Operation

```python
from bookshelf.models import Book

# Retrieve the book
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Check all books to confirm deletion
Book.objects.all()
# Expected output: <QuerySet []>
