from django.shortcuts import render, redirect
# 회원가입 암호화,회원가입 확인
from django.contrib.auth.hashers import make_password, check_password
# POST로 받을 DB 모델 
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
        user_id=request.POST['user_id']
        user_name=request.POST['user_name']
        password=request.POST['password']
        user_birth=request.POST['user_birth']
        phonenumber=request.POST['phonenumber']
        profile_image=request.POST['profile_image']
        # interest = request.POST['interest']

        # 그리고 변수를 User모델 객체에 담습니다.
        user = User(user_id=user_id, 
                    user_name=user_name, 
                    user_birth=user_birth, 
                    password=make_password(password),
                    phonenumber=phonenumber,
                    profile_image=profile_image
                    )
        user.save()
        return render(request, 'register.html')
    

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
    return render(request, 'modify.html')

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
    return render(request, 'usercommunity.html')


# 회원정보 삭제 
def delete(request):
    user = User.objects.get(id=int(request.session.get('user')))
    user.delete()
    del(request.session['user'])
    return render(request, 'main.html')
    