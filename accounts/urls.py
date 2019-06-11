from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'), #회원가입
    path('survey1/<int:profile_id>', views.survey, name='survey'),
]