from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


#아래와 같은 형태로 프로필 형태로 모델을 하나 더 만드는 것을 볼 수 있음. 
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_hp = models.IntegerField(default=0)
    user_pr = models.TextField(max_length=30, blank=True)
    user_num = models.IntegerField(default=0)
    user_mw = models.CharField(max_length=10, blank=True)
    user_name = models.TextField(max_length=10, blank=True)
    like_dorm = models.TextField(max_length=10, blank=True)
    like_info1 = models.IntegerField(default=0)
    like_info2 = models.IntegerField(default=0)
    like_info3 = models.IntegerField(default=0)
    like_info4 = models.IntegerField(default=0)
    like_mate1 = models.IntegerField(default=0)
    like_mate2 = models.IntegerField(default=0)
    like_mate3 = models.IntegerField(default=0)
    like_mate4 = models.IntegerField(default=0)

    def __str__(self):
        return self.user_name
#이 객체를 가르치는 말을 유저로 정하겠다