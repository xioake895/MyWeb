#coding=utf-8
from django.shortcuts import HttpResponseRedirect,render_to_response
from article.models import Article
from scrapy import cmdline
import os
#from a import cmd
import re
# Create your views here.
def login(request):
    #post方式
    if request.method=='POST':
        '''
        #获取表单数据
        username=request.POST.get('username',None)
        passwd=request.POST.get('title',None)
        #写入数据库
        new=Article(username=username,passwd=passwd)
        new.save()
        '''
        #跳转
        return HttpResponseRedirect('/search')
    #get方式
    return render_to_response('login.html')

def search(request):
    if request.method=='POST':
        kw=request.POST.get('kw',None)
        with open('kw.txt','w') as e:
            e.write(kw)
        #os.chdir('F:/project/selfweb/article/')
        os.system('scrapy crawl Web')
        #os.chdir('F:/project/selfweb/')
        #os.system('python3 manage.py runserver')
        return HttpResponseRedirect('/search_result')
        
        #启动爬虫
    return render_to_response('search.html')

def search_result(request):
    
    #cmd()
    contents=[]
    if request.method=='POST':
        pass
    with open(r'F:/project/selfweb/MyWebInfo.txt',encoding='utf-8') as f:
            lines=f.readlines()
    for line in lines:
        i=str(line).replace('*',' ')
        contents.append(i)
    return render_to_response('search_result.html',{'contents':contents})

   #return render_to_response('search_result.html',{'contents':lines})

def resume(request):
    return render_to_response('resume.html')
