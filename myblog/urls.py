"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
import xadmin
xadmin.autodiscover()
from xadmin.plugins import xversion
from django.conf import settings
from django.conf.urls.static import static
import blog.views

xversion.register_models()

urlpatterns = [
    url(r'^admin/', include(xadmin.site.urls),name='xadmin'),
    url(r'^$', blog.views.index,name='index'),
    url(r'^test', blog.views.test,name='test'),
    url(r'^blog/(?P<aid>\d+)/article/$', blog.views.article_content,name='article_content'),
    url(r'^blog/(?P<currPage>\d+)/page/$', blog.views.index,name='index'),
    url(r'^blog/(?P<cateName>\w+)/cate/$', blog.views.cate,name='cate'),
    url(r'^getQiniuToken/',blog.views.getToken,name='get_token'),
    url(r'^dengpei/', blog.views.like,name='like'),
]
urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT )
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT )
