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
        communities = Community.objects.all()
        members = Member.objects.all()
        return render(
            request, "community.html", {"user":user,"name":name,"communities": communities, "members": members}
        )
    else:
        communities = Community.objects.all()
        members = Member.objects.all()
        return render(
            request, "community.html", {"communities": communities, "members": members}
        )

    
def newcommunity(request):
    if request.method == "GET":
        user = User.objects.get(id=int(request.session.get("user")))
        name = user.user_name        
        return render(request, "new.html",{"user":user,"name":name})
    elif request.method == "POST":
        book = 1
        meeting_date = request.POST["meeting_date"]
        meeting_place = request.POST["meeting_place"]
        creator = User.objects.get(id=request.session.get("user"))
        description = request.POST["description"]
        community = Community(
            book=Book.objects.get(id=book),
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
