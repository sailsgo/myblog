#coding:utf-8
from django.db import models
import markdown
from django.utils.html import strip_tags


# Create your models here.
class Author(models.Model):
    id = models.AutoField(primary_key=True,verbose_name='作者ID')
    name = models.CharField(max_length=30,null=True)
    password = models.CharField(max_length=30,null=True)
    email = models.EmailField(max_length=30)
    realName = models.CharField(max_length=30,null=True)
    class Meta:
        verbose_name = '用户'
        verbose_name_plural = u'用户'
    def __unicode__(self):
        return self.realName
class Category(models.Model):
    id = models.AutoField(primary_key=True,verbose_name='类别ID')
    cateName = models.CharField(max_length=30,null=True,verbose_name='类别名称')

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = u'分类'
    def __unicode__(self):
        return self.cateName
class Label(models.Model):
    color_choices = (('1','Green'),('2','orange'),('3','blue'),('4','red'),('5','purple'),('6','yellow'))
    id = models.AutoField(primary_key=True,verbose_name='标签ID')
    labelName = models.CharField(max_length=30,null=True,verbose_name='标签名')
    labelColor = models.CharField(choices=color_choices,max_length = 3, null=True,verbose_name='边框色')
    class Meta:
        verbose_name = '标签'
        verbose_name_plural = u'标签'
    def __unicode__(self):
        return self.labelName
class Article(models.Model):
    status_choices = (('0','私密'),('1','公开'))
    id = models.AutoField(primary_key=True,verbose_name='文章ID') #文章ID
    title = models.CharField(max_length=100,verbose_name='文章标题')    #文章标题
    publishDate = models.DateField(null=True,verbose_name='发表日期')        #发表日期
    author = models.ForeignKey(Author,verbose_name='作者')      #作者，关联
    category = models.ForeignKey(Category,verbose_name='文章类别')      #分类，关联
    image = models.ImageField(upload_to='',max_length=100,verbose_name='简介图')    #图片
    readCount = models.IntegerField(verbose_name='阅读次数',null=True,blank=True,default=1)    #浏览次数
    content = models.TextField(verbose_name='文章内容')   #文章内容
    label = models.ManyToManyField(Label,verbose_name='文章标签')
    intro = models.CharField(max_length=100,verbose_name='文章简介',blank=True,null=True) #文章简介blank针对校验
    status = models.CharField(choices=status_choices,max_length=3,default='0',verbose_name='是否显示')
    # 重写save方法
    def save(self, *args, **kwargs):
        if not self.intro:
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            # 将markdown内容渲染为html内容，然后去掉html标签，截取指定长度的字符作为摘要
            self.intro = strip_tags(md.convert(self.content))[:74]
        super(Article, self).save(*args, **kwargs)
    class Meta:
        verbose_name = u'文章'
        verbose_name_plural = u'文章'
    def __unicode__(self):
        return self.title
class News(models.Model):
    news_choices = (('0','私密'),('1','公开'))
    id  = models.AutoField(primary_key=True,verbose_name='新闻ID')
    newsTitle = models.CharField(max_length=100,null=True,verbose_name='新闻标题')
    newsContent = models.TextField(verbose_name='新闻内容')
    coverImage = models.ImageField(verbose_name='封面轮播图',upload_to='')
    createTime = models.DateTimeField(null=True,verbose_name='新闻采集时间')
    status = models.CharField(choices=news_choices,default='0',null=True,max_length=16,verbose_name='是否生效') #0：表示不生效，1：表示生效

class DailySentence(models.Model):
    daily_choices = (('0','私密'),('1','公开'))
    id = models.AutoField(primary_key=True,verbose_name='每日一句')
    title = models.CharField(max_length=64,verbose_name='标题',null=True)
    dailycontent = models.TextField(verbose_name='内容',null=True)
    status = models.CharField(choices=daily_choices,default='0',max_length=4,verbose_name='是否生效')
    createTime = models.DateField(null=True,verbose_name='时间')
    class Meta:
        verbose_name = u'每日一句'
        verbose_name_plural = u'每日一句'
    def __unicode__(self):
        return self.title

class AccessRecord(models.Model):
    id = models.AutoField(primary_key=True)
    ip = models.CharField(max_length=30,null=True,verbose_name='访问IP')
    accessTime = models.DateTimeField(null=True,verbose_name='时间')
    accessCount = models.IntegerField(null=True,default=1,verbose_name='当天访问次数')
    class Meta:
        verbose_name = '访问用户'
        verbose_name_plural = u'访问用户'
    def __unicode__(self):
        return self.ip
class uyan_comment(models.Model):
    title = models.CharField(max_length=100,verbose_name="文章标题")
    content= models.TextField(verbose_name='评论内容')
    uname = models.CharField(max_length=30,verbose_name='用户名称')
    time= models.DateTimeField(verbose_name="评论时间")
    user_photo= models.CharField(max_length=100,verbose_name="头像")
    class  Meta:
        verbose_name = '友言评论'
        verbose_name_plural = u'友言评论'
    def __unicode__(self):
        return self.content
    
    
    
