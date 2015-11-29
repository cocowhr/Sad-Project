from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^register/$', 'api.views.register'),
    url(r'^login/$', 'api.views.login'),
    url(r'^searchhospname/$', 'api.views.searchhospname'),
    url(r'^searchdepartment/$', 'api.views.searchdepartment'),
    url(r'^orders/(?P<hospitalid>\d+)/$','api.views.searchdepartment'''),
    #Android
    url(r'^loginandroid/$', 'api.views.loginandroid'),
    url(r'^loginandroid/$', 'django.contrib.auth.views.login'),
    url(r'^registerandroid/$', 'api.views.register_page'),
]
