from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
def signup(request):
    #처음에 들어온 요청이 포스트 요청인지 확인
    if request.method == 'POST':
        
        #비밀번호 2개가 같은지 확인하기 
        if request.POST['password1'] == request.POST['password2']:
            try: #try 안에서 오류가 나지 않는 경우 계속실행
                user = User.objects.get(username = request.POST['username'])#db에 유저네임이 동일한 것이 있는지 확인하는것. 
                return render(request, 'signup.html', {'error' : '이미 사용하고 있는 이름입니다.'})
            except User.DoesNotExist: #try 안에서 User.DoesNotExist 에러가 났을 경우 실행
                user = User.objects.create_user(
                    request.POST['username'],
                    password=request.POST['password1'],
                )
                
                profile = Profile()
                profile.user_hp = request.POST['user_hp']
                profile.user_pr = request.POST['user_pr']
                profile.user_num = request.POST['user_num']
                profile.user_mw = request.POST['user_mw']
                profile.user_name = request.POST['user_name']
                profile.user = user
                profile.save()
                

                auth.login(request, user) #현재 상태를 로그인 상태로 바꿈, 이후 리다이렉트로 홈페이지로 이동시킴
                return redirect('main')
    else:
        return render(request, 'signup.html') #회원가입 페이지 보여주기

def login(request):
    if request.method=='POST': #POST 요청을 받은 경우
        username=request.POST['username']
        password= request.POST['password']
        #로그인에서 받은 정보를 가진 회원이 있는지 확인
        user=auth.authenticate(request, username=username, password=password)
        if user is not None: #User가 존재할 경우
            auth.login(request, user) #로그인 상태로 바꾸기
            return redirect('main')
        else:
            return render(request,'login.html',{'error' : '아이디나 비밀번호를 확인해주세요'})
    else:
        return render(request, 'login.html')

    return render(request, 'login.html')

def logout(request):
    auth.logout(request) #로그아웃 상태로 바꾸기
    return render(request, 'login.html')

#개인성향페이지 제출
def survey(request, profile_id):
    if request.method == 'POST':
        profile = get_object_or_404(Profile, pk=profile_id)
        profile.like_dorm = request.POST['like_dorm']
        profile.like_info1 = request.POST['like_info1']
        profile.like_info2 = request.POST['like_info2']
        profile.like_info3 = request.POST['like_info3']
        profile.like_mate1 = request.POST['like_mate1']
        profile.like_mate2 = request.POST['like_mate2']
        profile.like_mate3 = request.POST['like_mate3']
        profile.save()
        return redirect('matching')
    else:
        return render(request, 'survey.html')