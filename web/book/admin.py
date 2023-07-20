from django.contrib import admin
from .models import Book,Category


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ("book_isbn", "book_title", "book_author")


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "category")



# User 앱 관리자에서 보여주기
admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)
