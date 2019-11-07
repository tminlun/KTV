# _*_ encoding:utf-8 _*_
__author__: '张剑峰'
__date__: '2019/11/4 0004 13:42'

from django import forms
from captcha.fields import CaptchaField
from .models import UserProfile


class LoginForm(forms.Form):
    """登录表单"""
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=5)
    captcha = CaptchaField(error_messages={"invalid": "验证码输入错误"})

