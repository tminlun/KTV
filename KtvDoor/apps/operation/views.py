import time, re, random, string
from django.http import JsonResponse

from django.shortcuts import render,redirect,reverse
from django.views import View
from django.db.models import Q

from .models import OrderInfo, OrderRoom, League
from rooms.models import RoomDate, PrivateRoom, PrivateRoomPackage

# Create your views here.


# 订单列表
class OrderListView(View):
    def get(self, request):
        orders = OrderInfo.objects.all()

        keyboard = request.GET.get("keyboard", "")
        if keyboard:
            orders = orders.filter(Q(order_sn__icontains=keyboard) | Q(order_room__room_package__name__icontains=keyboard)
                                 | Q(order_room__room_package__price__icontains=keyboard)
                                 )

        return render(request, 'order_list.html', {
            "orders": orders,
        })

    def post(self, request):
        order_pk = request.POST.get('order_pk', 0)
        if order_pk == 0:
            return JsonResponse({'status': 500, 'msg': '删除失败'})

        try:
            OrderInfo.objects.get(pk=int(order_pk)).delete()
            return JsonResponse({'status': 200, 'msg': '删除成功'})
        except Exception:
            return JsonResponse({'status': 500, 'msg': '获取对象失败'})


# 订单详情
class OrderDetailAjaxView(View):
    def get(self, request):
        order_pk = int(request.GET.get("order_pk", 0))
        try:
            order_room = OrderRoom.objects.get(order=order_pk)
        except Exception:
            return JsonResponse({"status": 500, "msg": "获取对象失败"})

        data_dict = {
            "room_name": order_room.private_room.name
        }
        return JsonResponse(data_dict)




# 提交订单
class OrderAjax(View):
    def post(self, request):
        """
        提交订单
        :param request:
        :return:
        """

        # 获取号码和套餐
        mobile = request.POST.get("mobile", 0)
        room_package = int(request.POST.get("room_package", 0))

        if room_package == 0:
            return JsonResponse({"status": 500, "msg": "获取套餐失败"})

        try:
            package = PrivateRoomPackage.objects.get(pk=room_package)
        except Exception:
            return JsonResponse({"status": 500, "msg": "获取对象失败！"})

        # 自定义订单号（当前时间 + 随机字符串）
        # 当前时间
        old_time = time.strftime("%Y-%m-%d%H:%M:%S", time.localtime())
        current_time = str(re.sub(r'[-:]', '', old_time))
        # 随机字符串
        random_str = "".join([random.choice(string.digits + string.ascii_letters) for i in range(4)])
        order_sn = current_time + random_str
        try:
            # 实例化订单
            order_info = OrderInfo()
            order_info.user = request.user
            order_info.order_sn = order_sn
            order_info.order_mount = package.price
            order_info.mobile = mobile
            order_info.save()

            order_room = OrderRoom()
            order_room.private_room = package.private_room
            order_room.room_package = package
            order_room.order = order_info
            order_room.save()

            return JsonResponse({"status": 200, "msg": "创建成功！"})


        except Exception:
            return JsonResponse({"status": 500, "msg": "创建对象失败！"})


# 添加加盟
class LeagueView(View):
    def post(self,request):
        req = request.POST
        # 获取值
        message = req.get("message", "")
        moblie = req.get("moblie", "")
        name = req.get("name", "")

        if message == "" or moblie == "" or name == "":
            return JsonResponse({"status": 500, "msg": "输入不能为空"})


        try:
            league = League.objects.create()
            league.league_name = name
            league.league_moblie = moblie
            league.message = message
            league.save()
        except Exception:
            return JsonResponse({"status": 500, "msg": "创建失败！"})

        return JsonResponse({"status": 200, "msg": "创建成功！"})
