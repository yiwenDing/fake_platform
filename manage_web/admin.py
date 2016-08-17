# coding:utf-8
from django.contrib import admin
from models import fake_item,item_type
import const
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# Register your models here.

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

class fake_item_admin(admin.ModelAdmin):
    list_display = ('id','api_version',cell_item_view,'description','behot_time','status')
    # list_filter = ('cell_item',)


class item_type_admin(admin.ModelAdmin):
    list_display = ('type_name',)
    filter_horizontal = ('items',)

admin.site.register(fake_item,fake_item_admin)
admin.site.register(item_type,item_type_admin)