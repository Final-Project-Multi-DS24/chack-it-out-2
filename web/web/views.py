# HttpResponse(" ") - String을 출력하는 패키지.
from django.http import HttpResponse
# render(request, '___.html') - request요청대로, ___.html을 반환하는 패키지
from django.shortcuts import render
from user.models import User

def home(request):
    # 로그인정보가 있을때
    try:
        user = User.objects.get(id=int(request.session.get('user')))
        name = user.user_name
        image=user.profile_image
    # 그 외에는 그냥 메인페이지 접속
    except TypeError:
        return render(request, 'main.html')
    return render(request, 'main.html', {'user':request.session.get('user'),
                                         'name': name,
                                         'image': image} 
                                         )

def search(request):
    return render(request,'search.html')

def search_book(request):
    return render(request,'search_book.html')
