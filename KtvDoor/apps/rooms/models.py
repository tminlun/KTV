from datetime import datetime

from django.db import models

# Create your models here.


class RoomDate(models.Model):
    date = models.DateField(default=datetime.now, verbose_name="日期")

    class Meta:
        verbose_name = "包房日期"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.date.day)


class PrivateRoom(models.Model):
    name = models.CharField(max_length=30, verbose_name="包房名")
    number = models.CharField(max_length=15, verbose_name="人数")
    # 一个日期有多个房型
    room_date = models.ForeignKey(RoomDate, on_delete=models.CASCADE, verbose_name="包房日期")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "包房型"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class PrivateRoomPackage(models.Model):
    name = models.CharField(max_length=30, null=True,blank=True, verbose_name="名称")
    desc = models.CharField(max_length=50, null=True,blank=True, verbose_name="描述")
    price = models.FloatField(default=0, verbose_name="价格")
    # 一个房型有多个套餐
    private_room = models.ForeignKey(PrivateRoom, on_delete=models.CASCADE, verbose_name="房型")

    class Meta:
        verbose_name = "包房套餐"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
