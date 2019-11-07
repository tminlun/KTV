# _*_ encoding:utf-8 _*_
__author__: '张剑峰'
__date__: '2019/11/4 0004 11:27'

import xadmin

from .models import League, OrderInfo, OrderRoom


class LeagueAdmin(object):
    list_display = ('league_name', 'league_moblie', 'message', 'add_time')


class OrderInfoAdmin(object):
    list_display = ('user', 'order_mount', 'order_sn', 'mobile', 'pay_time')


class OrderRoomAdmin(object):
    list_display = ('private_room', 'room_package', 'order', 'add_time')


xadmin.site.register(League, LeagueAdmin)
xadmin.site.register(OrderInfo, OrderInfoAdmin)
xadmin.site.register(OrderRoom, OrderRoomAdmin)

