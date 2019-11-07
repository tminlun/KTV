from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect,reverse

from .forms import LoginForm
from .models import Banner, AboutType, About, ContactUs

# Create your views here.


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        return render(request, 'login.html',{
            "login_form": login_form,
        })

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # 获取值
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('index'))
            else:
                return render(request, 'login.html',{
                    'login_form': login_form,
                    'msg': '账号或者密码错误',
                })
        else:
            return render(request, 'login.html', {
                "login_form": login_form,  # 错误
            })


class LogoutView(View):
    """注销"""
    def get(self,request):
        logout(request)
        return redirect(request.GET.get('from', reverse('index')))


# 首页
class IndexView(View):
    def get(self, request):
        banners = Banner.objects.all().order_by("?")[:8]
        about = About.objects.first()
        return render(request, 'index.html', {
            "banners": banners,
            "about": about,
        })


# 关于我们
class AboutView(View):
    def get(self, request):
        try:
            about_types = AboutType.objects.all()
            about = About.objects.all()[0]
        except Exception:
            return render(request, 'about.html')

        # 根据类别筛选
        about_type_pk = int(request.GET.get("about_type_pk", 1))
        if about_type_pk > 0:
            about = About.objects.get(about_type=about_type_pk)

        return render(request, 'about.html',{
            "about_types": about_types,
            "about_type_pk": about_type_pk,
            "about": about,

        })


# 联系我们
class ContactUsView(View):
    def get(self, request):
        contacts = ContactUs.objects.all()

        return render(request, 'contact_us.html',{
            "contacts": contacts,
        })

