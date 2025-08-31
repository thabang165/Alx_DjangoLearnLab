from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # show these columns in the list
    search_fields = ('title', 'author')  # enable search by title or author
    list_filter = ('publication_year',)  # filter by publication year
