# _*_ encoding:utf-8 _*_
__author__: '张剑峰'
__date__: '2019/11/4 0004 14:02'

import xadmin

from .models import RoomDate, PrivateRoom, PrivateRoomPackage


class RoomDateAdmin(object):
    list_display = ('date',)


class PrivateRoomAdmin(object):
    list_display = ('name','number','room_date','add_time')


class PrivateRoomPackageAdmin(object):
    list_display = ('name','desc','price','private_room')


xadmin.site.register(RoomDate, RoomDateAdmin)
xadmin.site.register(PrivateRoom, PrivateRoomAdmin)
xadmin.site.register(PrivateRoomPackage, PrivateRoomPackageAdmin)
