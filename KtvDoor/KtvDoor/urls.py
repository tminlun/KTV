"""KtvDoor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import xadmin
from django.urls import path,include,re_path
from django.conf import settings #上传图片
from django.conf.urls.static import static #上传图片

from users.views import IndexView, AboutView, ContactUsView, LoginView,LogoutView
from operation.views import OrderListView, OrderAjax, OrderDetailAjaxView, LeagueView
from rooms.views import ReserveRoomView, ReservePackageView

urlpatterns = [
    path('xadmin/', xadmin.site.urls, name="xadmin"),
    path('captcha/',include('captcha.urls')), #验证码
    path('ueditor/', include('DjangoUeditor.urls')), #富文本

    path('login/', LoginView.as_view(), name="login"),  # 登录
    path('logout/',LogoutView.as_view(),name="logout"), #注销

    path('', IndexView.as_view(), name="index"),  # 首页
    path('about/', AboutView.as_view(), name="about"),  # 关于我们
    path('contact_us/', ContactUsView.as_view(), name="contact_us"),  # 联系我们
    path('reserve_room/', ReserveRoomView.as_view(), name="reserve_room"),  # 选择房间
    path('reserve_package/', ReservePackageView.as_view(), name="reserve_package"),  # 选择套餐
    path('order_ajax/', OrderAjax.as_view(), name="order_ajax"),  # 添加订单
    path('order_list/', OrderListView.as_view(), name="order_list"),  # 订单列表
    path('order_detail/', OrderDetailAjaxView.as_view(), name="order_detail"),  # 订单详情
    path('league_ajax/', LeagueView.as_view(), name="league_ajax"),  #加盟

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
