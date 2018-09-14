#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.conf.urls import url

from blog import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^archive/$', views.archive, name='archive'),
    url(r'^about/$', views.about, name='about'),
    url(r'^article/(?P<pk>\d+)$', views.ArticleView.as_view(), name='detail'),
    url(r'^category/(?P<kw>\d+)$', views.OneCategoryView.as_view(), name='one_category'),
    url(r'^category$', views.CategoryView.as_view(), name='category'),
    url(r'^tags/(?P<tag>\d+)$', views.TagsView.as_view(), name='tags'),
]
