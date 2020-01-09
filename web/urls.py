#coding=utf8

from django.conf.urls import url
from web.views import *

urlpatterns = (url(r'^create_code/$',create_code_img),  # 生成验证码
               url(r'^$', home),
               url(r'^register/$', register),  # 注册
               url(r'^login/$', login),  # 登录
               url(r'^logout/$', logout),  # 登出
               url(r'^about/$', about),  # 关于
               url(r'^comm/email/$',verifi_email),  # 验证邮箱
               url(r'^me/del/email/$',del_email),  # 邮箱解绑
               url(r'^comm/forgetpasswd/$',find_passwd),  # 忘记密码
               url(r'^comm/passwd/$',reset_passwd),  # 点击邮件链接重置密码
               )