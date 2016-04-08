"""Creazy_BBS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
import views
urlpatterns = [
    url(r'category/(\d+)/$',views.category,name='category'),
    url(r'article_detaill/(\d+)/$',views.article_detaill,name='article_detaill'),
    url(r'article/new/$',views.new_article,name='new_article'),
    url(r'account/logout$',views.acount_logout,name='logout'),
    url(r'account/login',views.acount_login,name='login'),

]
