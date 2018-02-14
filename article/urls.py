from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^$', views.index),
    #url(r'^(\d+)/$', views.digital, name='digital'),
    url(r'^first/$', views.first),
    url(r'^$', views.home, name='home'),
    url(r'^(?P<id>\d+)/$', views.detail, name='detail'),
    # 匹配数字，并且给这个数字一个组名字就叫id,可以用group("id")这样的语法获取
    url(r'^archives/$', views.archives, name='archives'),
    url(r'^aboutme/$', views.about_me, name='about_me'),
    url(r'^tag(?P<tag>\w+)/$', views.search_tag, name='search_tag'),
    url(r'^search/$', views.blog_search, name='search'),
    url(r'^feed$', views.RSSFeed(), name='RSS'),

]