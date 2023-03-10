from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user_auth.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('user', 'book_name', 'book_author', 'book_price')
