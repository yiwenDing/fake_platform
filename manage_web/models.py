# coding:utf-8
from __future__ import unicode_literals

from django.db import models
from django.db import connections
import const
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

# Create your models here.
def cell_item_view(obj):
    cell_item = obj.cell_item.strip()
    if not cell_item:
        return '无'
    matchobj = const.ITEM_GROUP_PATTERN.match(cell_item)
    if matchobj:
        return matchobj.expand('文章:\g<id>')
    matchobj = const.ITEM_CONTENT_GROUP_PATTERN.match(cell_item)
    if matchobj:
        return matchobj.expand('段子:\g<id>')
    matchobj = const.ITEM_AD_PATTERN.match(cell_item)
    if matchobj:
        return matchobj.expand('广告:\g<id>(模式\g<mode>)')
    matchobj = const.ITEM_CHANNEL_EXPLORE_BLOCK_PATTERN.match(cell_item)
    if matchobj:
        return '频道推荐'
    matchobj = const.ITEM_SUBJECT_CARD_PATTERN.match(cell_item)
    if matchobj:
        return matchobj.expand('专题卡片:\g<id>')
    matchobj = const.ITEM_CHANNEL_EXPLORE_PATTERN.match(cell_item)
    if matchobj:
        return matchobj.expand('频道推荐:\g<category>')
    matchobj = const.ITEM_CHANNEL_EXPLORE_CARD_PATTERN.match(cell_item)
    if matchobj:
        return matchobj.expand('频道推荐卡片')
    return '非法的Item数据'


class online_db_action:
    def fetch_data(self,cursor):
        cursor=connections['search'].cursor()
        cursor.execute("select * from web_app_fakeitemmodel")
        cursor.fetchall()

class fake_item(models.Model):
    id=models.BigIntegerField(primary_key=True,null=False)
    api_version=models.SmallIntegerField()
    cell_item=models.CharField(max_length=128)
    cell_data=models.CharField(max_length=4096)
    description=models.CharField(max_length=64)
    behot_time=models.IntegerField()
    status=models.SmallIntegerField()

    def __unicode__(self):
        return str(self.id)

    class Meta:
        verbose_name="数据项"
        verbose_name_plural="fake数据库"




class item_type(models.Model):
    type_name=models.CharField(max_length=30,verbose_name='类型')
    items=models.ManyToManyField(fake_item,blank=True,verbose_name='业务项')

    # def cell_item_without_null(self):
    #      group=fake_item.objects.filter(cell_item__istartswith='g')
    #      cell_item_without_null = [p.cell_item for p in group]
    #      return cell_item_without_null

    def __unicode__(self):
        return self.type_name
    class Meta:
        verbose_name="业务"
        verbose_name_plural="业务类型"