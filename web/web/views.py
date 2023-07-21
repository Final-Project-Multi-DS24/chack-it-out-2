# HttpResponse(" ") - String을 출력하는 패키지.
from django.http import HttpResponse

# render(request, '___.html') - request요청대로, ___.html을 반환하는 패키지
from django.shortcuts import render
from user.models import User
from book.models import Book
import random


def home(request):
    allbook = Book.objects.all()
    randombook_1 = random.choice(allbook)
    randombook_2 = random.choice(allbook)
    randombook_3 = random.choice(allbook)
    randombook_4 = random.choice(allbook)
    randombook_5 = random.choice(allbook)
    randombook_6 = random.choice(allbook)
    randombook_7 = random.choice(allbook)
    randombook_8 = random.choice(allbook)
    randomresult = [
        randombook_1,
        randombook_2,
        randombook_3,
        randombook_4,
        randombook_5,
        randombook_6,
        randombook_7,
        randombook_8,
    ]
    # 로그인정보가 있을때
    try:
        user = User.objects.get(id=int(request.session.get("user")))
        name = user.user_name
        # 책 객체를 랜덤으로하나 보여주겠다.
    # 그 외에는 그냥 메인페이지 접속
    except TypeError:
        return render(request, "main.html", {"randomresult": randomresult})
    return render(
        request,
        "main.html",
        {
            "user": user,
            "name": name,
            "randomresult": randomresult,
        },
    )


def search(request, pk):
    user = User.objects.get(id=pk)
    return render(request, "search.html", {"pk": pk, "user": user})


def search_book(request, pk):
    user = User.objects.get(id=pk)
    return render(request, "search_book.html", {"pk": pk, "user": user})
