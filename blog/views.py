from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from accounts.models import Profile
from .models import Matching
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import auth

def home(request):
    return render(request, 'login.html')
# 메인페이지
def main(request):
    return render(request, 'blog/main.html')
# 내정보
def tomypage(request):
    profiles=Profile.objects
    return render(request, 'blog/mypage.html', {'profiles':profiles})
# 매칭
def matching(request):
    count=[]
    name=[]
    profile=[]
    pall = Profile.objects.filter(like_dorm = request.user.profile.like_dorm) # 객체 전부 묶음으로 가져오기
    profile_me = Profile.objects.get(user_name=request.user.username) #자신의 profile을 받아옴
    for profile_mate in pall.all():
        if(profile_mate != profile_me ):
            c=0 #for문으로 상대방 정보를 받아올 때마다 c만들어서 초기화
            if(profile_me.like_mate1 == profile_mate.like_info1):
                c+=25
            if(profile_me.like_mate2 == profile_mate.like_info2):
                c+=25
            if(profile_me.like_mate3 == profile_mate.like_info3):
                c+=25
            if(profile_me.like_mate4 == profile_mate.like_info4):
                c+=25
            count.append(c)
            name.append(profile_mate.user.username)
    add=zip(name, count)
    return render(request,'blog/matching.html',{'add':add, 'pall':pall})

# 기숙사소개
def intro(request):
    return render(request, 'blog/intro.html')

# 쪽지함
def mail(request):
    blogs = Blog.objects
    return render(request, 'blog/mail.html', {'blogs':blogs})

# 쪽지함내용보기
def detail(request, blog_id) : 
    blog_detail = get_object_or_404(Blog, pk= blog_id) # 특정 객체 가져오기(없으면 404 에러)
    return render(request, 'blog/detail.html', {'blog':blog_detail})

# 게시판
def board(request):
    return render(request, 'blog/board.html')

def tosignup(request):
    return render(request, 'signup.html')

# 개인성향페이지
def tosurvey(request):
    profiles=Profile.objects
    return render(request, 'survey.html', {'profiles':profiles})

def mypage(request, profile_id):
    if request.method == 'POST':
        profile = get_object_or_404(Profile, pk=profile_id)
        if(profile.user_pr != None):
            profile.user_pr= request.POST['user_pr']
        user = get_object_or_404(User, pk=profile.user.id)
        if(profile.user_pr != None):
            user.set_password(request.POST['user_pw'])
        user.save()
        profile.save()
        auth.login(request, user)
        return redirect('main')
    else:
        return render(request, 'mypage.html')
# ********************************
# ********************************
# ********************************
# ********************************
def add_matching(request):
    matching = Matching()
    matching.target1 = request.GET['target1']
    matching.target2 = request.GET['target2']
    matching.target_date = timezone.datetime.now()

    matching.save()
    return redirect('matching')

#기숙사
def introgsg(request):
    return render(request, 'blog/introgsg.html')

# 
def introssg(request):
    return render(request, 'blog/introssg.html')

def introgrg(request):
    return render(request, 'blog/introgrg.html')

def introcsg(request):
    return render(request, 'blog/introcsg.html')

def introhtg(request):
    return render(request, 'blog/introhtg.html')

def introhdg(request):
    return render(request, 'blog/introhdg.html')

def introhmg(request):
    return render(request, 'blog/introhmg.html')





def startmatching(request):

    # nameme는 로그인한 해당 유저를 지칭함 
    nameme = list(Matching.objects.filter(target1=request.user.username))
    # 로그인한 사람의 정보를 가져오기 위해서는 request를 이용해서 받아와야함
    # nameall은 전체 객체를 불러오는 역활
    nameall = list(Matching.objects.all())

    # 계산은 로그인한 유저의 가장 최근 객체를 먼저로 계산함
    namel = nameme[0]
    nameplus = namel.calltarget2() + namel.calltarget1()
    print(nameplus)

    for i in range(0, len(nameall)):
        nameall_part = nameall[i]
        nameall_partplus = nameall_part.calltarget1() + nameall_part.calltarget2()
        if nameall_partplus == nameplus:

            profiles = Profile.objects.get(user_name = nameall_part.calltarget1())
            print("matched!")
            return render(request, 'blog/complete.html', {'profiles':profiles})
            
        else:
            print("wait more time")
    return render(request, 'blog/wait.html')
    





    print("run this method")
    return redirect('/')