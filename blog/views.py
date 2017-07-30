#coding:utf-8
from django.shortcuts import render
from django.shortcuts import HttpResponse
from blog.models import *
import urllib
import json
from urllib import urlencode
import time

import datetime
# Create your views here.
#文章主页
def index(request,currPage=1):
    #获取文章信息
    currPage=int(currPage)
    #sumPage = request.GET('count') 
    pageSize=6
    articleCount = Article.objects.filter(status='1').count()
    pageCount = articleCount/pageSize if articleCount%pageSize==0 else articleCount/pageSize+1
    if currPage>pageCount and pageCount!=0:
        currPage=pageCount
    index = (currPage-1)*pageSize
    left= index+pageSize
    articles = Article.objects.filter(status='1')[index:left]
    print articles
    #获取天气信息
    weather = getWeather(request)
    return render(request,'index.html',{'Articles':articles,'Weather':weather,'pageCount':pageCount,'currPage':currPage})
def article_content(request,aid):
    #获取文章信息
    article = Article.objects.filter(id=aid)
    articleDict={}
    if article:
        articleDict=article[0]
    article_list = Article.objects.values_list('id', flat=True).order_by('id')
    print article_list
    article_list = list(article_list)
    preDict = dict()
    nextDict = dict()
    if article_list:
        id_index = article_list.index(long(aid))  # 当前id的索引
        pre = next = 0
        if len(article_list)>1:
            if id_index != 0 and id_index !=len(article_list)-1:      # 如果不是第一篇或最后一篇
                pre = article_list[id_index-1]
                next = article_list[id_index+1]
            else:
                if id_index == 0:       # 第一篇
                    next = article_list[id_index+1]
                if id_index == len(article_list)-1:    # 最后一篇
                    pre = article_list[id_index-1]
        elif len(article_list) == 1:
            pre, next = 0, 0
        if pre !=0:
            preDict =  Article.objects.filter(id=pre)[0]
        if next !=0:
            nextDict = Article.objects.filter(id=next)[0]
    print preDict,nextDict
    return render(request,'content.html',{'Article':articleDict,"pre":preDict,"next":nextDict})
def cate(request,cateName):
    Articles = Article.objects.filter(category__cateName__icontains='%s'%cateName)
    weather = getWeather(request)
    return render(request,'index.html',{'Articles':Articles,'Weather':weather})
def test(request):
    return render(request,'index1.html')

def getWeather(request):
    ##获取天气信息
    ip=""
    if request.META.has_key('HTTP_X_FORWARDED_FOR'):  
        ip =  request.META['HTTP_X_FORWARDED_FOR']  
    else:  
        ip = request.META['REMOTE_ADDR']
    url = 'http://api.k780.com:88'
    if ip!="":
        params = {
          'app' : 'weather.today',
          'weaid' : ip,
          'appkey' : '24200',
          'sign' : '57729e5943500b472331ed73b3e98bc6',
          'format' : 'json',
        }
    params = urlencode(params)
    f = urllib.urlopen('%s?%s' % (url, params))
    response = f.read()
    re = json.loads(response)
    weather=dict()
    if re['success']=='1':
        weather['location']=re['result']['citynm']
        weather['temperature_curr']=re['result']['temperature_curr']
        temp=weather['temperature_curr']
        weather['temperature_curr']=temp[0:len(temp)-1]
        weather['week']=re['result']['week']
        weather['day']=re['result']['days']
        weather['weather']=re['result']['weather']
        weather['tag']=getWeatherTag(re['result']['weatid'])
    return weather
def getWeatherTag(tag):
    snow=['7','14','15','16','17','18','27','28','29']
    wind=['3','19','30','31','32','33','21']
    rain=['4','8','9','10','11','12','20','22','23']
    thunder=['13','5','6','24','25','26']
    sun=['1','2']
    if tag in snow:
        return 'snow'
    elif tag in wind:
        return 'wind'
    elif tag in rain:
        return 'rain'
    elif tag in thunder:
        return 'thunder'
    else:
        return 'sun'

def like(request):
    print "like"
    ips=""
    if request.META.has_key('HTTP_X_FORWARDED_FOR'):
        ips =  request.META['HTTP_X_FORWARDED_FOR']
    else:
        ips = request.META['REMOTE_ADDR']
    curr = datetime.datetime.now()
    print datetime.date(curr.year,curr.month,curr.day)
    re = AccessRecord.objects.filter(ip=ips,accessTime__startswith=datetime.date(curr.year,curr.month,curr.day))

    if re:
        p = re[0]
        p.accessCount = p.accessCount+1
        p.save()
    else:
        td=curr.strftime("%Y-%m-%d %H:%I:%S")
        p = AccessRecord(ip=ips,accessTime=td)
        p.save()
    """
    re.accessCount = re.accessCount
    if re：
       re.save
    ar = AccessRecord(ip=ip,accessCount=re[0])
    """
    return render(request,'deng.html')
def getToken(request):
    from qiniu import auth
    au = auth.Auth("eo8KrWCHq3gJe53OhK1Zv33iHF_FVYDe6TymSCyZ","LhJAkfoEJcbd7-m7m5lMliTO1gg7aCFIA5eTmBmg")
    token =  au.upload_token("images")
    return HttpResponse(token)
