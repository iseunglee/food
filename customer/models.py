from django.db import models
from chinese.models import Food
# Create your models here.

# 어떤 음식을 얼마나 카트에 담았나?

# 테이블 생성 디폴트 이름은 : customer_cart 프로젝토이름_클래스명
class Cart(models.Model):
    food = models.ForeignKey(Food, on_delete=models.DO_NOTHING)
    amount = models.IntegerField(default=0)
