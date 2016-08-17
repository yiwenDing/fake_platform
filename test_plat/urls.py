"""test_plat URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from manage_web.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^manage_web/',include('manage_web.urls',namespace='manage_web')),
    # url(r'^manage_web/$', index, name='index'),
    # url(r'^manage_web/login/$', login, name='login'),
    # url(r'^manage_web/account_login/$', account_login),
    # url(r'^manage_web/ad_action/$', ad_action),
    # url(r'^manage_web/group/$', group),
    # url(r'^manage_web/subject/$', subject),
    # url(r'^manage_web/picture/$', pictures),
    # url(r'^manage_web/PGC/$', PGC),
    # url(r'^manage_web/test_channel/$', test_channel),
    # url(r'^manage_web/UGC/$', UGC),
    # url(r'^manage_web/card/$', card),
    # url(r'^manage_web/get_data/$', receive_data),
]
