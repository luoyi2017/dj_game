#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin_login/$', views.admin_login, name='admin_login'),
    url(r'^admin_logout/$', views.admin_logout, name='admin_logout'),
    url(r'^filter_regtime/$', views.filter_regtime, name='filter_regtime'),
    url(r'^filter_player/', views.filter_player, name='filter_player'),
]