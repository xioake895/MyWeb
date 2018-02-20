#coding=utf-8
from django.shortcuts import HttpResponseRedirect,render_to_response
from article.models import Article
# Create your views here.
def login(request):
    #post方式
    if request.method=='POST':
        #获取表单数据
        username=request.POST.get('username',None)
        passwd=request.POST.get('title',None)
        #写入数据库
        new=Article(username=username,passwd=passwd)
        new.save()
        #跳转
        return HttpResponseRedirect('login/search')
    #get方式
    return render_to_response('login.html')

def search(request):
    if request.method=='POST':
        pass
        #启动爬虫
    return render_to_response('search.html')

def search_result(request):
    if request.method=='POST':
        pass
    return render_to_response('research_result.html')

def resume(request):
    return render_to_response('resume.html')