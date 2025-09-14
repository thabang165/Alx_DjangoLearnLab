# Update Operation

```python
from bookshelf.models import Book

# Update the title
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book.title
```

**Expected Output:**
```
'Nineteen Eighty-Four'
```
