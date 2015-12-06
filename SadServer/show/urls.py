from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^hello/$', 'show.views.hello'),
    url(r'^index/$', 'show.views.index'),
    url(r'^login/$', 'show.views.login'),
    url(r'^register/$', 'show.views.register'),
    url(r'^hospitals/$', 'show.views.hospitals'),
    url(r'^contact/$', 'show.views.contact'),
    url(r'^list/$', 'show.views.list'),
]
