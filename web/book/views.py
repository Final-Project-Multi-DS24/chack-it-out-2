from django.shortcuts import render,redirect
from .models import Book
from user.models import User,Reading,Wish
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
    # 위에 검색창 검색기능
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
    
    # 읽은 책 버튼 추가 기능
    elif "reading" in request.GET:
        reading=Reading(
            user = User.objects.get(id=int(request.session.get("user"))),
            book = Book.objects.get(book_isbn=pk)
        )
        reading.save()
        return redirect(f"/user/userpage/{request.session.get('user')}/reading")

    # 위시리스트 버튼 누르면 기능
    elif "wish" in request.GET:
        wish=Wish(
            user = User.objects.get(id=int(request.session.get("user"))),
            book = Book.objects.get(book_isbn=pk)
        )
        wish.save()
        return redirect(f"/user/userpage/{request.session.get('user')}/wish")
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
