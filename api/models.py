from django.db import models

class Author(models.Model):
    """
    The Author model represents a writer who can have multiple books.
    Fields:
        name (str): The name of the author.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    The Book model represents a literary work written by an Author.
    Fields:
        title (str): The title of the book.
        publication_year (int): The year the book was published.
        author (FK): A foreign key linking the book to its author.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author, related_name="books", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"

