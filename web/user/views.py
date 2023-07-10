from django.shortcuts import render, redirect
# 회원가입 암호화,회원가입 확인
from django.contrib.auth.hashers import make_password, check_password
# POST로 받을 DB 모델 
from .models import User

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
    


def login(request):
    # request to VIEW if "GET"(/link/), return templates to user
    if request.method == 'GET':
        return render(request, 'login.html')
    
    elif request.method == 'POST':
        # user_id를 저장하되 None값으로 (값이 덮어써지면 안되니까)
        user_id = request.POST.get('user_id', None)
        # 비밀번호 또한 동일
        password = request.POST.get('password', None)

        # objects.get : 객체를 반환한다 = user_id가 'user_id'인 User 모델의 객체를 반환한다.
        if not (user_id and password):
            pass
        # objects.get : 객체를 반환한다 = user_id가 'user_id'인 User 모델의 객체를 반환한다.
        else:
            user = User.objects.get(user_id=user_id)
            # password와 방금 반환한 객체의 password로 저장한 값이 True면?
            if check_password(password, user.password):
                request.session['user'] = user.id
				# home으로 redirect
                return redirect('/')
            else:
                print('비밀번호 오류')             
        return render(request, 'login.html')
    
