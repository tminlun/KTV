import datetime

from django.shortcuts import render,redirect,reverse
from django.views import View

from .models import RoomDate, PrivateRoom, PrivateRoomPackage
from operation.models import OrderInfo, OrderRoom
# Create your views here.


# 选择房间
class ReserveRoomView(View):
    def get(self, request):
        """
        展示日期和房型
        :param request:
        :return:
        """
        todate = datetime.datetime.now().date()
        room_dates = RoomDate.objects.filter(date__gte=todate)
        private_rooms = PrivateRoom.objects.all()

        # 根据日期筛选
        date_pk = int(request.GET.get("room_date_pk", 1))
        if date_pk:
            private_rooms = private_rooms.filter(room_date=date_pk)

        return render(request, 'reserve_room.html',{
            "room_dates": room_dates,  # 房型日期
            "private_rooms": private_rooms,  # 房型
            "date_pk": date_pk,  # 选中日期的pk
        })

    def post(self, request):
        """
        重定向成套页面并传递房型pk
        :param request:
        :return:
        """
        private_room_pk = int(request.POST.get("private_room_pk", 1))
        return redirect("http://127.0.0.1:8000/reserve_package/?from=%s" % private_room_pk)


# 选择套餐
class ReservePackageView(View):
    def get(self, request):
        """
        获取套餐
        :param request:
        :return:
        """

        # 动态获取房型
        private_room_pk = int(request.GET.get("from", 1))
        room_packages = PrivateRoomPackage.objects.filter(private_room=private_room_pk)  # 根据房型获套餐

        return render(request, 'reserve_package.html', {
                "room_packages": room_packages,  # 套餐
        })


