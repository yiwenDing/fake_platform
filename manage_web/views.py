# coding:utf-8
from django.shortcuts import render,render_to_response,HttpResponseRedirect
from django.http import HttpResponse
from django.db.models import Q
# Create your views here.
from models import *
from django.contrib import auth
def index(request):
    fake_item_objects=fake_item.objects.all().filter(cell_item__istartswith=' ')
    return render_to_response('manage_web/index.html',locals())

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


    return HttpResponse('dingyiwen')
    # return render_to_response("manage_web/test_channel.html")
def card(request):
    cards=fake_item.objects.filter(
        # Q(question__contains='channel'),
        Q(cell_item__contains='channel') | Q(cell_item__contains='card') | Q(description__contains='card')
    )
    return render_to_response('manage_web/card.html',locals())

def receive_data(request):
    id=request.GET['id']
    print 'hello'
    id_array=id.split(",")
    cursor=connections['search'].cursor()
    for i in id_array:
        cursor.execute("insert into web_app_fakeitemmodel SELECT * FROM test.manage_web_fake_item WHERE id=%s",[int(i)])
    # print fake_item.objects.get(id=id)
    return id_array


