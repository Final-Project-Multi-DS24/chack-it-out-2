from django.shortcuts import render
from .models import Book
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.


def search(request):
    if "searchword" in request.GET:
        query = request.GET.get("searchword")
        selectbar = request.GET.get("selectbar")
        if selectbar:
            if selectbar == "1":
                books = Book.objects.all().filter(Q(book_title__icontains=query))
            elif selectbar == "2":
                books = Book.objects.all().filter(Q(book_author__icontains=query))
            elif selectbar == "3":
                books = Book.objects.all().filter(Q(book_isbn__icontains=query))
        return render(
            request,
            "Booksearch.html",
            {"query": query, "books": books, "selectbar": selectbar},
        )
    else:
        return render(request, "Booksearch.html")


def result(request, pk):
    if "searchword" in request.GET:
        query = request.GET.get("searchword")
        selectbar = request.GET.get("selectbar")
        if selectbar:
            if selectbar == "1":
                books = Book.objects.all().filter(Q(book_title__icontains=query))
            elif selectbar == "2":
                books = Book.objects.all().filter(Q(book_author__icontains=query))
            elif selectbar == "3":
                books = Book.objects.all().filter(Q(book_isbn__icontains=query))
        return render(
            request,
            "Booksearch.html",
            {"query": query, "books": books, "selectbar": selectbar},
        )
    
    else:
        book = Book.objects.get(book_isbn=pk)
        return render(request, "result.html", {"pk": pk, "book": book})


def result2(request, pk):
    if "searchword" in request.GET:
        query = request.GET.get("searchword")
        selectbar = request.GET.get("selectbar")
        if selectbar:
            if selectbar == "1":
                books = Book.objects.all().filter(Q(book_title__icontains=query))
            elif selectbar == "2":
                books = Book.objects.all().filter(Q(book_author__icontains=query))
            elif selectbar == "3":
                books = Book.objects.all().filter(Q(book_isbn__icontains=query))
        return render(
            request,
            "Booksearch.html",
            {"query": query, "books": books, "selectbar": selectbar},
        )
    
    else:
        book = Book.objects.get(book_isbn=pk)
        return render(request, "result2.html", {"pk": pk, "book": book})
