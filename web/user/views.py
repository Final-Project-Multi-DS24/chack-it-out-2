from django.shortcuts import render, redirect
# 회원가입 암호화,회원가입 확인
from django.contrib.auth.hashers import make_password, check_password
# POST로 받을 DB 모델 

# 회원가입오류
# 1. 아이디 또는 비밀번호 오류
from django.db import IntegrityError
# 2. 날짜 오류
from django.core.exceptions import ValidationError

from .models import User
# 로그인폼
from .forms import LoginForm

# Create your views here.

# request to VIEW if "GET"(/link/), return templates to user
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
# 사용자의 요청이 POST인 경우
    elif request.method == 'POST':
# 각 input tag에서 name 속성값을 이용해 사용자가 보낸 값을 꺼내옵니다.
        try:
            user_id=request.POST['user_id']
            user_name=request.POST['user_name']
            password=request.POST['password']
            profile_image=request.POST['profile_image']
            # interest = request.POST['interest']

            # 그리고 변수를 User모델 객체에 담습니다.
            user = User(user_id=user_id, 
                        user_name=user_name, 
                        password=make_password(password),
                        profile_image=profile_image
                        )
            user.save()
        except IntegrityError:
            error="이미 존재하는 아이디이거나 아이디가 공백입니다."
            return render(request, 'register.html', {"error":error})
        except ValidationError:
            pass
        # 가입 완료시 메인으로 이동
        return render(request, 'main.html')
    

# 로그인 기능
def login(request):
    if request.method == 'POST':
        # POST로 들어오는경우, loginForm에 받아준다.
        form = LoginForm(request.POST)
        # is_valid - post로 들어온 form을 둘다 적었다.
        if form.is_valid():
            # 유저 pk를 세션에 저장
            request.session['user'] = form.user_id
            return redirect('/')
    # POST방식이 아닌 경우
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout(request):
    # 현재 로그인한 사용자의 정보가 세션에 존재하면
    if request.session.get('user'):
        del(request.session['user']) # user 정보 삭제
    
    # 로그아웃 수행 후 홈 페이지로 이동
    return redirect("/")

def userpage(request):
    return render(request, 'userpage.html')

def modify(request):
    if request.method == 'GET':
        return render(request, 'modify.html')
    elif request.method == 'POST':
        return render(request, 'main.html')
def search(request):
    return render(request, 'usersearch.html')

def reading(request):
    if request.session.get('user'):
        user = User.objects.get(id=int(request.session.get('user')))
        name = user.user_name
    return render(request, 'reading.html',{'name': name})

def favorite(request):
    if request.session.get('user'):
        user = User.objects.get(id=int(request.session.get('user')))
        name = user.user_name
    return render(request, 'favorite.html',{'name': name})

def usercommunity(request):
    if request.session.get('user'):
        user = User.objects.get(id=int(request.session.get('user')))
        name = user.user_name
    return render(request, 'usercommunity.html',{'name': name})


# 회원정보 삭제 
def delete(request):
    user = User.objects.get(id=int(request.session.get('user')))
    user.delete()
    del(request.session['user'])
    return render(request, 'main.html')
    