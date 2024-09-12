"""demo1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import re_path
from django.contrib import admin
from django.views.static import serve
from django.conf import settings
from apptest import views
urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    # 用户登录
    re_path(r'^login/',views.acc_login),
    # 展示预订信息
    re_path(r'^index/',views.index),
    # 极验滑动验证码 获取验证码的url
    re_path(r'^pc-geetest/register', views.get_geetest),
    # media相关的路由设置
    re_path(r'^media/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT}),
    # 处理预订请求
    re_path(r'^book/',views.book),
    # 首页
    re_path(r'^home/',views.home),
    # 注销
    re_path(r'^logout/',views.acc_logout),
    # 用户注册
    re_path(r'^reg/',views.reg),
    # 临时测试
    re_path(r'^test/',views.test),
    # 修改密码
    re_path(r'^change_password/',views.change_password),

    # about
    re_path(r'^about/',views.about),


]
