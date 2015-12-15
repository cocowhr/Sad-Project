# -*- coding:utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin


# 一切以mobile开头的url pattern均指向安卓客户端专用view
urlpatterns = [
    url(r'^register/$', 'api.views.register'),
    url(r'^login/$', 'api.views.login'),
    url(r'^adminlogin/$', 'api.views.adminlogin'),
    url(r'^adminprelogin/$', 'api.views.adminprelogin'),
    url(r'^logout/$', 'api.views.logout'),
    url(r'^searchhospname/$', 'api.views.searchhospname'),
    url(r'^appoint/$', 'api.views.appoint'),
    url(r'^searchdepartment/(?P<hospitalid>\d+)/$', 'api.views.searchdepartment'''),
    url(r'^cancelappoint/(?P<appointid>\d+)/$', 'api.views.cancelappoint'''),
    url(r'^payappoint/(?P<appointid>\d+)/$', 'api.views.payappoint'''),
    url(r'^list/$', 'api.views.list'),
    url(r'^info/$', 'api.views.info'),
    url(r'^rejectuser/(?P<userid>\d+)/$', 'api.views.rejectuser'''),
    url(r'^admituser/$', 'api.views.admituser'),
    url(r'^getdept/$', 'api.views.getdept'),
    url(r'^getdoc/$', 'api.views.getdoc'),
    url(r'^setmax/$', 'api.views.setmax'),
    # Android
    # 以下url均以mobile/开头
    url(r'^mobile/login/$', 'api.views.mobile_login'),
    url(r'^mobile/login/$', 'django.contrib.auth.views.login'),
    url(r'^mobile/register/$', 'api.views.mobile_register'),
    # url(r'^logout/$', 'api.views.logout'),    # 暂时无法确定移动端的logout如何实现，可由客户端更改变量实现
    url(r'^mobile/searchhospname/$', 'api.views.mobile_searchhospname'),
    url(r'^mobile/searchdepartment/(?P<hospitalid>\d+)/$', 'api.views.mobile_searchdepartment'''),
    url(r'^mobile/list/$', 'api.views.mobile_list'),
    url(r'^mobile/cancelappoint/(?P<appointid>\d+)/$', 'api.views.mobile_cancelappoint'''),
    url(r'^mobile/payappoint/(?P<appointid>\d+)/$', 'api.views.mobile_payappoint'''),
    url(r'^mobile/appoint/$', 'api.views.mobile_appoint'),
    url(r'^mobile/info/$', 'api.views.mobile_info'),
    url(r'^mobile/getdept/$', 'api.views.mobile_getdept'),

]
