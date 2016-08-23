# coding:utf-8
from django.shortcuts import render,render_to_response,HttpResponseRedirect
from django.http import HttpResponse
from django.db.models import Q
from django.db import connections,connection
# Create your views here.
from models import *
from django.contrib import auth
def index(request):
    fake_item_objects=fake_item.objects.all().filter(cell_item__istartswith=' ')
    return render_to_response('manage_web/index.html', {'fake_item_objects':fake_item_objects, 'request_user': request.user})

def login(request):
    return render_to_response('manage_web/login.html')

def account_login(request):
    username = request.POST['user']
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    print user, '====='
    if user is not None:  # and user.is_active:
        # correct password and user is marked "active"
        auth.login(request, user)
        return HttpResponseRedirect("/manage_web/")
    else:
        return render_to_response('manage_web/login.html', {'err': 'Wrong username or password!'})



def ad_action(request):
    ads=fake_item.objects.filter(description__icontains="ad")
    return render_to_response("manage_web/ad_action.html",locals())

def group(request):
    groups= fake_item.objects.filter(Q(cell_item__istartswith='g') | Q(description__icontains="group"))
    return render_to_response("manage_web/group.html",locals())

def PGC(request):
    pgcs = fake_item.objects.filter(Q(cell_item__icontains='pgc') | Q(description__icontains="pgc"))
    return render_to_response("manage_web/PGC.html",locals())

def pictures(request):
    gallerys = fake_item.objects.filter(description__icontains='gallery')
    return render_to_response("manage_web/pictures.html",locals())

def UGC(request):
    ugcs = fake_item.objects.filter(cell_item__icontains='user')
    return render_to_response("manage_web/UGC.html",locals())

def subject(request):
    subjects=fake_item.objects.filter(cell_item__icontains='subject')
    return render_to_response("manage_web/subject.html",locals())


def test_channel(request):
    cursor=connections['test_fake'].cursor()
    cursor.execute("select * from web_app_fakeitemmodel")
    test_items=cursor.fetchall()
    item_list_ids=[]
    item_list_apis=[]
    item_list_cell_items=[]
    item_list_descriptions=[]
    item_list_behot_times=[]
    item_list_status=[]
    for item in test_items:
        item_list_ids.append(item[0])
        item_list_apis.append(item[1])
        item_list_cell_items.append(item[2])
        item_list_descriptions.append(item[4])
        item_list_behot_times.append(item[5])
        item_list_status.append(item[6])
    return render_to_response('manage_web/test_channel.html',{'item_list_ids':item_list_ids,'test_items':test_items, 'apis': item_list_apis,'cell_items':item_list_cell_items,'descriptions':item_list_descriptions,'behot_times':item_list_behot_times,'status':item_list_status})
    # return render_to_response("manage_web/test_channel.html")
def card(request):
    cards=fake_item.objects.filter(
        # Q(question__contains='channel'),
        Q(cell_item__contains='channel') | Q(cell_item__contains='card') | Q(description__contains='card')
    )
    return render_to_response('manage_web/card.html',locals())

def get_data_id(request):
    id=request.GET['id']
    print 'hello'
    print id
    id_array = id.split(",")
    print id_array
    cursor = connections['test_fake'].cursor()
    for i in id_array:
        cursor.execute("insert into web_app_fakeitemmodel SELECT * FROM test.manage_web_fake_item WHERE id=%s", [i])
    # cursor.execute("insert into web_app_fakeitemmodel select * from test.manage_web_fake_item where id=%s",[i])
    # print fake_item.objects.get(id=id)
    # return id_array
    return HttpResponse('Hello dingyiwen')

def del_data_from_test(request):
    id=request.GET['id']
    id_array=id.split(",")
    print id
    cursor = connections['test_fake'].cursor()
    for i in id_array:
        cursor.execute("delete from web_app_fakeitemmodel WHERE id = %s", [i])
    return HttpResponseRedirect('/manage_web/test_channel/')

if __name__=='__main__':
    cursor=connections['test_fake'].cursor()
    i=3725353986
    cursor.execute("select * from web_app_fakeitemmodel")
    cursor.fetchall()

