#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ------------------------------------------------------------
# Filename:    adminx.py
# CreateDate:  2017/5/7
# Author:      mingjianyong
# Description:      adminx定制类

import xadmin
import xadmin.views as xviews
#引入自己的模块
from .models import Author, Category, Article, Label, AccessRecord, DailySentence
from xadmin.layout import Main, TabHolder, Tab, Fieldset, Row, Col, AppendedText, Side
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True
xadmin.site.register(xviews.BaseAdminView, BaseSetting)
class AdminSettings(object):
    site_title = "coding的博客后台管理"
    # 菜单设置
    def get_site_menu(self):
         return (
            {'title': '文章管理', 'perm': self.get_model_perm(Category, 'change'), 'menus':(
                {'title': '文章内容管理', 'url': self.get_model_url(Article,'changelist')},
                {'title': '类别管理', 'url': self.get_model_url(Category,'changelist')},
                {'title': '标签管理', 'url': self.get_model_url(Label,'changelist')},
            )},
            {'title': '每日一句', 'icon': 'info-sign', 'url': self.get_model_url(DailySentence,'changelist')},
            {'title': '访问者', 'icon': 'info-sign', 'url': self.get_model_url(AccessRecord,'changelist')},
        )
class ArticleAdmin(object):
    list_filter = ('title', 'publishDate', 'author','category','readCount','label','status')
    list_display = ('title', 'publishDate', 'author','category','readCount','label','status')
    list_editable = ['title','publishDate', 'category','label','status']
class CategoryAdmin(object):
    list_editable = ['cateName']
class LabelAdmin(object):
    list_editable = ['labelName']
class DailySentenceAdmin(object):
    list_display = ('title', 'createTime','status')
    list_editable = ['title','createTime','status']

xadmin.site.register(xviews.CommAdminView, AdminSettings)
xadmin.site.register(Article,ArticleAdmin)
xadmin.site.register(Category,CategoryAdmin)
xadmin.site.register(Label,LabelAdmin)
xadmin.site.register(AccessRecord)
xadmin.site.register(DailySentence,DailySentenceAdmin)

