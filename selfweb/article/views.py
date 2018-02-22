#coding=utf-8
from django.shortcuts import HttpResponseRedirect,render_to_response
from article.models import Article
from scrapy import cmdline
import re
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
        return HttpResponseRedirect('/search')
    #get方式
    return render_to_response('login.html')

def search(request):
    if request.method=='POST':
        try:
            cmdline.execute("scrapy crawl Web".split())
        except:
            pass
        return HttpResponseRedirect('/search_result')
        
        #启动爬虫
    return render_to_response('search.html')

def search_result(request):
    contents=[]
    if request.method=='POST':
        pass
    with open(r'F:/project/selfweb/article/MyWebInfo.txt',encoding='utf-8') as f:
            lines=f.readlines()
    for line in lines:
        i=str(line).replace('*',' ')
        contents.append(i)
    return render_to_response('search_result.html',{'contents':contents})
    '''
    return render_to_response('search_result.html',{'contents':lines})
    '''
def resume(request):
    return render_to_response('resume.html')