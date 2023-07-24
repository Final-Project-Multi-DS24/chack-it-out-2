from django.shortcuts import render, redirect
from .models import Community, Member
from book.models import Book
from user.models import User


# Create your views here.
def community(request):
    # 로그인 정보가 있을 때
    if request.session.get("user"):
        user = User.objects.get(id=int(request.session.get("user")))
        name = user.user_name
        # 현재 진행중인 모임만 출력
        communities = Community.objects.all().filter(is_finished=False)
        endcommunities = Community.objects.all().filter(is_finished=True)
        return render(
            request, "community.html", {"user":user,"name":name,"communities": communities, "endcommunities":endcommunities}
        )
    else:
        communities = Community.objects.all()
        members = Member.objects.all()
        return render(
            request, "community.html", {"communities": communities, "members": members}
        )

# 새 모임 만들기
def newcommunity(request):
    if request.method == "GET":
        user = User.objects.get(id=int(request.session.get("user")))
        name = user.user_name        
        return render(request, "new.html",{"user":user,"name":name})
    elif request.method == "POST":
        get_book_isbn = request.POST["book"]
        meeting_date = request.POST["meeting_date"]
        meeting_place = request.POST["meeting_place"]
        creator = User.objects.get(id=request.session.get("user"))
        description = request.POST["description"]
        community = Community(
            book=Book.objects.get(book_isbn=get_book_isbn),
            meeting_date=meeting_date,
            meeting_place=meeting_place,
            description=description,
            creator=creator,
        )
        community.save()
        member = Member(
            community=Community.objects.latest("id"),
            user=User.objects.get(id=int(request.session.get("user"))),
        )
        member.save()

        return redirect("/community/")

# 상세 페이지
def detail(request,pk):
        user = User.objects.get(id=int(request.session.get("user")))
        community=Community.objects.get(id=pk)
        book=community.book
        members=Member.objects.all().filter(community_id=pk)
        # 모임 참여 신청
        if "join" in request.GET:
             print('OK')             
        return render(request, "detail.html",{"user":user,"pk": pk,'community':community, "book":book, "members":members})

