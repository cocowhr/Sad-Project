from django.conf.urls import include, url
from django.contrib import admin

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
    url(r'^loginandroid/$', 'api.views.loginandroid'),
    url(r'^loginandroid/$', 'django.contrib.auth.views.login'),
    url(r'^registerandroid/$', 'api.views.register_page'),
]
