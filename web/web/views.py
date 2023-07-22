# HttpResponse(" ") - String을 출력하는 패키지.
from django.http import HttpResponse

# render(request, '___.html') - request요청대로, ___.html을 반환하는 패키지
from django.shortcuts import render
from user.models import User
from book.models import Book
import random


def home(request):
    allbook = Book.objects.all()
    randomresult = []
    for i in range(8):
        randomresult.append(random.choice(allbook))
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


def search(request):
    user = User.objects.get(id=int(request.session.get("user")))
    name = user.user_name
    return render(request, "search.html", {"user": user,"name": name})


def search_book(request):
    user = User.objects.get(id=int(request.session.get("user")))
    name = user.user_name
    return render(request, "search.html", {"user": user,"name": name})
