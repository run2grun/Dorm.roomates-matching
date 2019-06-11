from django.contrib import admin
from django.urls import path, include
import blog.views
import accounts.views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name='home'),
    path('blog/main', blog.views.main, name='main'),
    path('blog/mypage', blog.views.tomypage, name='tomypage'),
    path('blog/mypage/<int:profile_id>', blog.views.mypage, name="mypage"),
    path('blog/matching', blog.views.matching, name='matching'),
    path('blog/intro', blog.views.intro, name='intro'),
    path('blog/mail', blog.views.mail, name='mail'),
    path('blog/<int:blog_id>', blog.views.detail, name="detail"),
    path('blog/board', blog.views.board, name="board"),
    path('blog/matching/matching', blog.views.add_matching, name='add_matching'),
    path('blog/startmatching', blog.views.startmatching, name='startmatching'),
    path('blog/introgsg', blog.views.introgsg, name="introgsg"),
    path('blog/introssg', blog.views.introssg, name="introssg"),
    path('blog/introgrg', blog.views.introgrg, name="introgrg"),
    path('blog/introcsg', blog.views.introcsg, name="introcsg"),
    path('blog/introhtg', blog.views.introhtg, name="introhtg"),
    path('blog/introhdg', blog.views.introhdg, name="introhdg"),
    path('blog/introhmg', blog.views.introhmg, name="introhmg"),
    # 계정과 urls 연결
    path('accounts/', include('accounts.urls')),
    path('accounts/signup', blog.views.tosignup, name='tosignup'),
    path('accounts/survey', blog.views.tosurvey, name='tosurvey'),
    path('accounts/logout', accounts.views.logout, name='logout'),
    path('accounts/login', accounts.views.login, name='login'),
]
