from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from datetime import datetime
from django.http import Http404
from django.contrib.syndication.views import Feed
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def index(request):
    return HttpResponse('hello chunjue ,is my django')

#def digital(request, ages): #获取地址中的数字作为参数
    #return HttpResponse("You are my %s guest." % ages)
    #post = Article.objects.all()[int(ages)] #因为是降序排列 所以第一个写的在后面 最后一个写的排在第一个 0
    #str = ('标题：%s\n标签：%s\n时间：%s\n文章：%s' % (post.atitle, post.alabel, post.adate_time, post.acontent))
    #return HttpResponse(str)

def first(request):
    context = {'current_time': datetime.now()}
    return render(request, 'article/first.html', context)

def home(request, pIndex=1):
    posts = Article.objects.all() #获取全部的文章对象
    paginator = Paginator(posts, 5) #每页显示5个文章对象
    #page = request.GET.get('page')
    #try:
        #post_list = paginator.page(page)
    #except PageNotAnInteger: #如果页面不是整数，则传递第一页
        #post_list = paginator.page(1) #第一页  显示第一页
    #except EmptyPage: #如果页面超出了范围 则提交最后一页
        #post_list = paginator.page(paginator.num_pages)
    pIndex = int(pIndex)
    post_list = paginator.page(pIndex)
    plist = paginator.page_range #总页数
    context = {'post_list': post_list, 'plist': plist, 'pIndex': pIndex}
    return render(request, 'article/home.html', context)

def detail(request, id): #每篇文章的id是唯一的
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist: #不存在的情况
        raise Http404
    context = {'post': post}
    return render(request, 'article/post.html', context)

def archives(request): #归档
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExist:
        raise Http404
    context = {'post_list': post_list, 'error': False}
    return render(request, 'article/archives.html', context)

def about_me(request): #关于我--个人简介
    return render(request, 'article/aboutme.html')

def search_tag(request, tag): #按标签分类
    try:
        post_list = Article.objects.filter(alabel=tag) #搜索标签为点击的标签的同标签文章
    except Article.DoesNotExist:
        raise Http404
    context = {'post_list': post_list}
    return render(request, 'article/tag.html', context)

def blog_search(request):
    if 's' in request.GET:
        s = request.GET['s'] #因为输入框的name为 s
        if not s: #当s不存在时 即搜索框内没有内容 转到首页
            return render(request, 'article/home.html')
        else:
            post_list = Article.objects.filter(atitle__icontains=s) #标题内包含输入内容 大小写不敏感
            if len(post_list) == 0:
                context = {'post_list': post_list, 'error': True} #表示没有找到的情况下 error为True
                return render(request, 'article/archives.html', context) #采用归档的网页
            else:
                context = {'post_list': post_list, 'error': False}  # 表示找到的情况下 error为False
                return render(request, 'article/archives.html', context)  # 采用归档的网页
    return redirect('/') # 如果 's' 不存在于GET报文中 重定向主页

class RSSFeed(Feed): #定义类 RSS功能
    title = "RSS feed - article"
    link = "feeds/posts/"
    description = "RSS feed - blog posts"

    def items(self):
        return Article.objects.order_by('-adate_time') #按时间倒序排 最近的排在最前面

    def item_title(self, item):
        return item.atitle

    def item_pubdate(self, item):
        return item.adate_time

    def item_description(self, item):
        return item.acontent