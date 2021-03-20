from django.contrib import admin

from core.models import Book, Journal


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description', 'created_at', 'num_pages', 'genre']
    ordering = ['name']
    search_fields = ['name', 'genre', ]
    list_filter = ['created_at', 'num_pages', ]

@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description', 'created_at', 'type', 'publisher']
    ordering = ['name']
    search_fields = ['name', ]
    list_filter = ['created_at', ]