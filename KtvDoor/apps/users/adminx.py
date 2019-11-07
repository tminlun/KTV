# _*_ encoding:utf-8 _*_
__author__: '张剑峰'
__date__: '2019/11/4 0004 11:12'

import xadmin
from xadmin import views

from .models import Banner,AboutType,About, ContactUs


class BannerAdmin(object):
    list_display = ('title', 'index', 'url', 'image','is_banner', 'add_time')
    search_fields = ['title', 'image', 'index', 'is_banner','url']
    list_filter = ['title', 'image', 'index', 'url','is_banner', 'add_time']


class AboutTypeAdmin(object):
    list_display = ('name', 'add_time')


class AboutAdmin(object):
    list_display = ('name', 'about_type', 'describe', 'detail','add_time')
    search_fields = ['name', 'about_type', 'describe', 'detail','add_time']
    list_filter = ['name', 'about_type', 'describe', 'detail','add_time']


class ContactUsAdmin(object):
    list_display = ('name','address', 'phone', 'add_time')


xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(AboutType, AboutTypeAdmin)
xadmin.site.register(About, AboutAdmin)
xadmin.site.register(ContactUs, ContactUsAdmin)


# 配置
# 创建xadmin的最基本管理器配置，并与view绑定
class BaseSetting(object):
    # 开启主题功能
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    #修改左上角的title
    site_title = '张剑峰后台管理界面'
    #修改footer
    site_footer = '张剑峰的KTV门户网站'
    #收起菜单
    menu_style = 'accordion'


# 将基本配置管理与view绑定
xadmin.site.register(views.BaseAdminView,BaseSetting)
# 将title和footer信息进行注册
xadmin.site.register(views.CommAdminView, GlobalSettings)#views.(点)
