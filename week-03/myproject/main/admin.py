from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('entry_number', 'title', 'author', 'publish_year', 'isbn')
    search_fields = ('title', 'author', 'isbn')
