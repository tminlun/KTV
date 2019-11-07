from datetime import datetime

from django.db import models
from users.models import UserProfile as User

from rooms.models import PrivateRoomPackage,PrivateRoom

# Create your models here.


class League(models.Model):
    league_name = models.CharField(max_length=15, null=True, blank=True, verbose_name="加盟姓名")
    league_moblie = models.CharField(max_length=11, null=True, blank=True, verbose_name="加盟号码")
    message = models.TextField(max_length=200, null=True,blank=True, verbose_name="内容")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "招商加盟"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.league_name


class OrderInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True, verbose_name="用户")
    order_mount = models.FloatField("订单金额", default=0.0)
    order_sn = models.CharField("订单编号", max_length=30, null=True, blank=True, unique=True)
    mobile = models.CharField("联系电话",null=True,blank=True, max_length=11)
    pay_time = models.DateTimeField("支付时间", null=True, blank=True, default=datetime.now)

    class Meta:
        verbose_name = '订单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.order_sn


class OrderRoom(models.Model):
    private_room = models.ForeignKey(PrivateRoom,null=True,blank=True,  on_delete=models.CASCADE, verbose_name="包房")
    room_package = models.ForeignKey(PrivateRoomPackage, on_delete=models.CASCADE, verbose_name="包房套餐")
    order = models.ForeignKey(OrderInfo, on_delete=models.CASCADE, verbose_name="订单", related_name="order_room")
    add_time = models.DateTimeField("添加时间", default=datetime.now)

    class Meta:
        verbose_name = '订单的房型'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.private_room.name
