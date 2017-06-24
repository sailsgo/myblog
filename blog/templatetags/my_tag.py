#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ..models import *
from django import template
from django.db.models.aggregates import Count

register = template.Library()

@register.simple_tag
def getLasestArticle():
    return Article.objects.filter(status='1').order_by("-publishDate")[0:8]
@register.simple_tag
def getDailySentence():
    daily = DailySentence.objects.filter(status='1').order_by('-createTime')[0:1]
    print daily
    if daily:
        return daily[0]
    return {}
@register.simple_tag
def getTag():
    #co = Label.objects.annotate(count=Count('article')).filter(article__status='1').filter(count__gt=1).order_by("labelColor")
    co = Label.objects.annotate(count=Count('article')).filter(article__status='1').order_by("labelColor")
    return co
@register.simple_tag
def getCategory():
    return Category.objects.all()
@register.simple_tag
#获取最热文章
def get_hots():
    ar =  Article.objects.filter(status='1').order_by("-readCount")[0:1]
    if ar:
        return ar[0]
    return {}
