from django.contrib import admin
from .models import Book


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ("book_isbn", "book_title", "book_author")


# User 앱 관리자에서 보여주기
admin.site.register(Book, BookAdmin)
