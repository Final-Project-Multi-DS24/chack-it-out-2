from django.shortcuts import render, redirect
from .models import Community, Member
from book.models import Book
from user.models import User


# Create your views here.
def community(request):
    communities = Community.objects.all()
    members = Member.objects.all()
    return render(
        request, "community.html", {"communities": communities, "members": members}
    )


def newcommunity(request):
    if request.method == "GET":
        return render(request, "new.html")
    elif request.method == "POST":
        book = 9791195463817
        meeting_date = request.POST["meeting_date"]
        meeting_place = request.POST["meeting_place"]
        description = request.POST["description"]
        community = Community(
            book=Book.objects.get(book_isbn=book),
            meeting_date=meeting_date,
            meeting_place=meeting_place,
            description=description,
        )
        community.save()
        member = Member(
            Communityid=Community.objects.latest("id"),
            user_pk=User.objects.get(id=int(request.session.get("user"))),
            is_leader=True,
        )
        member.save()

        return redirect("/community/")
