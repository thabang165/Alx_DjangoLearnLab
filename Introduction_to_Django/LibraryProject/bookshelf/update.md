# Update Operation

```python
from bookshelf.models import Book

# Retrieve the book we just created
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Check the updated title
book.title
# Expected output: 'Nineteen Eighty-Four'
