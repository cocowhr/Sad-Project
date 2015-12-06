from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^register/$', 'api.views.register'),
    url(r'^login/$', 'api.views.login'),
    url(r'^searchhospname/$', 'api.views.searchhospname'),
    url(r'^appoint/$', 'api.views.appoint'),
    url(r'^searchdepartment/(?P<hospitalid>\d+)/$','api.views.searchdepartment'''),
    url(r'^cancelappoint/(?P<appointid>\d+)/$','api.views.cancelappoint'''),
    url(r'^payappoint/(?P<appointid>\d+)/$','api.views.payappoint'''),
    url(r'^list/$', 'api.views.list'),
    #Android
    url(r'^loginandroid/$', 'api.views.loginandroid'),
    url(r'^loginandroid/$', 'django.contrib.auth.views.login'),
    url(r'^registerandroid/$', 'api.views.register_page'),
]
