from django.conf.urls import url
from views import *
urlpatterns=[
    url(r'^$',index,name='index'),
    url(r'^login/$',login,name='login'),
    url(r'^account_login/$',account_login),
    url(r'^ad_action/$',ad_action),
    url(r'^group/$',group),
    url(r'^subject/$',subject),
    url(r'^pictures/$',pictures),
    url(r'^PGC/$',PGC),
    url(r'^test_channel/$',test_channel),
    url(r'^UGC/$',UGC),
    url(r'^card/',card),
    url(r'^get_data_id/$',get_data_id),
    url(r'^del_data/$', del_data_from_test),

]
